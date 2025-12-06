import pytest

from colores import BLANCO, NEGRO, a_hex, a_rgb, contraste, luminancia, mezcla


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


def test_luminancia_de_los_extremos():
    assert luminancia(NEGRO) == 0.0
    assert round(luminancia(BLANCO), 3) == 1.0


def test_luminancia_de_un_gris_medio():
    assert 0.1 < luminancia((128, 128, 128)) < 0.3


def test_contraste_maximo():
    assert round(contraste(NEGRO, BLANCO), 1) == 21.0


def test_contraste_de_un_color_consigo_mismo():
    assert round(contraste(NEGRO, NEGRO), 1) == 1.0


def test_contraste_no_depende_del_orden():
    assert contraste(NEGRO, BLANCO) == contraste(BLANCO, NEGRO)


def test_mezcla_al_cincuenta_por_ciento():
    assert mezcla(NEGRO, BLANCO) == (128, 128, 128)


def test_mezcla_en_los_extremos():
    assert mezcla(NEGRO, BLANCO, 0.0) == NEGRO
    assert mezcla(NEGRO, BLANCO, 1.0) == BLANCO
