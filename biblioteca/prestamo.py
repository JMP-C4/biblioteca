from datetime import datetime
import uuid

class Prestamo:
    """
    Representa un préstamo de un libro a un usuario en la biblioteca.
    """

    def __init__(self, id: str, libro=None, usuario=None, fecha_prestamo=None, libro_isbn=None, usuario_id=None):
        """
        Permite inicializar el préstamo tanto con objetos como con IDs directos.
        """
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.libro_isbn = libro_isbn or (libro.isbn if libro else None)
        self.usuario_id = usuario_id or (usuario.id if usuario else None)
        self.fecha_prestamo = fecha_prestamo or datetime.utcnow()
        self.devuelto = False

    def devolver(self):
        """Marca el préstamo como devuelto, lanza error si ya estaba devuelto."""
        if self.devuelto:
            raise ValueError("El préstamo ya fue devuelto")
        self.devuelto = True

    @classmethod
    def crear(cls, libro_isbn: str, usuario_id: str):
        """Crea un nuevo préstamo con IDs, sin necesitar objetos Libro/Usuario."""
        return cls(
            id=uuid.uuid4().hex,
            libro_isbn=libro_isbn,
            usuario_id=usuario_id,
            fecha_prestamo=datetime.utcnow()
        )

    def to_dict(self):
        """Convierte el préstamo en un diccionario serializable."""
        return {
            "id": self.id,
            "libro_isbn": self.libro_isbn,
            "usuario_id": self.usuario_id,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "devuelto": self.devuelto
        }
