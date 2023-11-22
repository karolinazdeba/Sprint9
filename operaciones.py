def sumar(a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == '__main__':
    print(sumar(4, 5))
    print(restar(10, 3))
    print(multiplicar(2, 3))
    print(dividir(4, 2))
