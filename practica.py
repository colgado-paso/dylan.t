# crear un codigo que pida al usuario ingresar su nombre, su edad y su ciudad de residencia
# nombre = input("ingrese su nombre")
# edad = int(input("ingrese su edad"))
# ciudad = input("ingrese su  ciudad de residencia ")
# print(f" hola mi nombre es {nombre}, mi edad es {edad} y vivo en {ciudad}")
# -------------------------------------------------------
# n2 crea u nprograma que pregunte un numero al usuario y muestre si es par o impar
# numero = int(input("ingrese un numero"))

# if numero % 2 == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")
# ---------------------------------------------------------
# n3 haz un programa que imprima los numero del 1 al 10 pero usando for
# for i in range(1, 11):
#     print(i)
# n3.1 haz un programa que imprima los numeros del 1 al 10 pero usando un while
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# -----------------------------------------------------------
# n4
# pedir al usuario que genere un numero random entre 1 y 50
# luego pedir al usuario que adivine el numero
# y mostrar si es correcto o no

import random
numram = random.randint(1, 50)
print(numram)
num = int(input("adivine el numero entre 1 y 50"))
