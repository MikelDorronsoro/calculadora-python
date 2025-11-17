# calculadora/__init__.py

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")


def pedir_operacion():
    print("Elige una operación:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")

    while True:
        opcion = input("Opción (1-4): ")
        if opcion in {"1", "2", "3", "4"}:
            return opcion
        print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    op = pedir_operacion()
    x = pedir_entero("Introduce el primer número: ")
    y = pedir_entero("Introduce el segundo número: ")

    if op == "1":
        resultado = sumar(x, y)
    elif op == "2":
        resultado = restar(x, y)
    elif op == "3":
        resultado = multiplicar(x, y)
    else:  # "4"
        try:
            resultado = dividir(x, y)
        except ValueError as e:
            print("Error:", e)
        else:
            print("Resultado:", resultado)
        exit(0)

    print("Resultado:", resultado)
