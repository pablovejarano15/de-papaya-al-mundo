# Montaje: que parezca hecho por una persona

Todo esto lo hacíamos en automático en un PC normal (sin tarjeta gráfica dedicada) con Python, OpenCV y ffmpeg. Cómo
se construye, en `10_herramientas.md`.

## Principios
1. **El primer minuto, al 100 %**: cada plano muestra literalmente lo que dice la voz («pagar con el móvil» no es
   «comprar un móvil»). Después, el primer plano de cada capítulo y los momentos con nombres y cifras. El resto basta con
   que sea razonable.
2. **Nada quieto más de 3-4 s.** Todo plano se mueve un poco (empuje, barrido, parallax).
3. **Intensidad en el gancho, criterio después.** A un público adulto, el zoom + whoosh en cada frase le cansa. Desde el
   minuto 10, edición más ligera: quien sigue ahí ya está interesado.
4. **Natural antes que efectista**: nada que señale lo obvio (un «¡ÉL!» con flecha a un mecánico cuando ya se habla del
   mecánico) ni efectos que no den tiempo a leer. Si no da tiempo a leerlo, no se pone.
5. Lo que delataba a la máquina: pausas iguales, sonidos mal elegidos, zooms que tiemblan y planos que no pegan.
   Cada uno tiene su arreglo abajo.

## Ritmo (canal de coches y dinero; un canal de ingeniería o documental puede ir más lento)
| Tramo | Duración de plano |
|---|---|
| 0-15 s | 1,0-1,7 s, alternando clip y foto real con zoom rápido |
| 15-40 s | 1,6-2,5 s |
| Cuerpo | 2,0-3,2 s |
| Desde el minuto 10 | 3,0-4,8 s, sin destellos ni marcos |
| Documental de ingeniería | 4-6,5 s, sin destellos |

- Los cortes caen en las pausas de la voz (final de frase o coma), nunca a media palabra.
- No repetir planos casi iguales en ~8 planos seguidos; no dos planos aéreos seguidos.
- Destello blanco suave al empezar cada capítulo (y, en el gancho, cada 3-4 cortes).
- Fotos reales: 2 s en el gancho y 3 s en el resto, con acercar, alejar o barrido y frenada suave.
- Lo que hay que leer (un comentario, un titular) dura lo que se tarda en leerlo: ~3 palabras por segundo + 1 s.

## Cámara virtual (lo que más «humaniza» la imagen)
- Los zooms de ffmpeg avanzan a saltos de píxel y tiemblan. Mejor renderizar el movimiento a mano (OpenCV con
  precisión subpíxel): curvas con aceleración y frenada, amplitud según la duración del plano y zoom hacia el sujeto
  (mapa de saliencia).
- Fotos con profundidad → **parallax 2,5D** (un modelo de profundidad pequeño, Depth Anything V2 Small, separa planos);
  capturas, tarjetas y gráficos, con un Ken Burns normal.
- **Golpe**: acercamiento en 5 fotogramas con desenfoque de movimiento y un temblor que se apaga, en la palabra clave.
- Si el clip de stock ya tiene movimiento de cámara, no se le añade otro.
- Curvas comunes para todo lo que se anima: entrada con frenada, muelle con ~3 % de sobrepaso para elementos que se
  desplazan, barrido con desenfoque.

## Elegir el plano bueno
- Para cada plano se descargan varios candidatos y un modelo de imagen-texto local (CLIP o SigLIP 2, multilingüe) los
  ordena por parecido con la búsqueda **y con la frase que suena** en ese momento.
- De cada clip se busca el mejor trozo: sin cortes internos, sin negros ni fundidos, con acción. Si es corto, se
  ralentiza un poco (hasta 0,8×) antes de repetirlo en bucle.
- Si ningún vídeo encaja, una foto con movimiento (nunca dos fotos seguidas).
- Al acabar, lista de **planos flojos** para reescribir su búsqueda o meter una foto real.

## Pausas con criterio
La voz de IA hace todas las pausas iguales. Se alargan los huecos según lo que pasa en el guion:

| Dónde | Pausa |
|---|---|
| Antes de un capítulo | 1,1 s |
| Tras el título del capítulo (para leer el rótulo) | 1,6 s |
| Tras una pregunta retórica | 0,75 s |
| Tras una frase que acaba en cifra | 0,6 s |
| Tras «:» que anuncia algo corto | 0,55 s |
| Fin de párrafo | 0,45 s |

