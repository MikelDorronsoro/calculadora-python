# calculadora/__init__.py

def sumar(a, b):
    return a + b

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    x = pedir_entero("Introduce el primer número: ")
    y = pedir_entero("Introduce el segundo número: ")
    print("La suma es:", sumar(x, y))
