# Errores que no hay que repetir

## Contenido y packaging
| Error | Qué pasó | Cómo evitarlo |
|---|---|---|
| Hablar de la miniatura o del vídeo al empezar | Se fue mucha gente entre los segundos 12 y 24 | Directo a la promesa y al primer dato |
| Falso final a mitad del vídeo | La retención cayó en ese minuto | Frases de cierre solo en el último minuto |
| Título y miniatura que cuentan cosas distintas | CTR bajísimo | Título, miniatura y gancho, juntos |
| Promesa positiva («casi perfectos») | Mismo diseño, una fracción de las visitas | Ángulo de aviso y pérdida |
| Minutos de teoría antes del primer puesto | La retención se desplomó justo ahí | Criterios en una frase, primer puesto < 1:30 |
| Lo práctico después del número 1 | Esa parte casi no se vio | Entre el número 2 y el 1 |
| Todos los ganchos con la misma fórmula y billetes | El canal parecía siempre lo mismo | Rotar fórmulas (`04_ganchos.md`) |
| Abrir con un dibujo | «Muy cutre» | Primer plano real y bonito; el dibujo, encima o desde el s. 6 |
| Coches dibujados a línea en la pizarra | Feos, bajan la retención | Recortes de fotos reales y renders 3D |
| Cuentas con muchas cifras dichas deprisa en un panel quieto | Nadie las seguía | Una cifra por frase, construida en pantalla, fondo en movimiento |
| Leer 14 modelos seguidos con la voz | Aburre | Más de 5, escritos en pantalla |
| Miniatura que da la respuesta entera | Nadie hace clic | La mitad de la información |
| Fiarse del juez automático de miniaturas | Iba al revés del CTR real | Mandan los datos reales |
| Etiquetas con restos de plantilla («(si aplica)») | Se publicaron | 10-15 etiquetas reales, revisadas |
| Tres vídeos del mismo tema seguidos | Se quitaron público entre ellos | Alternar temas |
| Recomendar un producto que sale bien en un estudio pero tiene muchas quejas | Riesgo de perder credibilidad | Contrastar con foros y quejas reales antes |
| Personajes con nombre y modelos al azar en las imágenes | Incoherente | Imágenes de su edad y su coche |
| Voz latina deletreando siglas («i te be») en un canal para España | Quejas de los espectadores | Diccionario de pronunciación (`08_voz_y_sonido.md`) |
| Quitar bromas después de generar la voz | Hubo que regenerarla (créditos) | Aprobarlas antes |

## Montaje y stock
| Error | Qué pasó | Cómo evitarlo |
|---|---|---|
| Marcas en las búsquedas de stock | Otra marca en pantalla mientras la voz acusaba | Stock genérico; la marca, con fotos reales |
| Búsquedas abstractas | Cromas verdes, calaveras, vacas | Persona + acción + objeto físico |
| Cambiar solo la búsqueda de un plano malo | El clip saltó a otra escena | Vetarlo por id |
| Vetar por número de plano con una hoja vieja | Se vetó el plano equivocado (los números se corren al rehacer) | Vetar por escena + búsqueda, con la hoja del montaje actual |
| Fiarse solo del filtro automático | Decenas de planos absurdos se colaron | Hoja de contacto de todo el stock |
| Revisar antes de renderizar | «Nada sospechoso» sin haber mirado nada | Revisar siempre después del render |
| Un efecto anclado a las últimas palabras de la escena | «Solo 1,9 s», omitido | Anclarlo con tiempo por delante |
| Zoom de golpe encima de un gráfico | El gráfico no se leía | Sobre planos especiales, efectos cortos o ninguno |
| Rotulador señalando lo obvio | Quedaba ridículo | Solo lo que no es obvio |
| Un texto que se va antes de poder leerlo | Hubo que rehacerlo | ~3 palabras/s + 1 s; los rótulos de capítulo, con pausa |
| Fiarse de que un vídeo es Creative Commons | Era de licencia estándar | Comprobarlo con yt-dlp |
| Fotos de Commons solo con el nombre de la marca | Una bicicleta, unas tazas | «<Marca> logo / producto / sede» y mirar el título |
| Stock que trae otro país (taxis y policía de EE. UU., dólares) | Rompe la credibilidad | «european», «street», persona + acción |

## Audio
| Error | Qué pasó | Cómo evitarlo |
|---|---|---|
| Elegir efectos solo por parecido de texto | Un motor de grúa bajo un coche, puertas sobre coches aparcados | Solo familias inequívocas y acciones que se ven |
| `adelay` sin reajustar los tiempos | La música sonaba 25 s adelantada | Medir la mezcla (correlación, pausas) tras cada cambio |
| AAC a 192 kbps con efectos brillantes | Picos por encima de 0 dB | 320 kbps y pico verdadero ≤ −1 dBTP |
| Música encima del silencio dramático del gancho | Se perdía el efecto | Gancho sin música hasta el s. ~25 o más |

## Herramientas
| Error | Qué pasó | Cómo evitarlo |
|---|---|---|
| Claves del `.env` con el mismo nombre o con «:» | Una pisaba a otra; otra no se leía | `NOMBRE_UNICO=valor`, una por línea |
| Dos procesos del mismo vídeo a la vez | Errores al escribir archivos | Uno solo, en segundo plano con log |
| Pexels / Coverr / Commons con límite por hora | El vídeo esperó o se quedó a medias | Buscar mientras se genera la voz; varias fuentes |
| APIs «gratis» que no lo son tanto | Sin imágenes, sin descargas | Probar antes de contar con ellas |
| `.bat` con saltos de Linux | cmd leía «cho» y fallaba | CRLF y sin tildes |
| Plan gratuito de Gemini saturado | Revisiones de 45 min | Si no avanza, revisar a mano lo importante |
| Paquete que arrastra una versión nueva de OpenCV | Rompió otra herramienta | Fijar versiones (`opencv-python<5`) |
