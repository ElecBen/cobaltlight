# cobaltlight

Convierte, mezcla y compara colores hex y RGB.

## Uso

```python
from colores import a_rgb, contraste

a_rgb("#f00")                       # (255, 0, 0)
round(contraste((0, 0, 0), (255, 255, 255)), 1)  # 21.0
```

## Estructura

```
colores.py  modulo principal
tests/      tests con pytest
docs/       notas de diseno
```

## API

| funcion | que devuelve |
| --- | --- |
| `a_rgb(hexa)` | la tupla (r, g, b) de un color escrito en hex |
| `a_hex(rgb)` | el color en forma #rrggbb, recortado a 0-255 |
| `luminancia(rgb)` | la luminancia relativa del color, de 0.0 a 1.0 |
| `contraste(a, b)` | la razon de contraste entre dos colores, de 1.0 a 21.0 |
| `mezcla(a, b, peso)` | la mezcla de dos colores; peso 0.0 devuelve `a` |
