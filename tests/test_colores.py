from colores import a_rgb


def test_a_rgb_de_seis_digitos():
    assert a_rgb("#ff0000") == (255, 0, 0)


def test_a_rgb_de_tres_digitos():
    assert a_rgb("#f00") == (255, 0, 0)


def test_a_rgb_sin_almohadilla():
    assert a_rgb("00ff00") == (0, 255, 0)
