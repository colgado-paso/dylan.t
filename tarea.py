# calcular el puntaje de credito
# se debe  calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educativo y nacional
# cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.500.001 o mas : 1.000.000
# nivel educacional
# basico : x1, medio: x1.3 , superior: x1.5
# nacionalidad
# chilena : +300.000, extranjera: +0

# def calcular_puntaje_credito(ingresos, nivel_educativo, nacionalidad):

#     if 500000 <= ingresos <= 1000000:
#         puntaje_ingresos = 300000
#     elif ingresos >= 1500001:
#         puntaje_ingresos = 1000000
#     else:
#         puntaje_ingresos = 0


#     if nivel_educativo == 'basico':
#         puntaje_educacion = 1
#     elif nivel_educativo == 'medio':
#         puntaje_educacion = 1.3
#     elif nivel_educativo == 'superior':
#         puntaje_educacion = 1.5
#     else:
#         puntaje_educacion = 1
#     puntaje_final = puntaje_ingresos * puntaje_educacion


#     if nacionalidad == 'chilena':
#         puntaje_final += 300000


#     return puntaje_final


# ingresos = int(input("Ingrese los ingresos mensuales (CLP): "))
# nivel_educativo = input("Ingrese el nivel educativo (basico, medio, superior): ").lower()
# nacionalidad = input("Ingrese la nacionalidad (chilena, extranjera): ").lower()


# puntaje = calcular_puntaje_credito(ingresos, nivel_educativo, nacionalidad)


# print(f"El puntaje de crédito es: {puntaje}")
# ------------------------------------------------------------------------------------------------------------

# import random
# from random import randint


# print("ingrese 2 digitos")

# n1 = int(input("numero 1"))
# n2 = int(input("numero 2"))


# while n1 > n2:
#     print("el numero 2 no puede ser menor ")
#     n2 = int(input("numero 2"))

# num = random.randint(n1,n2)
# print("▄")

# for i in randint(num):
#     print("▄")
# ---------------------------------------------------------
# crea un programa que la cantidad de ramos
# luego pida el promedio por cada materia
# basados en su promedio final, aplica puntaje
# de beneficio
# 4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0 : 800
# agrega puntaje segun carrera
# tecnico :+60, ingenieria +40, diplomado +20

# ramos = int(input(" ingrese la cantidad de ramos "))
# suma = 0
# for i in range(ramos):
#     notaramo = float(input(f"ingrese la nota del ramo {i+1} "))
#     suma += notaramo
# prom = suma/ramos

# if notaramo >= 4.5 and notaramo <= 5:
#     puntaje_beneficio = 300
#     print(f"su puntaje de beneficio es {puntaje_beneficio}")
# elif notaramo >= 5.1 and notaramo <= 6.0:
#     puntaje_beneficio = 500
#     print(f"su puntaje de beneficio es {puntaje_beneficio}")
# elif notaramo >= 6.1 and notaramo <= 7.0:
#     puntaje_beneficio = 800
#     print(f"su puntaje de beneficio es {puntaje_beneficio}")
# else:
#     print("no tiene beneficios")


# carrera = int(input("""
#                     ingrese la carrera
#                     1. tecnico
#                     2. ingenieria
#                     3. diplomado
#                     """))

# if carrera == 1:
#     puntaje_beneficio += 60
# elif carrera == 2:
#     puntaje_beneficio += 40
# elif carrera == 3:
#     puntaje_beneficio += 20
# else:
#     print(" carrera invalida ")
# -----------------------------------------------------------------
# import random

# numram = random.randint(1, 50)
# print(numram)
# intentos = 5
# num = int(input("adivine el numero random entre 1,50 "))

# while numram != num:
#     intentos -= 1
#     if intentos == 0:
#         print("se han agotados los intentos ")
#         break
#     if num < numram:
#         print("el numero a divinar es menor ")
#         print(f"te quedan {intentos} intentos ")
#     else:
#         print("el numero adivinar es mayor ")
# if intentos == 0:
#     print("perdiste ")

# print("felicidades has adivinado el numero ")
# -----------------------------------------------------------------
