import math

def area_triangulo(base, altura):
    return base * altura / 2

def area_circulo(radio):
    return math.pi * radio ** 2

def main():
    print("bienvenido al calculador de areas con python")
    print("seleccione el area que desea calcular")
    print("t - triangulo")
    print("c - circulo")

    opcion = input("ingrese 't' o 'c': ").lower()

    if opcion == "t":
        base = float(input("ingrese valor de base: "))
        altura = float(input("ingrese valor altura: "))
        area_final = area_triangulo(base, altura)
        print(f"resultado area de triangulo: {area_final}")
    elif opcion == "c":
        radio = float(input("ingrese el radio del circulo: "))
        area_final_circulo = area_circulo(radio)
        print(f"El area del circulo es: {area_final_circulo}")

if __name__ == "__main__":
    main()


