
# # nombre=input()
# # print("ingrese sa edad")
# # edad=input()

# # print("hola", nombre," su edad es",edad)


# # print(" ingrese 3 numeros")
# # n1=int(input("nota1"))
# # n2=int(input("nota2"))
# # n3=int(input("nota3"))
# # prom=(n1+n2+n3)/3
# # print("el promedio es ",prom)

# # if prom>=40:
# #     print("el alumno ha aaprobado ")
# # else:
# #     print(" el aumno ha reprobado")


# edad=int(input("ingrese su edad"))

# if edad>=18:
#     print("el usuario es mayor de edad")
# else:
#     print("el usuario es menor de edad")
# edad=int(input("ingrese su edad"))

# if edad<12:
#     print("usted es un niño ")
# elif edad>=12 and edad<18:
#     print("usted es un adolecente")
# elif edad>=18 and edad<65:
#     print("usted es adulto")
# else:
#     print("usted es un anciano ")

# def convertir_temperatura(valor, unidad):
#     """Convierte temperaturas entre Celsius y Fahrenheit.

#     Parámetros:
#     - valor: número (temperatura a convertir)
#     - unidad: str ("c" para Celsius o "f" para Fahrenheit)

#     Retorna:
#     - float: temperatura convertida
#     """
#     if unidad.upper() == "C":
#         resultado = (valor * 9/5) + 32
#     elif unidad.upper() == "F":
#         resultado = (valor - 32) * 5/9
#     else:
#         raise ValueError(
#             "Unidad no válida. Use 'C' para Celsius o 'F' para Fahrenheit.")
#     return resultado
# pida al usuario ingresar un numero 7 veces y mostrar la suma de todos los numeros
# -------------------------------------------------------------------------------------
# N1
# suma = 0
# for i in range(7):
#     numero = int(input(" ingrese un numero "))
#     suma = suma+numero
#     print(" la suma de los numeros es ", suma)
# -------------------------------------------------------------------------------------
# N2
carrito = 10
limones = 0
cantlimones = 0
cantvegetales = 0
op = 0

int(input("bienvenidos a la feria que vegetales desea comprar?"))
print("1. limones")
print("2. papas")
print("3. zanahorias")
print("4. tomates")
print("5. lechuga")
print("6. espinacas")
print("7. salir")
op = int(input("ingrese la opcion deseada"))
if op == 1:
    cantlimones = int(
        input("ingrese la cantidad de limones que desea comprar"))
    limones = cantlimones * 0.5
    print("el precio de los limones es ", limones)
elif op == 2:
    cantvegetales = int(
        input("ingrese la cantidad de papas que desea comprar"))
    vegetales = cantvegetales * 0.3
    print("el precio de las papas es ", vegetales)
elif op == 3:
    cantvegetales = int(
        input("ingrese la cantidad de zanahorias que desea comprar"))
    vegetales = cantvegetales * 0.4
    print("el precio de las zanahorias es ", vegetales)
elif op == 4:
    cantvegetales = int(
        input("ingrese la cantidad de tomates que desea comprar"))
    vegetales = cantvegetales * 0.6
    print("el precio de los tomates es ", vegetales)
elif op == 5:
    cantvegetales = int(
        input("ingrese la cantidad de lechugas que desea comprar"))
    vegetales = cantvegetales * 0.7
    print("el precio de las lechugas es ", vegetales)
elif op == 6:
    cantvegetales = int(
        input("ingrese la cantidad de espinacas que desea comprar"))
    vegetales = cantvegetales * 0.8
    print("el precio de las espinacas es ", vegetales)
elif op == 7:
    print("gracias por su compra")
else:
    print("opcion no valida")
