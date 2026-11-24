"""Motor de las animaciones programadas: páginas HTML con una función render(t) → vídeo MP4 (+ WAV de efectos).

    python motor.py prueba <nombre> 0.5 2 4 6   hoja prueba_<nombre>.jpg con esos segundos (MIRARLA antes de renderizar)
    python motor.py video <nombre> [salida.mp4] <nombre>.mp4 + <nombre>.wav
    python motor.py todas <n1> <n2> …            varias, una detrás de otra
    python motor.py sonido <nombre>              solo el WAV de efectos

<nombre> = página (check -> check.html) o página + número (cuenta2 -> cuenta.html?n=2). Las páginas que empiezan por
«short» se capturan en vertical (1080 × 1920); el resto, a 1920 × 1080.

Contrato de cada página (ver cuenta.html y check.html):
- window.DUR = duración en segundos; window.seek(t) pinta el instante t; window.LISTO = true cuando han cargado
  fuentes e imágenes. Sin animaciones CSS: todo se calcula en render(t), así el render es exacto y repetible.
- window.SUB (opcional) = capturas por fotograma: 4 si hay movimiento rápido (desenfoque de movimiento real), 1-2 si no.
- window.SFX (opcional) = [[segundo, "carpeta/archivo.mp3" dentro de sfx/, pico en dB, segundos máx., modo], …];
  modo «ini» (empieza ahí), «pico» (su pico cae ahí) o «fin» (acaba ahí, para crescendos).

Captura con Edge (o el Chromium de Playwright) en varios procesos y funde las capturas de cada treintavo de segundo.
Requisitos: pip install playwright pillow numpy librosa soundfile · python -m playwright install chromium · ffmpeg.
"""
import io
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SFX = Path(os.environ.get("SFX_DIR", AQUI / "sfx"))   # carpeta de efectos (por categorías: whoosh/, pop/, impacto/…)
FPS, SUB, SR = 30, 4, 48000
PROCESOS = max(1, min(8, (os.cpu_count() or 4) - 1))


def url(nombre: str) -> str:
    m = re.fullmatch(r"([a-z_]+?)(\d+)?", nombre)
    return (AQUI / f"{m[1]}.html").as_uri() + (f"?n={m[2]}" if m[2] else "")


def tam(nombre: str) -> tuple[int, int]:
    return (1080, 1920) if nombre.startswith("short") else (1920, 1080)


def abrir(p, nombre: str):
    args = ["--allow-file-access-from-files", "--force-color-profile=srgb", "--disable-lcd-text"]
    try:
        nav = p.chromium.launch(channel="msedge", args=args)
    except Exception:  # noqa: BLE001 — sin Edge: el Chromium de Playwright
        nav = p.chromium.launch(args=args)
    w, h = tam(nombre)
    pag = nav.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
    pag.on("console", lambda m: print("  consola:", m.text[:200]) if m.type in ("error", "warning") else None)
    pag.on("pageerror", lambda e: print("  ERROR JS:", str(e)[:300]))
    pag.goto(url(nombre), timeout=180000)
    pag.wait_for_function("window.LISTO === true", timeout=240000)
    return nav, pag


