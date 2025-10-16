import pytest
from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.usuario import Usuario
from biblioteca.prestamo import Prestamo


@pytest.fixture
def biblioteca():
    b = Biblioteca()
    b.agregar_libro(Libro("001", "El Principito", "Antoine de Saint-Exupéry"))
    b.agregar_libro(Libro("002", "Cien años de soledad", "Gabriel García Márquez"))
    b.registrar_usuario(Usuario("U001", "Juan Pérez"))
    return b
