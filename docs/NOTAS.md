# Notas de diseno

`a_rgb()` acepta la forma corta de tres digitos duplicando cada
uno, que es lo que hace el navegador. No acepta las de cuatro y ocho digitos
con alfa: el modulo trabaja con colores opacos y no quiere decidir como se
compone la transparencia.