def prueba(nombre: str, ts: list[float]) -> None:
    from PIL import Image, ImageDraw
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav, pag = abrir(p, nombre)
        w, h = tam(nombre)
        cols, tw, th = (4, 480, 270) if w > h else (6, 270, 480)
        hoja = Image.new("RGB", (cols * tw, ((len(ts) + cols - 1) // cols) * th), (0, 0, 0))
        for i, t in enumerate(ts):
            pag.evaluate("t => window.seek(t)", t)
            im = Image.open(io.BytesIO(pag.screenshot(type="jpeg", quality=88, timeout=180000))).resize((tw, th), Image.LANCZOS)
            ImageDraw.Draw(im).text((6, 4), f"{t:.2f}", fill=(0, 255, 120))
            hoja.paste(im, ((i % cols) * tw, (i // cols) * th))
        nav.close()
    hoja.save(AQUI / f"prueba_{nombre}.jpg", quality=84)
    print("hoja ->", AQUI / f"prueba_{nombre}.jpg", hoja.size)


def tramo(arg: tuple[str, int, int, int]) -> int:
    from playwright.sync_api import sync_playwright
    nombre, a, b, sub = arg
    dst = AQUI / "_frames" / nombre
    with sync_playwright() as p:
        nav, pag = abrir(p, nombre)
        for i in range(a, b):
            pag.evaluate("t => window.seek(t)", i / (FPS * sub))
            (dst / f"{i:05d}.jpg").write_bytes(pag.screenshot(type="jpeg", quality=95, timeout=180000))
        nav.close()
    return b - a


def _cargar(ruta: Path):
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ruta), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).copy()


def _archivo(rel: str) -> Path | None:
    """«rotulador/x» = cualquier archivo de sfx/rotulador; si falta un efecto, se avisa y se sigue sin él."""
    if rel.startswith("rotulador/"):
        d = SFX / "rotulador"
        hay = sorted(d.iterdir()) if d.is_dir() else []
        return hay[min(1, len(hay) - 1)] if hay else None
    return SFX / rel if (SFX / rel).exists() else None


def sonido(dur: float, eventos: list, salida: Path) -> bool:
    """Pista de efectos de la animación (sin voz): cada efecto recortado, igualado de pico y en su segundo."""
    import librosa
    import numpy as np
    import soundfile as sf
    mezcla = np.zeros(int(dur * SR) + SR // 2, np.float32)
    puestos = 0
    for t, rel, db, max_s, *resto in eventos:
        modo = resto[0] if resto else "ini"
        ruta = _archivo(rel)
        if ruta is None:
            print(f"  (sin efecto: falta sfx/{rel})")
            continue
        y, _ = librosa.effects.trim(_cargar(ruta), top_db=38)
        if rel.startswith("rotulador/"):
            y = y[int(0.4 * SR):]
        n = int(max_s * SR)
        if len(y) > n:
            y = (y[-n:] if modo == "fin" else y[:n]).copy()
        if len(y) < 128:
            continue
        f = max(1, min(len(y) // 4, int(0.12 * SR)))
        if modo == "fin":
            k = min(len(y), int(0.3 * SR))
            y[:k] *= np.linspace(0, 1, k)
            y[-int(0.012 * SR):] *= np.linspace(1, 0, int(0.012 * SR))
        else:
            y[-f:] *= np.linspace(1, 0, f)
            y[:64] *= np.linspace(0, 1, 64)
        y = y / (np.abs(y).max() + 1e-9) * 10 ** (db / 20)
        i = int(t * SR) - {"ini": 0, "pico": int(np.argmax(np.abs(y))), "fin": len(y)}[modo]
        if i < 0:
            y, i = y[-i:], 0
        y = y[:max(0, len(mezcla) - i)]
        mezcla[i:i + len(y)] += y
        puestos += 1
    if not puestos:
        salida.unlink(missing_ok=True)
        return False
    sf.write(salida, np.clip(mezcla[:int(dur * SR)], -0.98, 0.98), SR, subtype="PCM_16")
    return True


def video(nombre: str, salida: Path | None = None, solo_sonido: bool = False) -> None:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav, pag = abrir(p, nombre)
        dur = float(pag.evaluate("window.DUR"))
        eventos = pag.evaluate("window.SFX || []")
        sub = int(pag.evaluate("window.SUB || 0") or SUB)
        nav.close()
    salida = salida or AQUI / f"{nombre}.mp4"
    con = sonido(dur, eventos, salida.with_suffix(".wav"))
    print(f"{nombre}: sonido {'-> ' + salida.with_suffix('.wav').name if con else 'sin efectos'}")
    if solo_sonido:
        return
    dst = AQUI / "_frames" / nombre
    shutil.rmtree(dst, ignore_errors=True)
    dst.mkdir(parents=True)
    n = round(dur * FPS) * sub
    paso = -(-n // PROCESOS)
    with ProcessPoolExecutor(PROCESOS) as ex:
        hechas = sum(ex.map(tramo, [(nombre, a, min(n, a + paso), sub) for a in range(0, n, paso)]))
    # Cada fotograma final = media de las capturas de su treintavo de segundo (desenfoque de movimiento real).
    pesos = " ".join("1" * sub)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS * sub), "-i", str(dst / "%05d.jpg"),
                    "-vf", f"tmix=frames={sub}:weights='{pesos}',select='eq(mod(n\\,{sub})\\,{sub - 1})',"
                           "setpts=N/30/TB,format=yuv420p",
                    "-r", str(FPS), "-c:v", "libx264", "-crf", "18", "-preset", "slow", str(salida)], check=True)
    shutil.rmtree(dst, ignore_errors=True)
    print(f"{nombre}: {hechas} capturas, {dur:.2f} s -> {salida}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    if sys.argv[1] == "prueba":
        prueba(sys.argv[2], [float(x) for x in sys.argv[3:]] or [0.5, 2, 4, 6])
    elif sys.argv[1] == "todas":
        for nombre in sys.argv[2:]:
            video(nombre)
    else:
        video(sys.argv[2], Path(sys.argv[3]) if len(sys.argv) > 3 else None, solo_sonido=sys.argv[1] == "sonido")
