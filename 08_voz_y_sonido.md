# Voz (ElevenLabs) y música

## La voz
- Una voz de la **biblioteca de ElevenLabs** (son de actores que la ceden). **Nunca clonar** voces que no sean tuyas.
- **Una voz por canal**: la voz es parte de la marca. No mezclar voces dentro de un canal; otras voces, para otro canal
  o para una prueba A/B consciente.
- Antes de elegir, genera la misma frase con 3-4 voces y escúchalas (tono serio de narración para documental; más
  rápida y cercana para consumo).
- Modelo rápido y barato (Turbo/Flash) con los ajustes guardados de la voz en la web, para que suene igual en la API.
- Ritmo medido: unas 165-175 palabras por minuto. Coste orientativo: ~0,5 créditos por carácter → ~8.400 créditos por
  3.000 palabras.
- El texto se manda **por partes de < 4.800 caracteres, cortando entre párrafos** (igual que en la web). Si se
  regenera una parte, solo se vuelve a sincronizar esa.
- Las bromas y el guion, aprobados **antes** de generar la voz: rehacerla cuesta créditos.

## Pronunciación (voz latina, público de España)
Las voces latinas deletrean a su manera: «ITV» = «i te be», «BMW» = «be eme doble be», «150 CV» = «ciento cincuenta ce
ve». En España se dice «i te uve», «be eme uve doble», «ciento cincuenta caballos». Las letras que cambian son la **V**
(uve), la **W** (uve doble) y la **Y** (i griega).

Solución que funciona: **no se toca el guion**; antes de mandar el texto a ElevenLabs, un paso convierte las siglas con
un diccionario (`pronunciacion.json`, incluido en esta carpeta):
- siglas del diccionario → cómo se dicen («ITV» → «i te uve», «CV» → «caballos», «kW» → «kilovatios», «km/h» →
  «kilómetros por hora»);
- siglas con cifras o guion y la V o W sueltas → deletreadas con los nombres de España («EV6» → «e uve 6», «CR-V» →
  «ce erre uve», «V8» → «uve 8»);
- una sigla solo de letras con V, W o Y que no esté en el diccionario **para la voz** hasta añadirla (si no, la voz
  latina la diría mal); las que se leen como palabra («IVA», «VIP») van en una lista aparte.
- Después, al sincronizar, las palabras deletreadas («i», «te», «uve») se vuelven a juntar en la sigla, para que los
  subtítulos y los efectos anclados a «ITV» sigan cuadrando.
- Además, un aviso si el guion trae vocabulario de otro país (carro, manejar, celular, computadora, ustedes,
  concesionaria, estacionar…).
Si tu público y tu voz son del mismo país, no te hace falta.

## Sincronizar voz y texto
- Lo más rápido: la **alineación forzada de ElevenLabs** (le das el audio y el texto exacto que se leyó y devuelve el
  tiempo de cada palabra en segundos). Si falla, **Whisper local** (faster-whisper, modelo small, en CPU; tarda más).
- Las palabras del guion se emparejan con las reconocidas (difflib) para saber cuándo empieza cada escena y cuándo
  suena cada palabra (para cortes, efectos y subtítulos).
- Caché por huella del audio: si cambias una parte, solo se retranscribe esa.

## Música
- La elige el dueño del canal (por gusto y por licencia): carpetas por estado de ánimo (tensión, oscura, épica,
  reflexiva, lofi, ambiental) y una lista de pistas para intercalar. Fuentes: YouTube Audio Library o bibliotecas con
  licencia comercial.
- Lo que solía encajar en documentales de consumo: lofi y ambiental. Lo comercial y «viral» queda fuera de tono.
- Por capítulos, bajo la voz, gancho sin música y subidas en las pausas (detalle en `06_montaje.md`).

## Efectos
- Estilo documental. Los elige y descarga el dueño (YouTube Audio Library → Efectos de sonido, sin atribución; Sonniss
  GDC). Por categorías: whoosh, impacto, alerta, dinero, teclado, foto, subida, golpe, firma, suscripción, rotulador.
- Cada efecto se recorta solo (sin silencio inicial) y con una duración máxima por categoría.
- Packs de «efectos virales» descargados de vídeos: solo los genéricos; los de memes, juegos, dibujos, películas y
  canciones, nunca (Content ID y tono barato).
