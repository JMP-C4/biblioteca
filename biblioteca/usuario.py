from dataclasses import dataclass, field
from typing import List


@dataclass
class Usuario:
    id: str
    nombre: str
    libros_prestados: List[str] = field(default_factory=list)

    def prestar_libro(self, isbn: str):
        if isbn in self.libros_prestados:
            raise ValueError("Usuario ya tiene prestado ese libro")
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn: str):
        if isbn not in self.libros_prestados:
            raise ValueError("El usuario no tiene prestado ese libro")
        self.libros_prestados.remove(isbn)

    def tiene_libro(self, isbn: str) -> bool:
        return isbn in self.libros_prestados

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "libros_prestados": list(self.libros_prestados),
        }
