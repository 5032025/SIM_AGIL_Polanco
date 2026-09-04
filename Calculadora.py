def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def restar(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b

def dividir(a, b):
    """Divide dos números y devuelve el resultado. Lanza una excepción si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    # Ejemplos de uso de las funciones
    print("Suma: ", sumar(5, 3))          # Salida: 8
    print("Resta: ", restar(5, 3))        # Salida: 2
    print("Multiplicación: ", multiplicar(5, 3))  # Salida: 15
    try:
        print("División: ", dividir(5, 0))  # Esto lanzará una excepción
    except ValueError as e:
        print(e)  # Salida: No se puede dividir por cero.