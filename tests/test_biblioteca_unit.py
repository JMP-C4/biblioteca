import pytest
from datetime import datetime
from biblioteca.libro import Libro
from biblioteca.usuario import Usuario
from biblioteca.prestamo import Prestamo
from biblioteca.biblioteca import Biblioteca


# ------------------------------
# TESTS PARA CLASE LIBRO
# ------------------------------
def test_crear_libro():
    libro = Libro("123", "Python Básico", "Juan Pérez")
    assert libro.isbn == "123"
    assert libro.titulo == "Python Básico"
    assert libro.autor == "Juan Pérez"
    assert libro.disponible is True


def test_prestar_y_devolver_libro():
    libro = Libro("999", "Flask", "Miguel Grinberg")
    libro.prestar()
    assert not libro.disponible
    libro.devolver()
    assert libro.disponible


# ------------------------------
# TESTS PARA CLASE USUARIO
# ------------------------------
def test_crear_usuario():
    usuario = Usuario("1", "Carlos")
    assert usuario.id == "1"
    assert usuario.nombre == "Carlos"
    assert usuario.libros_prestados == []


def test_prestar_y_devolver_libro_usuario():
    usuario = Usuario("1", "María")
    usuario.prestar_libro("123")
    assert "123" in usuario.libros_prestados
    usuario.devolver_libro("123")
    assert "123" not in usuario.libros_prestados


# ------------------------------
# TESTS PARA CLASE PRESTAMO
# ------------------------------
def test_crear_prestamo():
    usuario = Usuario("1", "Pedro")
    libro = Libro("001", "Clean Code", "Robert Martin")
    prestamo = Prestamo("1", libro, usuario)
    assert prestamo.libro == libro
    assert prestamo.usuario == usuario
    assert prestamo.fecha_devolucion is None


def test_devolver_libro():
    usuario = Usuario("1", "Lucía")
    libro = Libro("001", "Clean Architecture", "Robert Martin")
    prestamo = Prestamo("2", libro, usuario)
    prestamo.devolver()
    assert prestamo.fecha_devolucion is not None
    assert libro.disponible


# ------------------------------
# TESTS PARA CLASE BIBLIOTECA
# ------------------------------
def test_agregar_y_buscar_libro():
    biblioteca = Biblioteca()
    libro = Libro("101", "Django 4", "Adrian Holovaty")
    biblioteca.agregar_libro(libro)
    assert biblioteca.obtener_libro("101") == libro


def test_agregar_y_obtener_usuario():
    biblioteca = Biblioteca()
    usuario = Usuario("10", "José")
    biblioteca.agregar_usuario(usuario)
    assert biblioteca.obtener_usuario("10") == usuario


def test_buscar_por_titulo_y_autor():
    biblioteca = Biblioteca()
    libro = Libro("202", "Machine Learning", "Andrew Ng")
    biblioteca.agregar_libro(libro)
    assert libro in biblioteca.buscar_por_titulo("Machine")
    assert libro in biblioteca.buscar_por_autor("Andrew")


# ------------------------------
# TESTS DE EXCEPCIONES Y ERRORES
# ------------------------------
def test_no_puede_agregar_libro_duplicado():
    biblioteca = Biblioteca()
    libro = Libro("321", "SQL Básico", "Juan Pérez")
    biblioteca.agregar_libro(libro)
    with pytest.raises(ValueError):
        biblioteca.agregar_libro(libro)


def test_eliminar_libro_inexistente():
    biblioteca = Biblioteca()
    with pytest.raises(KeyError):
        biblioteca.eliminar_libro("999")


# ------------------------------
# TEST DE INTEGRACIÓN
# ------------------------------
def test_flujo_completo_prestamo_y_devolucion():
    biblioteca = Biblioteca()
    libro = Libro("888", "React", "Facebook Team")
    usuario = Usuario("1", "Andrés")

    biblioteca.agregar_libro(libro)
    biblioteca.agregar_usuario(usuario)

    prestamo = biblioteca.prestar("888", "1")
    assert not libro.disponible
    assert prestamo.libro == libro
    assert prestamo.usuario == usuario

    prestamo.devolver()
    assert libro.disponible
    assert prestamo.fecha_devolucion is not None
