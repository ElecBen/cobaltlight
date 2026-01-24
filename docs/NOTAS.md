# Notas de diseno

`a_rgb()` acepta la forma corta de tres digitos duplicando cada
uno, que es lo que hace el navegador. No acepta las de cuatro y ocho digitos
con alfa: el modulo trabaja con colores opacos y no quiere decidir como se
compone la transparencia.

La luminancia usa la curva de WCAG 2.1, con el tramo lineal por
debajo de 0.03928. Es mas lenta que un promedio de los tres canales, pero es
la unica que da los mismos numeros que las herramientas de accesibilidad.

`mezcla()` interpola en RGB, no en un espacio perceptual. Para dos
colores parecidos no se nota; para mezclar azul y amarillo, si. Cambiarlo
obligaria a meter una conversion a Lab y el modulo dejaria de ser copiable de
un fichero a otro.
