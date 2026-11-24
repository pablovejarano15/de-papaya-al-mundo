# De papaya al mundo — manual para un canal de YouTube sin cara

Esta carpeta es el método que hemos ido apuntando durante meses al llevar canales de YouTube sin cara: voz de IA,
imágenes y vídeos libres de derechos y montaje automático en el PC, con Claude haciendo de guionista, montador y
analista. Está escrita para ti, Claude: úsala como guía cada vez que ayudes con este canal.

## Cómo usarla
Antes de cada tarea, lee solo el manual que toca:

| Tarea | Leer |
|---|---|
| Elegir nicho, buscar ideas | `02_ideas_y_nicho.md` |
| Título, miniatura y gancho (siempre juntos) | `01_crecer_en_youtube.md`, `04_ganchos.md`, `09_miniaturas.md` |
| Escribir un guion | `03_guion.md`, `04_ganchos.md`, `05_humor.md` |
| Generar la voz | `08_voz_y_sonido.md` |
| Montar el vídeo | `06_montaje.md`, `07_stock_y_licencias.md` |
| Animaciones a medida (cuentas, fichas, ganchos programados) | `animaciones/LEEME.md` (motor + plantillas que funcionan) |
| Subir, medir, monetizar | `01_crecer_en_youtube.md` |
| Instalar y construir las herramientas | `10_herramientas.md` |
| Antes de dar algo por terminado | `11_errores_que_no_repetir.md` |

- Los ejemplos salen de un canal de coches y dinero en España. **Copia el mecanismo, no el tema.**
- Cuando el canal tenga datos en YouTube Studio, apunta lo que funciona en un `aprendizajes.md` propio del canal. Los
  datos de este canal mandan sobre cualquier regla de aquí.
- `pronunciacion.json` es el diccionario de siglas que usamos para que una voz latina diga las cosas como en España
  (ver `08_voz_y_sonido.md`).

## Reglas de oro (si solo lees esto)
1. **Packaging primero.** Título + miniatura + primeros 15 segundos = una sola promesa. Ningún guion se escribe sin
   título y miniatura decididos.
2. **La idea se valida en inglés.** Busca vídeos en inglés que hayan triunfado frente a la media de su propio canal
   (outliers) y comprueba que en español el tema está libre o poco hecho. Se copian el tema, el ángulo y la composición
   de la miniatura; nunca el guion ni la imagen.
3. **Dolor antes que historia.** «No hagas esto si no quieres perder dinero», «los únicos N que merece la pena…»
   funcionan mejor que «la historia de…».
4. **El primer minuto lo decide todo.** Primera frase de ≤ 15-18 palabras con algo concreto en juego, nada de hablar
   del vídeo ni de la miniatura en los primeros 30 s, algo visual que cuente el dato sin voz y, en las listas, el primer
   puesto antes del 1:30.
5. **Nada de falsos finales.** Las frases de cierre, solo en el último minuto. Cada capítulo acaba abriendo una duda.
6. **El vídeo termina presentando otro vídeo del canal** (post hook) con unos segundos de cola para la pantalla final.
7. **Datos verificados** con fuentes serias y contrastados con la experiencia de usuarios reales. Nunca inventar ni
   exagerar.
8. **El primer minuto del montaje, plano a plano**: cada imagen enseña exactamente lo que dice la voz. El resto, que
   sea razonable.
9. **Nada quieto más de 3-4 s, pero natural antes que efectista**: intensidad en el gancho, criterio después, y nada
   que señale lo obvio o que no dé tiempo a leer.
10. **Gratis y local siempre que se pueda**: stock libre, modelos que corren en el PC, ffmpeg. Claude no genera los
    clips del vídeo.
11. **Pregunta al dueño del canal las decisiones estratégicas** (tema, ángulo, qué entra en una lista, fórmula del
    gancho, estructura, duración) con 2-4 opciones y tu recomendación primero. Las frases, búsquedas y detalles de
    montaje los decides tú con estas reglas.
12. **Comprueba antes de decir que algo está hecho**: mira los fotogramas, mide el audio, revisa los avisos.
