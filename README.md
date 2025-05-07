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
