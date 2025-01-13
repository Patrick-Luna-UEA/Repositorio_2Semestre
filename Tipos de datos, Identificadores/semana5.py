print("Patrick Luna Semana-5 Calculos")

import math  # Importamos la librería math para el cálculo del área del círculo

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2

# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado su lado.
    :param lado: Longitud del lado del cuadrado (float)
    :return: Área del cuadrado (float)
    """
    return lado ** 2

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    return 0.5 * base * altura

# Función principal que interactúa con el usuario
def main():
    """
    Función principal que permite al usuario elegir una figura y calcular su área.
    """
    
    while True:  # Bucle que permite repetir la elección
        # Solicitar al usuario elegir una figura
        print("Elige una figura para calcular su área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Triángulo")
        print("4. Salir")
        
        opcion = int(input("Ingresa el número de la figura (1, 2, 3 o 4): "))

        # Condicional para ejecutar la función correspondiente según la elección del usuario
        if opcion == 1:
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
        
        elif opcion == 2:
            lado = float(input("Ingresa el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area:.2f} unidades cuadradas.")
        
        elif opcion == 3:
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f} unidades cuadradas.")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break  # Salir del bucle y terminar el programa
        
        else:
            print("Opción no válida.")

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
