# Clase que representa un automóvil
class Automovil:
    def __init__(self, marca, modelo, año, precio):
        """Inicializa un nuevo automóvil con marca, modelo, año y precio."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.vendido = False  # Indica si el automóvil ha sido vendido

    def __str__(self):
        """Devuelve una representación en cadena del automóvil."""
        estado = "Vendido" if self.vendido else "Disponible"
        return f"{self.marca} {self.modelo} ({self.año}) - ${self.precio:.2f} - {estado}"

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre):
        """Inicializa un nuevo cliente con un nombre."""
        self.nombre = nombre

# Clase que representa la concesionaria
class Concesionaria:
    def __init__(self):
        """Inicializa una concesionaria vacía con un inventario vacío."""
        self.inventario = []
        self.ventas = []

    def agregar_automovil(self, automovil):
        """Agrega un automóvil al inventario de la concesionaria."""
        self.inventario.append(automovil)
        print(f"Agregado: {automovil}")

    def mostrar_inventario(self):
        """Muestra todos los automóviles en el inventario."""
        if not self.inventario:
            print("El inventario está vacío.")
            return
        
        print("Inventario de la concesionaria:")
        for automovil in self.inventario:
            print(automovil)

    def vender_automovil(self, automovil, cliente):
        """Vende un automóvil a un cliente si está disponible."""
        if automovil in self.inventario and not automovil.vendido:
            automovil.vendido = True  # Marcar el automóvil como vendido
            self.ventas.append((automovil, cliente))  # Registrar la venta
            print(f"{cliente.nombre} ha comprado el automóvil: {automovil}")
        else:
            print("El automóvil no está disponible para la venta.")

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Crear una instancia de la concesionaria
    concesionaria = Concesionaria()

    # Crear algunos automóviles
    auto1 = Automovil("Toyota", "Corolla", 2020, 20000)
    auto2 = Automovil("Ford", "F150", 2021, 30000)
    auto3 = Automovil("Honda", "Civic", 2019, 18000)

    # Agregar automóviles a la concesionaria
    concesionaria.agregar_automovil(auto1)
    concesionaria.agregar_automovil(auto2)
    concesionaria.agregar_automovil(auto3)

    # Mostrar el inventario
    concesionaria.mostrar_inventario()

    # Crear un cliente y realizar una venta
    cliente1 = Cliente("Patrick Luna")
    
    # Vender un automóvil al cliente
    concesionaria.vender_automovil(auto1, cliente1)

    # Mostrar el inventario después de la venta
    concesionaria.mostrar_inventario()

    # Intentar vender el mismo automóvil nuevamente
    concesionaria.vender_automovil(auto1, cliente1)

    # Vender otro automóvil al mismo cliente
    concesionaria.vender_automovil(auto2, cliente1)

    # Mostrar el inventario final
    concesionaria.mostrar_inventario()
