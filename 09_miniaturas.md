# Miniaturas

## La lección principal
**La luz, los materiales y la historia van en la foto base, no se añaden después.** Una base donde lo malo se ve viejo y
gastado y la luz roja/verde cae de verdad sobre el objeto gana siempre a una base neutra con brillos añadidos por
software.

## Flujo
1. **Composición de referencia**: una miniatura que ya funcionó (outlier en inglés del mismo tema). Se copia la idea y
   la composición, **nunca la imagen** (riesgo de strike).
2. **Base sin texto**, por orden de calidad: Canva Pro (Magic Media, la que mejor sigue el prompt), ChatGPT, FLUX Krea
   gratis en Hugging Face (muy fotográfica, ~8 imágenes al día gratis, no respeta bien el orden de los objetos), o una
   **foto real** de Commons (CC0/CC BY) recortada.
3. **Prompt** (en inglés): sujeto grande (60-80 % del alto), orden exacto de izquierda a derecha, hueco oscuro arriba
   para el título, la historia en los materiales (el que pierde: viejo, abollado, sucio; el que gana: nuevo,
   impecable), la luz de color pedida («red rim light from behind», «green glow behind»), suelo con reflejos,
   «realistic, not neon, not cartoon», «no text, no logos, no watermark». Pide 2 variantes a la vez.
4. **Composición por código** (HTML/CSS renderizado con el navegador, o Pillow): recorte del sujeto (BiRefNet/rembg),
   gradación moderada, textos, iconos ✗/✓, flechas, etiquetas, tarjetas.
5. **Revisión**: vista de móvil (170 px), en gris y con la duración encima, al lado de la referencia.
6. **2-3 variantes** para «Probar y comparar», cambiando el **mensaje** (orden, dato, pregunta), no solo el color.

## Reglas de diseño
- **Un solo héroe** grande (65-70 % del lienzo, tres cuartos o perfil, nítido, fondo oscuro o desenfocado). En un canal
  de coches, un coche real y reconocible también en temas abstractos (financiar, taller, seguros): el papel o la pieza,
  como mucho de apoyo. Un coche genérico de IA «no se reconoce».
- **Un mensaje de ≤ 4 palabras** que **remate el título, nunca lo repita**: el título plantea la premisa; la miniatura,
  el veredicto visceral.
- **Dos niveles de texto** que funcionaron muy bien: banda amarilla con letra negra (choque o pregunta, 2-4 palabras) +
  banda roja con letra blanca (veredicto, 2-3 palabras: «¡NO LO COMPRES!»).
- **Exactamente un ancla de tensión**: flecha roja curva a un fallo, triángulo de aviso o una cifra que duele.
- **No regales la respuesta**: un precio y la pregunta por el otro, el mito y «NO ES ESO». Con las dos cifras ya no
  queda nada que descubrir y nadie hace clic.
- Veredicto con color: rojo/✗ lo que pierde, verde/✓ lo que gana. Exagerado pero creíble (cifras 3D, objeto ampliado
  con brillo, lados rojo/luminoso).
- Coche blanco o claro a plena luz rindió mejor que coches oscuros de noche.
- Personas, opcionales y sobrias (ceño fruncido, mirada escéptica); nada de caras sobreactuadas.
- Esquina inferior derecha libre (la tapa la duración).
- Logos de marca: ayudan a enganchar si es la marca protagonista; logos de Commons; nunca logos de terceros junto a
  texto acusatorio.
- Prueba del móvil: lo que no se lee a 170 px en 0,3 s, fuera.
- El vídeo tiene que cumplir lo que promete la miniatura.

## Capas y profundidad (técnica de los tutoriales de Canva que funcionan)
- Sujeto recortado con **sombra paralela** (sin ella parece una pegatina) sobre un fondo degradado que se aclara detrás.
- Ajustes solo en el sujeto: brillo, contraste, saturación y textura arriba; viñeta suave.
- **El título grande asoma por detrás del sujeto**, que tapa como mucho el 10-15 % de las letras y nunca la parte que
  las distingue.
- **Rayos detrás del sujeto, casi transparentes** (10-15 % de opacidad; más, parece plantilla).
- **Tarjeta inclinada con borde blanco** para la segunda cosa (el rival, la prueba), grande y clara.
- Fuentes gratis (Google Fonts, OFL): Anton, Bebas Neue, Lilita One, Montserrat, Archivo Black, Oswald.

## Jueces automáticos
Un modelo (Gemini gratis) puntuando miniaturas es **ruidoso y puede ir al revés del CTR real** (premió con 90 la que
peor funcionó y con 55 las que más pinchan del canal). Úsalo solo para pillar fallos de lectura (texto cortado,
confuso). Para decidir mandan los datos reales del canal y las referencias en inglés que funcionaron.