Tope: 2,5 % de la duración total, al menos 9 s entre pausas añadidas y nada en el gancho (allí manda el silencio
dramático, puesto a mano antes de la frase clave).

## Rótulos y planos especiales
- **Rótulo de capítulo o frase lapidaria**: tipografía gigante que se escribe letra a letra (~1,35 s) con cursor y
  sonido de teclado, sobre rejilla con degradado (verde; rojo si es un aviso) o, alternando, sobre hormigón gris con
  letra oscura. En ~1 de cada 6 escenas, solo cuando la escena empieza con una frase rotunda. El de capítulo, el tiempo
  de leerlo.
- **Titular real de prensa** (medio, fecha, titular, entradilla y la frase subrayada). Solo titulares reales; si se
  traduce, se dice.
- **Barras y gráficos con datos reales** (una cifra que crece al decirla, una línea de bolsa con sus hitos).
- **Foto real con el nombre del modelo** escrito arriba a la izquierda en cada puesto de una lista.
- **Lista de modelos en pantalla**: tarjetas por marca que entran una tras otra (1,6 s + 0,35 s por modelo).
- **Timeline panorámico** de la lista, siempre **dentro del primer minuto**, cuando la voz dice «son doce…»: tarjetas en
  la pared curva de un cilindro; la cámara barre 3-4 tarjetas desenfocadas en ~2,2 s y entra en la primera hasta que
  su foto llena la pantalla; justo después, la foto de ese primer puesto (el corte no se nota).
- **Antes / después**: tarjeta roja (lo malo) y verde (lo bueno) que suben con un muelle; la cifra de la derecha cuenta
  al decirla. Cada vez que la voz enfrenta dos cifras.
- **Frase en pantalla**: fondo negro con suelo de rejilla, la frase palabra a palabra con la voz, la clave en verde e
  iconos de línea con brillo. 1-2 en el gancho y una cada 2-3 min para la idea que hay que retener.
- **Índice en tira**: los capítulos en miniaturas que pasan de lado, una vez en el primer minuto y medio.
- **Tarjeta de comentario** de YouTube (modo oscuro) con un comentario real, palabra a palabra.
- **Al menos un plano especial antes del segundo 60** (mejor entre el 20 y el 45, cuando cae la retención).

## Capa de efectos sobre el vídeo (sincronizada con una palabra)
- **Texto grande**: la frase clave en 3-6 palabras gruesas arriba, palabra a palabra con un golpe, la clave en amarillo.
  1-3 en el gancho y uno al arrancar cada puesto. Lo que no dice la voz literalmente o la cifra que duele.
- **Palabras gigantes una a una** en el centro, con el plano desenfocado y oscuro debajo: una tanda en el gancho para
  frases de ritmo («MUCHOS / DURANTE / TODO EL DÍA»).
- **Tarjeta sobre rayos**: el plano se encoge a una tarjeta redondeada con sombra sobre rayos que giran. Para presentar
  un resultado o una prueba, 1-2 por vídeo.
- **Caja de cita** (banda roja, letra blanca gruesa) para lo que dice alguien; **nota** (pastilla blanca) para la idea
  de la frase. Solo cuando aporten.
- **Rotulador a mano sobre el vídeo**: lazo, flecha con nota, subrayado o tachón pegados al objeto aunque la cámara se
  mueva (detección del objeto + seguimiento por puntos). Solo para lo que **no** es obvio (un coche concreto entre
  varios, la cifra de un titular). Objetos en marcha, 2 s como mucho. El plano con trazo va sin zoom y dura ≥ 2,4 s
  desde la palabra.
- **Etiqueta amarilla** abajo a la izquierda con la cifra que se dice («69.800 €», «245 CV»), como mucho 1 cada 8 s.
- Densidad orientativa: ~1 elemento cada 10-12 s en el cuerpo, más en el gancho, ~1 cada 30-40 s desde el minuto 10.
- Nada encima de un plano especial (rótulo, titular, gráfico): pasa al plano siguiente.
- **Nunca emojis 3D ni iconos de pegatina**: quedan baratos.

## Animaciones propias (lo que más sube el nivel)
**El motor y dos plantillas listas para usar están en `animaciones/` (instrucciones en `animaciones/LEEME.md`).**
- Para lo que no hay en stock (cuentas, comparaciones, procesos), animaciones hechas en **HTML/CSS/JS** y capturadas
  fotograma a fotograma con un navegador sin cabeza (Playwright + Edge o Chromium). Cada página tiene una función
  `render(t)` que pinta el instante t (sin animaciones CSS: así el render es exacto y repetible), su duración y su lista
  de efectos de sonido.
