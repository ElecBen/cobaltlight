NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


def a_rgb(hexa):
    """Pasa un color hex de 3 o 6 digitos a una tupla (r, g, b)."""
    if len(hexa.lstrip("#")) not in (3, 6):
        raise ValueError("el hex debe tener 3 o 6 digitos")
    t = hexa.lstrip("#")
    if len(t) == 3:
        t = "".join(c * 2 for c in t)
    return tuple(int(t[i:i + 2], 16) for i in (0, 2, 4))


def a_hex(rgb):
    """Pasa una tupla (r, g, b) a la forma #rrggbb."""
    return "#" + "".join("%02x" % max(0, min(255, int(c))) for c in rgb)


def luminancia(rgb):
    """Luminancia relativa segun WCAG, entre 0.0 y 1.0."""
    canales = []
    for c in rgb:
        v = c / 255
        canales.append(v / 12.92 if v <= 0.03928
                       else ((v + 0.055) / 1.055) ** 2.4)
    r, g, b = canales
    return 0.2126 * r + 0.7152 * g + 0.0722 * b
