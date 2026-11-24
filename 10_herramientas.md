# Qué hace falta y cómo se construye el sistema

## Lo que necesitas
**PC**: Windows con un procesador normal basta (todo corre en CPU, sin tarjeta gráfica dedicada). Disco: cada vídeo en
proceso ocupa 5-6 GB (clips, planos, versiones); al subirlo se archiva y se queda en unos cientos de MB.

**Programas** (gratis): Python 3.12 con un entorno virtual (`.venv`), ffmpeg, Git, Microsoft Edge o Chromium (para
renderizar animaciones y miniaturas desde HTML), yt-dlp.

**Paquetes de Python**: requests, numpy, opencv-python (fijado a `<5`: la 5 quita funciones que se usan), Pillow,
faster-whisper, onnxruntime, rembg (recortes con BiRefNet), pedalboard, librosa, pyloudnorm, soundfile, playwright,
gradio_client (Hugging Face), curl_cffi (leer foros sin captcha), google-api-python-client + google-auth-oauthlib
(YouTube), ruff (comprobar el código).

**Modelos locales** (gratis, se bajan solos la primera vez): SigLIP 2 o CLIP (parecido imagen-texto, para elegir
planos), Depth Anything V2 Small (profundidad para el parallax), BiRefNet (recortes), Whisper small (transcripción),
paraphrase-multilingual-MiniLM (parecido entre títulos, para ideas).

**Cuentas y claves** (en un archivo `.env`, formato `NOMBRE=valor`, una por línea, nunca compartido ni subido a Git):
| Servicio | Para qué | Coste |
|---|---|---|
| Claude (Claude Code en el PC) | guion, búsquedas, montaje, código, revisión | plan de pago |
| ElevenLabs | voz | plan de pago (créditos por carácter) |
| Pexels, Pixabay, Coverr, Openverse | stock | gratis (clave de API) |
| Wikimedia Commons | fotos reales | gratis, sin clave |
| Hugging Face | imágenes con IA (FLUX) | gratis con token (~8 al día) |
| Google AI Studio (Gemini) | revisiones y resúmenes | gratis (a veces saturado) |
| Google Cloud: YouTube Data API | leer comentarios y datos públicos; subir | gratis |
| Canva Pro | bases de miniaturas | de pago (gratis con algunos packs de estudiante) |
| vidIQ, TubeLab | outliers, palabras clave, transcripciones | opcionales |

Ojo: la API de subida de YouTube, con un proyecto de Google sin auditar, sube los vídeos en privado bloqueado. Lo
práctico es subir a mano en Studio con todo preparado (ver abajo). Una app de Google en modo «Prueba» pide permiso otra
vez cada 7 días.

## El flujo de un vídeo
Todo con un único programa de línea de comandos (`yt.py <paso> <vídeo>`), un paso por etapa:

1. **Guion** (`guion.txt`, lo escribe Claude) → comprobación automática (`03_guion.md`).
2. **Partes y voz**: trocea el guion en partes de < 4.800 caracteres (con la pronunciación ya aplicada) y genera
   `audio/1.mp3, 2.mp3…` con la API de ElevenLabs.
3. **Escenas**: cada párrafo se trocea en escenas de ~30 palabras.
4. **Búsquedas** (`busquedas.txt`, lo escribe Claude): una línea por escena (formato abajo).
5. **Tiempos**: alineación forzada (o Whisper) → cuándo empieza cada escena y cada palabra.
6. **Pausas** con criterio (`06_montaje.md`).
7. **Stock**: busca en todas las fuentes, descarga, ordena por parecido con la búsqueda y la frase, analiza cada clip
   (mejor trozo, velocidad, foco) y deja un `manifest.json` (plano ↔ recurso).
8. **Render**: cada plano con su movimiento de cámara; los planos especiales (rótulos, titulares, gráficos,
   animaciones HTML) se generan en local. El motor de las animaciones HTML va incluido en `animaciones/`.
9. **Revisar**: filtro automático + hojas de contacto + primer minuto a mano.
10. **Mezcla**: voz + música por capítulos + efectos + ambientes, capa de efectos (textos, rotulador, cajas,
    etiquetas, botón de suscribirse), volumen final −14 LUFS.
11. **Para subir**: una carpeta con todo numerado por dónde va en Studio (vídeo, título, títulos para probar,
    descripción con capítulos y créditos, miniaturas A/B/C, etiquetas, subtítulos `.srt`, texto de Comunidad,
    comentario fijado con pregunta, minutos de los anuncios) y un panel HTML con botones «Copiar».
12. **Archivar** al terminar (a la Papelera, no borrar para siempre): se quitan clips y planos y se dejan una versión
    ligera y las hojas de planos.

Los pasos largos (stock, render, mezcla) se lanzan en segundo plano con su log. **Un solo proceso a la vez por
vídeo** (dos chocan al escribir los mismos archivos).

## Formato de `busquedas.txt` (el «lenguaje» del montaje)
```
## 1 El gancho {tension}                 ← capítulo (N = escena; carpeta de música entre llaves)
1: car stuck in traffic jam; man checking phone in car; empty car dealership at night
1+ foto: Toyota RAV4 2024 | nombre: Toyota RAV4 / híbrido      ← foto real de Commons con el nombre
1* rodear: ¡SOLO 2! @dos                 ← rotulador sincronizado con la palabra «dos»
1* texto: SE PARÓ A LOS *80.000 KM* @paró
3: >> NÚMERO 10 | EL QUE NADIE QUIERE    ← rótulo tecleado al empezar la escena
3+ titular: Medio | 12-03-2026 | Titular real | entradilla | frase a resaltar
5+ barras: Título | Subtítulo | Fuente: … | A:12, B:30, C:7 | B
6+ timeline: 10 Nombre = búsqueda Commons; 9 Nombre = stock: búsqueda en inglés | 4.5
8+ comparar: CALCULADO = 2.600 M€ | REAL = 4.650 M€ @cuatro
9+ pizarra: cuenta | 8                   ← animación propia (HTML) de esa escena
```
- `N:` búsquedas de stock en el orden de la narración; `N+` planos especiales; `N*` efectos encima del plano anclados a
  una palabra (`@palabra`, escrita como en el guion: dígitos si están en dígitos).
- Un efecto no puede anclarse a una de las últimas palabras de la escena (no da tiempo a verlo).

## Para que Claude gaste pocos tokens
- No leer PDFs ni guiones enteros: para ver las escenas, imprimir solo sus primeras palabras.
- Revisión visual con hojas de contacto o 3-4 fotogramas reducidos (`-vf scale=384:-1`), nunca vídeos enteros.
- Los logs largos, filtrados (solo avisos y errores).
- Lo que se aprende, a un archivo de reglas (este manual, `CLAUDE.md` del proyecto) para no redescubrirlo.

## Descartado (y por qué)
- DaVinci Resolve, Premiere, Blender: manuales o piden tarjeta gráfica.
- PySceneDetect: arrastra OpenCV 5 y rompe otras cosas (los cortes internos se detectan con OpenCV directamente).
- Remotion: resuelve gráficos, no los problemas de montaje de aquí.
- Generadores de imágenes «gratis» con marca de agua o calidad baja (Pollinations); la API gratis de Gemini no genera
  imágenes.

## Trucos de Windows
- `.bat` para doble clic: saltos de línea de Windows (CRLF) y sin tildes en los `echo`; el código, en un `.py` aparte.
- Rutas con espacios, siempre entre comillas.
- Tras editar Python, `python -m ruff check --select F,E9 <archivos>` antes de lanzar nada.