- Las cuentas **no van en un panel oscuro con filas que tardan en salir**: fondo de vídeo real en movimiento, cifras
  que cuentan al decirlas, barras que crecen, el resultado que se queda, una pausa de ~1 s antes del resultado.
- Gancho entero programado (vídeo real + tarjetas, contadores, sellos, cartas que se barajan): es lo que más retiene,
  pero lleva tiempo. Mira siempre una hoja de fotogramas antes de renderizar.
- Pizarra: nada de **objetos dibujados a línea** (un coche a rotulador queda feo y hunde la retención). En su lugar,
  «láminas»: fondo blanco, recortes de fotos reales o renders 3D que entran con un muelle, flechas gordas de rotulador
  y textos que se escriben solos (letra Kalam).

## Sonido
- **Gancho sin música**: solo voz y efectos; la música entra con un fundido de 1,5 s hacia el segundo 25.
- **Música por capítulos**: cada capítulo con su pista (alternar estados: tensión, reflexiva, épica…). La anterior se
  funde terminando en el corte. La elige el dueño del canal; Claude no elige música «a oído».
- La música va unos 22 dB por debajo de la voz y **sube +8 dB en las pausas** (con +4 no se nota); se aparta de la voz
  sobre todo en los medios-agudos.
- Voz con una cadena de estudio suave (compresión ligera, EQ) y **volumen final −14 LUFS** en dos pasadas (ganancia +
  limitador, sin bombeo), AAC a 320 kbps y pico verdadero ≤ −1 dBTP (a 192 kbps el AAC rebotaba por encima de 0).
- **Efectos de documental, nunca de memes**: whoosh en la mitad de los cortes del gancho (su pico, justo en el corte),
  teclado en los rótulos, obturador con las fotos reales, crescendo que acaba en el primer rótulo, golpe con el zoom,
  clic + campana en «suscríbete», grave cinematográfico en cada cambio de capítulo. Los de adorno, solo con aire (≥ 0,6 s
  de otro efecto, máximo 2 cada 4 s, nunca el mismo seguido). Todos igualados de pico.
- **Ambientes** bajo la voz (−30 dB, entrando 0,4 s antes del corte) solo cuando no hay duda de lo que se ve: interior
  de coche, calle con tráfico, ciudad de noche, bar, estación, lluvia, gente. **Efectos puntuales solo si se ve la
  acción** (una puerta que se abre, una página), como mucho 1 cada 20 s. Mejor nada que un sonido que no pega (elegir
  solo por parecido de texto puso un motor de grúa bajo un coche).
- Al cambiar algo del audio, **mídelo**: pico verdadero, que la música esté sincronizada (un `adelay` mal puesto la
  adelantó 25 s) y que suba en las pausas.

## Subtítulos
- Si muchos espectadores tienen activados los subtítulos de YouTube (Studio lo dice), **no los quemes**: sube el `.srt`
  (texto del guion + tiempos de la voz) y deja que lo active quien quiera; si no, verían dos juegos.
- Si los quemas: en el gancho, 2-4 palabras gruesas con la que suena en amarillo; después, frases abajo en dos líneas
  escritas palabra a palabra al ritmo de la voz, sin rebotes.

## Final
- 8 s de cola sin voz tras la última palabra: el último plano sigue acercándose despacio y en 1,2 s se oscurece y se
  desenfoca (sin corte), y la música sube +10 dB hasta su fundido. Ahí va la pantalla final.

## Revisión antes de mezclar (obligatoria)
1. **Filtro automático** de planos: casi negros, poco parecidos a su búsqueda, repetidos, logos de marcas de las que no
   se habla, texto ajeno, presentadores, fondos de croma verde.
2. **Hoja de contacto de TODO el stock**: un fotograma pequeño por plano con su escena y su búsqueda. El filtro
   automático se deja muchos fallos absurdos que una hoja enseña en segundos.
3. **El primer minuto, plano a plano**, con lo que dice la voz debajo.
4. Los planos malos se vetan por su id (para que no salten a otra escena) y se reescribe la búsqueda.
5. Mira los avisos del montaje («no encuentro la palabra», «solo 1,9 s para leer la caja») antes de dar la mezcla por
   buena.
6. Para revisar a ojo, como mucho 3-4 fotogramas reducidos: sale barato.
