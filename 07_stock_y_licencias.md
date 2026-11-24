# Stock, fotos reales y licencias

## Fuentes gratis (cuantas más, menos se parecen los vídeos entre sí)
| Fuente | Qué da | Licencia / notas |
|---|---|---|
| Pexels (API gratis) | vídeo y foto | Uso comercial sin atribución. ~200 búsquedas/hora: lanzar las búsquedas mientras se genera la voz |
| Pixabay (API gratis) | vídeo y foto | Uso comercial sin atribución |
| Wikimedia Commons | fotos reales de cosas concretas (marcas, modelos, edificios, personas públicas) y algo de vídeo | CC0, CC BY (con crédito en la descripción), CC BY-SA (con crédito; no vale para miniaturas, obligaría a licenciarla igual). Sin clave; el User-Agent tiene que llevar un enlace o responde 429 |
| Coverr (API gratis) | vídeo | Sin atribución; 50 peticiones/hora |
| Openverse | fotos CC de Flickr y otros | Con crédito |
| Unsplash | fotos | Sin atribución |
| YouTube Audio Library | música y efectos | Sin atribución |
| Sonniss GDC (paquete anual) | efectos de sonido profesionales | Gratis, uso comercial sin atribución; prohibido usarlos para entrenar IA |
| Vídeos CC BY de YouTube y material de prensa de las marcas | planos de un modelo concreto | Comprobar la licencia con `yt-dlp --print "%(license)s"` aunque digan que es Creative Commons («NA» = licencia estándar, no se usa). Nunca recortar ni tapar marcas de agua: si un plano lleva logo ajeno o presentador, no se usa |

- Los créditos de todo lo que lo pida, en la descripción del vídeo (pegar la descripción entera).
- Fotos de Commons de menos de ~800 px o con marca de agua: fuera.

## Cómo escribir las búsquedas
- **En inglés, visuales y concretas: persona + acción + objeto + lugar** («tired businessman walking to office», nunca
  «tired»). Variadas y **en el orden de la narración** (plano 1 → búsqueda 1).
- En el gancho, 5 búsquedas por escena, muy literales: cada frase, su imagen.
- **Nunca nombres de marca ni de modelo en el stock.** Devuelve otra marca y la voz acusa a la que no es: «volvo
  dealership» trajo un Mercedes, «hybrid car badge» un logo de BMW, «toyota corolla» un GT86, «volkswagen electric car»
  un Escarabajo. Las marcas y modelos se enseñan solo con fotos reales (Commons) o vídeos de prensa con licencia; el
  stock, siempre genérico.
- Para una cosa concreta con nombre (empresa, producto, lugar, persona), además del stock genérico, una **foto real**
  de Commons. Los modelos de imagen-texto no distinguen marcas: cualquier rascacielos puntúa como «la sede de X».
- En Commons, la marca sola falla («Zanussi» → una cocina de gas; «Miele» → una bicicleta): busca «<Marca> logo»,
  «<Marca> refrigerator» o la sede, y **mira el título de cada foto** antes de darla por buena.
- Temas genéricos (concesionarios, bancos, aseguradoras): fotos reales de **varias marcas seguidas**, nunca una sola
  mientras la voz acusa.
- Emblemas y figuras de capó, siempre con foto real de esa marca (el stock trae la de otra).

## Búsquedas que fallan siempre (y qué poner)
| Búsqueda | Qué trae | Mejor |
|---|---|---|
| abstractas: «podium», «calendar pages», «charts on screen», «contract document», «calculator», «warranty certificate» | plantillas de croma verde, una calavera, vacas, flores | persona + acción + objeto físico: «man reading warranty booklet», «repairman arriving at front door» |
| «subscribe button», «man pointing», «coworkers arguing», «tapping … button» | **plantillas de croma verde sin recortar** | evitarlas; el filtro automático tiene que marcar el croma |
| «red flag» | banderas de países | «red warning light» |
| «taxi», «police», «financing», «invoices», «budget» | taxis y policías de EE. UU., dólares, el impreso 1040 | añadir «european», «street», o persona + acción |
| «driver hands on wheel», «touchscreen» | el logo del volante de una marca | manos, pantallas sin volante o exteriores |
| «seat belt being fastened» | cinturones de pantalón | «woman fastening seat belt in car» |
| «appliance store aisle» | pasillos de supermercado | «home appliance showroom» |
| «two men», «couple» para dos amigos | una pareja | los personajes por separado y de su edad |
| «small three cylinder engine», «car engine smoke» | V8 clásicos, un Mustang | genérico sin cilindros: «smoke rising from engine bay» |

## Vetos
- Un plano malo no se arregla solo cambiando su búsqueda: el clip sigue entre los candidatos y salta a otra escena. Su
  id va a una lista de excluidos que no se vuelve a usar.
- Lista global de vetos para todos los canales: sesiones de fotos que salen en todos los vídeos (el mismo comercial con
  la misma carpeta azul), carteras vacías, billetes colgados… Por autor + patrón del título.

## Clips con IA (cuando el stock no tiene el plano)
- Interior de un motor, una avería, una metáfora visual: imagen primero con un modelo gratis (FLUX en Hugging Face),
  se aprueba, y luego vídeo a partir de esa imagen con el mismo prompt.
- Sin texto, logos, matrículas ni caras. Un clip = un plano por vídeo; se guardan en una biblioteca reutilizable por
  canal. Si son realistas, declararlo en la subida.
- Lo normal es que todo el material se descargue gratis y se monte en local; la IA de imagen o vídeo (gratis) solo
  rellena huecos concretos. Claude no gasta tokens generando imágenes.
