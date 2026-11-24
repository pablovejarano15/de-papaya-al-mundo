# Guion

## Antes de escribir
- Packaging cerrado (título + miniatura + promesa del gancho).
- Un vídeo de referencia para la estructura (ver `02_ideas_y_nicho.md`).
- Datos verificados con búsqueda web y fuentes serias (organismos oficiales, asociaciones de consumidores, pruebas
  independientes, prensa reconocida). Apunta la fuente de cada cifra.
- **Contraste con la experiencia real**: un producto puede salir muy bien en un estudio y tener muchas quejas de
  usuarios. Antes de **recomendar** algo, mira foros, comentarios de las reseñas más vistas y bases públicas de quejas
  o llamadas a revisión. Si las quejas se repiten, no se recomienda, o se recomienda diciendo el fallo con la voz.
  Las opiniones dan color y sensaciones; las cifras salen de las fuentes oficiales. Nunca presentes una opinión como un
  hecho contra una marca.
- Las decisiones estratégicas (tema, ángulo, qué entra en la lista y con qué filtros, fórmula del gancho, estructura,
  duración), pregúntaselas al dueño con opciones y tu recomendación. Las frases las decides tú.

## Estructura
- **Gancho** (15-45 s): ver `04_ganchos.md`.
- Contexto mínimo, sin teoría.
- **3-6 bloques** con giros; cada capítulo termina abriendo una duda para el siguiente.
- **Cierre**: frase de suscripción + post hook a otro vídeo del canal. Sin despedidas.
- Cada párrafo es una escena del montaje: separa párrafos con una línea en blanco. En las listas, cada puesto abre
  párrafo con «Número X: Nombre.» para poder ponerle su rótulo.

### Listas y rankings
- Nada de bloques de teoría delante: los criterios van en **una frase** dentro del gancho («para entrar aquí, cada coche
  ha pasado cinco filtros: …») y cada criterio se explica dentro del puesto que mejor lo ilustra.
- El gancho ya nombra **un puesto concreto** («uno es el Tesla, y no por lo que crees»).
- **Primer puesto antes del minuto 1:30.** Cuenta atrás.
- **Lo práctico, antes del número 1**: la ley, los pasos y las comprobaciones van entre el número 2 y el número 1,
  abiertos con «Antes del número uno…». Después del número 1, solo matiz, resumen corto y cierre (lo que va después
  del número 1 se ve mucho menos).
- Más de 5 modelos o elementos: la voz dice «afecta a todos estos» y la lista sale **escrita en pantalla**, por grupos,
  el tiempo de leerla. Nunca leer 14 nombres seguidos.

## Reglas de escritura
- **Primera frase ≤ 15-18 palabras**, con una cifra de lo que pasa (no de lo que te vas a gastar) o algo concreto en
  juego.
- **Prohibido en los primeros 30 s**: hablar del vídeo, de la miniatura o del canal.
- **Sin frases de cierre hasta el final real** («en resumen», «para terminar»…).
- **Microtransformación**: de la confusión a la claridad con una acción pequeña, real y aplicable hoy («10 minutos con
  la app del banco: mira estas 3 cosas»), no información genérica.
- **Narrador sin país**: nunca «aquí» o «nosotros» refiriéndose a una nacionalidad; nombra el país («en España…»).
- **Vocabulario del público**: si el canal es para España, palabras de España (coche, conducir, móvil, aparcar,
  vosotros), aunque la voz sea latina.
- **Cuentas pausadas**: en una cuenta con 3 o más cifras, una cifra por frase, de dónde sale cada número, la operación
  dicha con palabras y el resultado repetido en una frase corta. En el montaje, la cuenta se construye en pantalla paso
  a paso (ver `06_montaje.md`). Al cerrar alguna, una broma seca si encaja.
- **Marcas y modelos con nombre y veredicto**, uno a uno.
- Un **titular real** de prensa o un dato llamativo en el primer minuto (mejor entre el segundo 20 y el 45).
- Las cifras en el guion tal como se van a buscar después (si están en dígitos, en dígitos).

## Suscripción y comentarios (dentro del guion)
- Petición de suscripción en el minuto 3-6 (por valor futuro, pegada a un dato que acaba de oírse y nombrándolo), otra
  en el 10-11 en vídeos de más de 12 min y una frase justo antes del post hook. Nunca en el primer minuto.
- Una pregunta a comentarios a mitad del vídeo, tras un veredicto que divida. Una sola, y nunca al final.
- Menciones a otros vídeos del canal a mitad (con tarjeta en ese segundo) y post hook al final.

## La voz de los espectadores
- Antes de cada guion, lee los comentarios del canal relacionados con el tema (YouTube Data API con una clave pública):
  los de propietarios que aportan un dato y los que llevan la contraria.
- Mete **1-3 comentarios reales** dichos con la voz («Un espectador con un BYD me escribió…») y **respóndelos con
  datos**, nunca burlándote. En pantalla, como tarjeta de comentario de YouTube.
- Nunca el nombre de nadie (solo la inicial, «@J***»). Nunca inventar ni cambiar el sentido de un comentario (se puede
  recortar).
- Si hay material, un apartado de 60-100 s a mitad del vídeo («Lo que nos escribís») con 3-4 comentarios de todo el
  canal (la queja más repetida, el que lleva la contraria con un buen argumento, un usuario con un dato), cada uno
  respondido con un dato en pantalla, y que acabe en la pregunta a comentarios.

## Duración
- Una voz de IA normal lee unas 165-175 palabras por minuto. 20 min ≈ 3.500 palabras.
- Para vídeos largos: ideal 20 min o más; 18, suficiente; por debajo de 17, mejor no. Si falta, se añade contenido con
  valor (otra cuenta, un caso real, más comentarios, una comparación), nunca paja.

## Humor
- Pocas bromas (3-5 por vídeo), secas y que salgan del propio dato. Detalle en `05_humor.md`.
- **Lista las bromas aparte y que el dueño las apruebe antes de generar la voz**: quitarlas después obliga a regenerarla.

## Comprobación automática antes de la voz
Merece la pena tener un script que lea el guion y pare la voz si:
- dura menos de 17 min (por palabras);
- la primera frase pasa de 18 palabras o abre con una fórmula prohibida («Si estás a punto de gastarte…»);
- se habla del vídeo o de la miniatura en los primeros 30 s;
- hay petición de suscripción en el primer minuto o falta en el minuto 3-6 / 10-11 / antes del post hook;
- en una lista, el primer puesto entra después del 1:30 o no se nombra ninguno en el gancho;
- falta la pregunta a comentarios a mitad, o hay una en el último 10 %;
- una frase nombra más de 5 modelos;
- hay siglas sin pronunciación definida o palabras de otro país (ver `08_voz_y_sonido.md`).
