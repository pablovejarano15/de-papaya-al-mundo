# Animaciones programadas (el nivel más alto del montaje)

Lo que más sube la calidad y la retención de un vídeo sin cara: animaciones hechas a medida, con datos reales, que
cada cifra aparece justo cuando la dice la voz. Se hacen con **HTML/CSS/JS** (lo que mejor escribe Claude) y un motor
en Python las convierte en vídeo, fotograma a fotograma, con desenfoque de movimiento real.

## Qué hay en esta carpeta
| Archivo | Qué es |
|---|---|
| `motor.py` | El motor: abre cada página en un navegador sin ventana, captura cada instante y monta el MP4 (+ un WAV con los efectos) |
| `comun.js` | Utilidades comunes: curvas de animación (`E.out5`, `E.back`, `E.spring`…), entradas (`pop`, `sube`), trazos de rotulador (`trazo`/`dib`), cifras con puntos (`miles`) y fondo de vídeo (`fondoVideo`) |
| `base.css` | Estilo común (fondos oscuros, colores, letras) |
| `cuenta.html` + `cuentas.js` | **Cuenta paso a paso**: cada cifra entra al decirla con su origen debajo, la operación en un círculo, el resultado que cuenta hasta su valor y se queda, barras automáticas para comparar, nota a rotulador, barra partida y pasos abajo. Opcional: objeto real recortado a la izquierda y fondo de vídeo real |
| `check.html` | **Lista de comprobaciones**: número gigante, título que se escribe, líneas ✓/✕ y pasos |
| `fondos.py` | Saca fotogramas de clips de stock para usarlos de fondo (en movimiento, desenfocado) |
| `creditos.js`, `fondos.js` | Créditos de las imágenes y lista de fondos (los rellenan tú o `fondos.py`) |

## Instalar (una vez)
```
pip install playwright pillow numpy librosa soundfile
python -m playwright install chromium
```
- **ffmpeg** instalado y en el PATH.
- **Fuentes** (gratis, Google Fonts, licencia OFL) en `animaciones/fuentes/`:
  - https://github.com/google/fonts/raw/main/ofl/anton/Anton-Regular.ttf
  - https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat%5Bwght%5D.ttf (guardarla como `Montserrat[wght].ttf`)
  - https://github.com/google/fonts/raw/main/ofl/kalam/Kalam-Bold.ttf
- **Efectos de sonido** (opcional) en `animaciones/sfx/<categoría>/` o en la carpeta que diga la variable `SFX_DIR`.
  Las plantillas usan `whoosh/whoosh.mp3`, `whoosh/whoosh-clean.mp3`, `pop/pop.mp3`, `pop/Pop 1.wav`,
  `pop/Pop (2).mp3`, `dinero/Digital counting.mp3`, `impacto/Hard Hit 4.mp3` y cualquier archivo de `rotulador/`.
  Cambia los nombres por los tuyos (YouTube Audio Library, sin atribución). Si falta uno, el motor avisa y sigue.

## Probar
```
python motor.py prueba cuenta1 0.5 1.5 3 5 7 9    → prueba_cuenta1.jpg (hoja con esos segundos)
python motor.py video cuenta1                     → cuenta1.mp4 + cuenta1.wav
python motor.py video check2
```
**Mira siempre la hoja de prueba antes de renderizar**: un render cuesta minutos; una hoja, segundos.

## Cómo se sincroniza con la voz
- Cada animación ocupa una escena del vídeo. Sus tiempos (`t`) son **segundos desde que empieza esa escena**.
- Salen de los tiempos por palabra de la voz (la alineación forzada de ElevenLabs o Whisper con `word_timestamps`):
  tiempo de la palabra − inicio de la escena. Lo cómodo es un script que, dada una frase o una palabra («cuarenta y
  ocho»), devuelva su segundo y escriba `cuentas.js` solo.
- El MP4 se monta en su escena y el WAV de efectos se mezcla con el resto del sonido.

