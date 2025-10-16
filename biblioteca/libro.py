from dataclasses import dataclass
from typing import Dict


@dataclass
class Libro:
    isbn: str
    titulo: str
    autor: str
    disponible: bool = True

    def prestar(self):
        """Marca el libro como prestado si está disponible."""
        if not self.disponible:
            raise ValueError("El libro no está disponible para prestar")
        self.disponible = False

    def devolver(self):
        """Marca el libro como disponible si estaba prestado."""
        if self.disponible:
            raise ValueError("El libro ya está marcado como disponible")
        self.disponible = True

    def to_dict(self) -> Dict[str, object]:
        """Convierte el libro a un diccionario (útil para serialización o depuración)."""
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible,
        }
