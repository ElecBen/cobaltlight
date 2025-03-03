import pytest

from colores import a_hex, a_rgb


def test_a_rgb_de_seis_digitos():
    assert a_rgb("#ff0000") == (255, 0, 0)


def test_a_rgb_de_tres_digitos():
    assert a_rgb("#f00") == (255, 0, 0)


def test_a_rgb_sin_almohadilla():
    assert a_rgb("00ff00") == (0, 255, 0)


def test_a_rgb_con_digitos_de_mas():
    with pytest.raises(ValueError):
        a_rgb("#ff00")


def test_a_hex():
    assert a_hex((255, 0, 0)) == "#ff0000"


def test_a_hex_recorta_lo_que_se_sale():
    assert a_hex((300, -20, 0)) == "#ff0000"


def test_hex_y_rgb_son_inversos():
    assert a_rgb(a_hex((12, 34, 56))) == (12, 34, 56)
