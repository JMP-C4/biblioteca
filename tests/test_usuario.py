import pytest
from biblioteca.prestamo import Prestamo
from datetime import datetime


def test_crear_prestamo():
    p = Prestamo.crear(libro_isbn="111", usuario_id="u1")
    assert p.libro_isbn == "111"
    assert p.usuario_id == "u1"
    assert p.fecha_prestamo is not None
    assert p.fecha_devolucion is None


def test_devolver_prestamo():
    p = Prestamo.crear("222", "u2")
    p.devolver()
    assert p.esta_devuelto() is True
    assert p.fecha_devolucion is not None


def test_devolver_dos_veces_levanta_error():
    p = Prestamo.crear("333", "u3")
    p.devolver()
    with pytest.raises(ValueError):
        p.devolver()


def test_to_dict_contiene_claves():
    p = Prestamo.crear("444", "u4")
    d = p.to_dict()
    assert d["libro_isbn"] == "444"
    assert d["usuario_id"] == "u4"


def test_id_unico():
    p1 = Prestamo.crear("a", "1")
    p2 = Prestamo.crear("a", "1")
    assert p1.id != p2.id