## Formato de `cuentas.js` (una entrada por escena)
```
"1": {"dur": 9.5,                       duración de la escena
      "kick": "texto pequeño de arriba", "tit": "TÍTULO con <span class=\"y\">amarillo</span>",
      "fuente": "Fuente: … (abajo a la izquierda)",
      "filas": [
        {"l": "Etiqueta", "s": "de dónde sale", "v": "10.931 €", "t": 1.0},
        {"op": "+", "l": "…", "v": "7.680 €", "t": 2.8, "c": "r"},       c: r rojo, g verde, w blanco, y amarillo
        {"op": "+", "l": "…", "v": "17.435 €", "t": 4.6, "n": "nota a rotulador", "tn": 5.4},
        {"r": true, "op": "=", "l": "Resultado", "v": "36.046 €", "t": 6.6, "tv": 7.2}],   tv: la cifra sale después de la fila
      "img": "nombre", "nombre": "MODELO", "sub": "subtítulo",   objeto recortado en img/nombre.png (opcional)
      "bg": "clave",                                              fondo de vídeo de fondos.py (opcional)
      "abre": 1.2, "respira": 8.0,                                vídeo nítido antes y después de la cuenta
      "sigue": true, "nuevo": true,                               continúa la cuenta de la escena anterior
      "parte": {"izq": "40 % perdido", "der": "en 3 años", "frac": 0.4, "t0": 5.0, "t": 5.4},
      "chips": ["PASO 1", "PASO 2", "PASO 3"], "paso": 2,
      "chip": {"txt": "FUENTE: OCU", "t": 0.8}}                   la fuente grande mientras la voz la presenta
```
- `"antes": "20.000 €"` + `"tx0": 3.1` = cifra vieja tachada con la nueva al lado.
- Las filas con cifra y la misma unidad (al menos dos) llevan barras que crecen solas para compararlas.

## Reglas para que queden bien
1. **Pausada no es quieta**: fondo de vídeo real en movimiento, cámara que empuja un poco, cifras que cuentan, barras
   que crecen. Nunca un panel oscuro con filas que tardan en salir.
2. **Cada cifra cuando la dice la voz**, con su origen debajo; el resultado se queda y se resalta; una pausa de ~1 s en
   la voz antes del resultado.
3. Una cifra por frase en el guion. Si la cuenta es larga, se reparte en varias escenas con `sigue`.
4. Sin animaciones CSS ni `setTimeout`: todo sale de `render(t)`, para que cualquier segundo se pueda pintar igual.
5. `window.SUB = 4` si hay movimiento rápido (barridos, cartas que vuelan); 1-2 si no (renderiza antes).
6. Textos que se autoajustan: mide con `scrollWidth` y escala; un contenedor `display:flex` mide siempre el ancho del
   padre (usa `inline-flex` si lo vas a medir).
7. Imágenes recortadas: fotos reales (Commons CC0/CC BY con su crédito en `creditos.js`) recortadas con rembg/BiRefNet.
   Si la foto tiene otro objeto pegado detrás, el recorte se lo lleva: elige otra foto. Un coche oscuro necesita más
   luz en el estudio.
8. Nada de objetos dibujados a línea (quedan cutres): fotos recortadas, renders 3D o formas sencillas.

## Pedirle a Claude animaciones nuevas
Las dos plantillas son el ejemplo del contrato. Para cualquier otra cosa, pídeselo así:

> Hazme una página `nombre.html` para `animaciones/` siguiendo el contrato de `motor.py` (window.DUR, window.seek,
> window.LISTO, window.SFX; todo en una función render(t), sin animaciones CSS), con `base.css` y `comun.js`. Tiene que
> durar X s y enseñar: [qué pasa, en orden, con el segundo en que lo dice la voz]. Fondo de vídeo real en movimiento.
> Después, `python motor.py prueba nombre …` con 8 segundos repartidos y mira la hoja antes de renderizar.

Ideas que funcionaron muy bien:
- **Gancho entero programado** (40-55 s): vídeo real de fondo + lazo de rotulador + contador de días + sello con un
  silencio + pantalla partida + cartas boca abajo que se barajan sin destripar el ranking y se reparten Nº 10…Nº 1.
- **Ficha de cada puesto**: el producto real recortado «en estudio» (suelo con reflejo) y sus datos entrando cuando los
  dice la voz; sello «FUERA» para los descartados, precio tachado, nota a rotulador.
- **Marcador**: las mismas cartas del gancho; tras cada puesto se da la vuelta la suya con su veredicto.
- **Cadena de responsabilidad**: tú → vendedor → fabricante, con el objeto (la garantía) viajando y quedándose donde
  se atasca.
- **Dos líneas que se tocan**: lo que vale algo frente a lo que cuesta arreglarlo, hasta que se cruzan.
- **Resumen final**: huecos con «?» que se llenan con la respuesta de cada caso.
- **Versión vertical** para Shorts: páginas que empiezan por `short` (1080 × 1920), dejando libre arriba el título y
  la franja de subtítulos.
