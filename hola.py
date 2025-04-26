
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
