// Datos de cuenta.html (una entrada por escena: cuenta.html?n=1). Ejemplos para probar la plantilla.
// Tiempos en segundos desde el inicio de la escena, sacados de los tiempos por palabra de la voz (ver LEEME.md).
window.CUENTAS={
 "1":{"dur":9.5,"kick":"Ejemplo · la letra pequeña de una cuota","tit":"LA CUOTA DE <span class=\"y\">160 €</span>",
  "fuente":"Ejemplo para la plantilla",
  "filas":[
   {"l":"Entrada","s":"lo que pagas el primer día","v":"10.931 €","t":1.0},
   {"op":"+","l":"48 cuotas de 160 €","s":"160 × 48","v":"7.680 €","t":2.8},
   {"op":"+","l":"Última cuota","s":"la que no sale en grande","v":"17.435 €","c":"r","t":4.6},
   {"r":true,"op":"=","l":"Pagas en total","v":"36.046 €","t":6.6,"tv":7.2,"n":"¡más del doble de lo que parecía!","tn":8.2}]},
 "2":{"dur":8.0,"kick":"Ejemplo · paso 2 de 3","tit":"LO QUE <span class=\"y\">PIERDE</span> EN 3 AÑOS",
  "fuente":"Ejemplo para la plantilla",
  "filas":[
   {"l":"Precio nuevo","v":"30.000 €","t":1.0},
   {"op":"−","l":"Valor a los 3 años","s":"mediana de anuncios reales","v":"18.000 €","t":2.6},
   {"r":true,"op":"=","l":"Pierdes","v":"12.000 €","t":4.2}],
  "parte":{"izq":"40 % perdido","der":"en solo 3 años","frac":0.4,"t0":5.0,"t":5.4},
  "chips":["PRECIO","DEPRECIACIÓN","SEGURO"],"paso":2}
};
