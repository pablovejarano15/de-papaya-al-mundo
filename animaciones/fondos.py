"""Fondos de vídeo real para las animaciones («pausada no es quieta»: una cuenta sobre un panel oscuro quieto aburre).

Saca ~7 s a 30 fps de clips de stock (Pexels, Pixabay…) y los deja en img/bg/<clave>/NNNN.jpg a 640 px (van
desenfocados detrás de la cuenta); con NITIDO, además a 1920 px en img/hd/<clave>/ para enseñarlos nítidos. Escribe
fondos.js con cuántos fotogramas tiene cada uno. En cuentas.js, «bg»: "<clave>" pone ese fondo en la cuenta.

    python fondos.py
"""
import json
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
# clave -> (clip, segundo desde el que se corta). Rutas relativas a esta carpeta o absolutas.
FONDOS = {
    # "concesionario": ("clips/concesionario.mp4", 1.0),
    # "trafico": ("clips/trafico_ciudad.mp4", 0.5),
}
NITIDO = set()  # claves que también se quieren a tamaño completo


def _sacar(src: Path, dst: Path, desde: float, filtro: str, calidad: str) -> int:
    dst.mkdir(parents=True, exist_ok=True)
    if not any(dst.glob("*.jpg")):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{desde:.2f}", "-t", "7", "-i", str(src),
                        "-vf", f"fps=30,{filtro}", "-q:v", calidad, str(dst / "%04d.jpg")], check=True)
    return len(list(dst.glob("*.jpg")))


if __name__ == "__main__":
    cuentas, hd = {}, {}
    for clave, (clip, desde) in FONDOS.items():
        src = Path(clip) if Path(clip).is_absolute() else AQUI / clip
        if not src.exists():
            print("FALTA", clave, src)
            continue
        cuentas[clave] = _sacar(src, AQUI / "img" / "bg" / clave, desde, "scale=640:-2", "5")
        if clave in NITIDO:
            hd[clave] = _sacar(src, AQUI / "img" / "hd" / clave, desde,
                               "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080", "3")
    (AQUI / "fondos.js").write_text("// generado por fondos.py\nwindow.FONDOS=" + json.dumps(cuentas) + ";\nwindow.FONDOS_HD="
                                    + json.dumps(hd) + ";", encoding="utf-8")
    print(len(cuentas), "fondos:", " ".join(f"{k}={v}" for k, v in cuentas.items()))
