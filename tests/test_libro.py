import pytest
from biblioteca.libro import Libro


def test_creacion_libro():
    l = Libro(isbn="000", titulo="T", autor="X")
    assert l.isbn == "000"
    assert l.titulo == "T"
    assert l.autor == "X"
    assert l.disponible is True


def test_prestar_cambia_disponible():
    l = Libro(isbn="1", titulo="T", autor="A")
    l.prestar()
    assert l.disponible is False


def test_prestar_no_disponible_levanta_error():
    l = Libro(isbn="1", titulo="T", autor="A", disponible=False)
    with pytest.raises(ValueError):
        l.prestar()


def test_devolver_cambia_disponible():
    l = Libro(isbn="2", titulo="T2", autor="B", disponible=False)
    l.devolver()
    assert l.disponible is True


def test_to_dict():
    l = Libro(isbn="3", titulo="TT", autor="C")
    d = l.to_dict()
    assert d["isbn"] == "3"
    assert isinstance(d["disponible"], bool)
