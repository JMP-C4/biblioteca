from typing import Dict, List
from .libro import Libro
from .usuario import Usuario
from .prestamo import Prestamo
from datetime import datetime



class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}

    def agregar_libro(self, libro: Libro):
        if libro.isbn in self.catalogo:
            raise ValueError("El libro ya existe en el catálogo")
        self.catalogo[libro.isbn] = libro

    def obtener_libro(self, isbn: str) -> Libro:
        try:
            return self.catalogo[isbn]
        except KeyError:
            raise KeyError("Libro no encontrado")

    def eliminar_libro(self, isbn: str):
        if isbn not in self.catalogo:
            raise KeyError("Libro no encontrado")
        del self.catalogo[isbn]

    def listar_libros(self) -> List[Libro]:
        return list(self.catalogo.values())

    def agregar_usuario(self, usuario: Usuario):
        if usuario.id in self.usuarios:
            raise ValueError("Usuario ya existe")
        self.usuarios[usuario.id] = usuario

    def obtener_usuario(self, user_id: str) -> Usuario:
        try:
            return self.usuarios[user_id]
        except KeyError:
            raise KeyError("Usuario no encontrado")

    def buscar_por_titulo(self, texto: str) -> List[Libro]:
        t = texto.lower()
        return [l for l in self.catalogo.values() if t in l.titulo.lower()]

    def buscar_por_autor(self, autor: str) -> List[Libro]:
        a = autor.lower()
        return [l for l in self.catalogo.values() if a in l.autor.lower()]

    def prestar(self, isbn: str, user_id: str) -> Prestamo:
        if user_id not in self.usuarios:
            raise KeyError("Usuario no existe")
        if isbn not in self.catalogo:
            raise KeyError("Libro no existe")

        libro = self.catalogo[isbn]
        usuario = self.usuarios[user_id]

        if not libro.disponible:
            raise ValueError("El libro no está disponible")

        libro.disponible = False
        prestamo = Prestamo(str(len(self.prestamos) + 1), libro, usuario, datetime.utcnow())
        self.prestamos[prestamo.id] = prestamo
        usuario.prestar_libro(isbn)
        return prestamo

    def devolver(self, isbn: str, user_id: str):
        if user_id not in self.usuarios:
            raise KeyError("Usuario no existe")
        if isbn not in self.catalogo:
            raise KeyError("Libro no existe")

        usuario = self.usuarios[user_id]
        libro = self.catalogo[isbn]

        usuario.devolver_libro(isbn)
        libro.disponible = True

        for p in self.prestamos.values():
            if p.libro == libro and p.usuario == usuario and not p.esta_devuelto():
                p.devolver()
                return p

        raise KeyError("Préstamo no encontrado")
