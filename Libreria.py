# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, precio):
        """Inicializa un nuevo libro con título, autor y precio."""
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f"{self.titulo} por {self.autor} - ${self.precio:.2f}"

# Clase que representa una tienda de libros
class TiendaDeLibros:
    def __init__(self):
        """Inicializa una tienda vacía con un inventario vacío."""
        self.inventario = []

    def agregar_libro(self, libro):
        """Agrega un libro al inventario de la tienda."""
        self.inventario.append(libro)
        print(f"Agregado: {libro}")

    def mostrar_inventario(self):
        """Muestra todos los libros en el inventario."""
        if not self.inventario:
            print("El inventario está vacío.")
            return
        
        print("Inventario de la tienda:")
        for libro in self.inventario:
            print(libro)

    def buscar_libro(self, titulo):
        """Busca un libro por su título y lo devuelve si se encuentra."""
        for libro in self.inventario:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre):
        """Inicializa un nuevo cliente con un nombre."""
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, libro):
        """Agrega un libro al carrito del cliente."""
        self.carrito.append(libro)
        print(f"{libro.titulo} ha sido agregado al carrito de {self.nombre}.")

    def mostrar_carrito(self):
        """Muestra los libros en el carrito del cliente."""
        if not self.carrito:
            print(f"{self.nombre}, tu carrito está vacío.")
            return
        
        print(f"Carrito de {self.nombre}:")
        for libro in self.carrito:
            print(libro)

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Crear una instancia de la tienda
    tienda = TiendaDeLibros()

    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 15.99)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 12.50)
    libro3 = Libro("1984", "George Orwell", 10.00)

    # Agregar libros a la tienda
    tienda.agregar_libro(libro1)
    tienda.agregar_libro(libro2)
    tienda.agregar_libro(libro3)

    # Mostrar el inventario
    tienda.mostrar_inventario()

    # Crear un cliente
    cliente1 = Cliente("Patrick Luna")

    # Buscar y agregar un libro al carrito del cliente
    libro_buscado = tienda.buscar_libro("1984")
    if libro_buscado:
        cliente1.agregar_al_carrito(libro_buscado)

    # Mostrar el carrito del cliente
    cliente1.mostrar_carrito()
