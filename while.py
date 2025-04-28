# suma = 0
# while True:
#     num=int(input("ungrese un numero , cero para salir"))
#     if num==0:
#         break
#     suma+=num
#     PermissionError(suma)
#     print(f"la suma total es {suma}")
# ------------------------------------------------
# Ejercicio 1

# pida al usuario el limite inferior y superior de un rango
# despues genere u numero al azar dentro de ese rango
# el segundo numero no , debe ser menor que el primero

# import random

# print(" ingrese dos numeros")
# num1=int(input("ingrese el primer numero"))
# num2=int(input("ingrese otro numero mayor que el primero"))


# numram=random.randint(num1,num2)

# print(numram)
# ------------------------------------------------------
# ejercicio 2
# import random

# print(" ingrese dos numeros")
# num1=int(input("ingrese el primer numero"))

# num2=int(input("ingrese otro numero mayor que el primero"))

# while num2<num1:
#     print("el numero debe ser mayor al anterior")
#     num2=int(input("ingrese otro numero mayor que el primero"))


# numram=random.randint(num1,num2)

# print(numram)
# -------------------------------------------------------
# ejercicio 3
#  pida al usuario que genere un numero random entre 1 y 50
# luego pida al usuario que adivine el numero

# import random
# numram=random.randint(1,50)
# print(numram)

# num=int(input("adivia el numero random entre 1,50"))

# while numram!=num:
#     if num<numram:
#         print("el numero a adiviniar es menor")
#     else:
#         print("el numero a adiviniar es mayor")
# print("felicidades has adivinado el numero")
# ---------------------------------------------------------------
# ejercicio 4

# import random

# numram = random.randint(1, 50)
# print(numram)
# intentos = 5
# num = int(input("adivia el numero random entre 1,50"))

# while numram != num:
#     intentos -= 1
#     if intentos == 0:
#         print("se han agotado los intentos")
#         break
#     if num < numram:
#         print("el numero a adiviniar es menor")
#         print(f"te quedan {intentos} intentos")
#     else:
#         print("el numero a adiviniar es mayor")
# if intentos == 0:
#     print("perdiste")

# print("felicidades has adivinado el numero")
# ----------------------------------------------------------------
import random


numram = random.randint(1, 50)
print(numram)
print("Adivine el numero entre 1 y 50")
intentos = 5

num = int(input())

while numram != num:
    intentos -= 1
    if intentos == 0:
        print("se han agotado los intentos")
        break
    if num > numram:
        print("El numero a adivinar es menor")
    else:
        print("El numero a adivinar es mayor")
    print(f"te quedan {intentos} intentos")
    num = int(input())

if intentos == 0:
    print("Perdiste")
else:
    print("SOS UN GENIO, ADIVINASTE EL NUMERO")
# ----------------------------------------------------------------
# ejercicio 5
# designe 2 peleadoras solicitando sus nombres y puntos de vida
# cada peleador tendra 50 puntos de vida y  debe mostrar barra de vida
# las peleas son por turnos cada turno el peleador ataca entre 3 y 15
# existe posibilidad de atacaque critico del 20 %
# gana el que le quite toda la vida al otro

# print("ingrese los nombres de los peleadores")
# p1=input("peleador 1")
# p2=input("peleador 2")
# p1v=50
# p2v=50
# turno=random.randint(1,2)

# while p1v>0 and p2v>0:
#     if turno %2==0:
#         print("turno de",p1)
#         ataque=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataque*2
#             print("ataque critico")
#         p2v-=ataque

#         print(f" cida de {p2}")
#         print("/"*p2v)
#     else:
#         print("turno de",p2)
#         ataque=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataque*2
#             print("ataque critico ")
#         p2v-=ataque

#         print(f" cida de {p1}")
#         print("/"*p1v)
# if p1v>p2v:
#     print("ha ganado {p1}")
# else:
#     print("ha ganado {p2}")
