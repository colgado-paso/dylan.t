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
# import random


# numram = random.randint(1, 50)
# print(numram)
# print("Adivine el numero entre 1 y 50")
# intentos = 5

# num = int(input())

# while numram != num:
#     intentos -= 1
#     if intentos == 0:
#         print("se han agotado los intentos")
#         break
#     if num > numram:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     print(f"te quedan {intentos} intentos")
#     num = int(input())

# if intentos == 0:
#     print("Perdiste")
# else:
#     print("SOS UN GENIO, ADIVINASTE EL NUMERO")
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
# ---------------------------------------------------------------
# ejercicio 6
# Crear un cajero automatico
# Tener en cuenta cajas de billetes de 5000(150.000) , 10000(300.000) y 20000(600.000)
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave
# asociar el saldo disponible
# Si la clave es incorrecta, no se podra acceder al cajero

# intentos = 3

# while intentos >0:
#     intentos -= 1
#     color = input("ingrese un color")

#     if color.lower() != "negro":
#         print(" el color no es el requerido ")
#     else:
#         print(" el color es el correcto")
#         break
# ---------------------------------------------------------------------
# ejercicio 7
# la florida 20%, la pintana 30%, puente alto 25%, san joaquin15%
# grupo familiar: 1=>2% 2 a 4 =>3% , 5 o mas =>4%
# preguntar al usuarioa en que comuna vive
# preguntar al usuario con cuantas personas vive ev su hogar
# el arancel actual es de 200.000 por semestre
# basados en las respuestas del usuario y
# la informacion dada , calcular su descuento

# print("ingrese su comuna")
# comuna = int(input("n1= la florida, \n2= la pintana, \n3= puente alto, \n4= san juaquin"))
# print("ingrese su grupo familiar")
# grupo_fam = int(input("grupo familiar"))
# arancel = 200000
# descuento = arancel * 0,2

# if comuna.lower() == "la florida":
#     arancel = descuento * 20
# elif comuna.lower() == "la pintana":
#     arancel = descuento* 30
# elif comuna.lower() == "puente alto":
#     arancel = descuento * 25
# elif comuna.lower() == "san joaquin":
#     arancel = descuento  * 15
# else:
#     print("comuna no valida")
#     exit()
# if grupo_fam == 1:
#     descuento += arancel * 2
# elif grupo_fam >= 2 and grupo_fam <= 4:
#     descuento += 3
# elif grupo_fam >= 5:
#     descuento = 0.04
# else:
#     print("grupo familiar no valido")
#     exit()
# -----------------------------------------------------------------------------------
# print("seleccione la comuna donde usted vive ")

# print("""
#       1.- la florida
#       2.- la pintana
#       3.- puente alto
#       4.- san joaquin
#       """)

# comuna = input(
#     "ingrese el numero de la comuna donde usted vive ").lower().strip()

# if comuna == "1":
#     descuento = 20
# elif comuna == "2":
#     descuento = 30
# elif comuna == "3":
#     descuento = 25
# elif comuna == "4":
#     descuento = 15
# else:
#     print("Ingrese una opcion correcta ")
#     exit()
# try:
#     familia = int(
#         input("¿ cuantas personas viven en su casa incluyendolo a usted ?"))
# except ValueError:
#     print(" ingrese un numero valido")
#     exit()

# if familia == 1:
#     descuento += 2
# elif 2 <= familia <= 4:
#     descuento += 3
# else:
#     descuento += 4

# valor_base = 200000
# descTotal = valor_base * (descuento / 100)
# print(f"su descuento es de ${descTotal}")
# print(f"su arancel es de ${valor_base - descTotal}")


# ----------------------------------------------------------------
# ejercicio 8
# clasificar segun categoria y precio
# catv 1 +200, cat 2 +400, cat 3 +600
# precios : 1000 y menos ;3%, entre entre 1001 y 5000 ;5% , 5001 y mas 6%
# poner lista de 3 productos por categoria, las cat son 1, 2, 3
# agrega los impuestos al precio , segun las cat luwgo
# aplicar descuento al total de la boleta segun el monto
# total = 0
# print("""
#       seleccione una categoria
#       1.- zapatillas
#       2.- poleras
#       3.- pelotas
#       """)
# cat = int(input())

# if cat == 1:
#     print("""
#           1.- zapatilla puma 2500
#           2.- zapatilla nike 3000
#           3.- zpatilla futbol 4000
#           """)
#     op = int(input())
#     if op == 1:
#         total += 2500+200
#     elif op == 2:
#         total += 3000+200
#     elif op == 3:
#         total += 4000+200
# elif cat == 2:
#     print("""
#           1.- polera puma 1500
#           2.- polera nike 2000
#           3.- polera futbol 5000
#           """)
#     op = int(input())
#     if op == 1:
#         total += 1500+400
#     elif op == 2:
#         total += 2000+400
#     elif op == 3:
#         total += 5000+400
# elif cat == 3:
#     print("""
#           1.- pelota puma 5500
#           2.- pelota nike 6000
#           3.- pelota de playa  1000
#           """)
#     op = int(input())
#     if op == 1:
#         total += 5500+600
#     elif op == 2:
#         total += 6000+600
#     elif op == 3:
#         total += 1000+600
# else:
#     print("opcion invalida")

# if total <= 1000:
#     total = total * 0.97
# print(f"su total a pagar es de {total}")
# ---------------------------------------------------------
# codigo ia
# total = 0
# print("""
#       seleccione una categoria 
#       1.- zapatillas
#       2.- poleras
#       3.- pelotas
#       """)

# try:
#     cat = int(input("ingrese el numero de la categoria "))
# except ValueError:
#     print(" debe ingresar un numero valido ")
#     exit()

# if cat == 1:
#     print("""
#           1.- zapatillas puma $2500
#           2.- zapatillas nike $3000
#           3.- zapatillas futbol $4000
#           """)
#     try:
#         op = int(input("seleccione un producto "))
#     except ValueError:
#         print("debe ingresar un numero valido ")
#         exit()

#     if op == 1:
#         total += 2500 + 200
#     elif op == 2:
#         total += 3000 + 200
#     elif op == 3:
#         total += 4000 + 200
#     else:
#         print("opcion invalida ")
#         exit()

# elif cat == 2:
#     print("""
#           1.- polera puma $1500
#           2.- polera nike $2000
#           3.- polera futbol $5000
#           """)
#     try:
#         op = int(input("seleccione un producto "))
#     except ValueError:
#         print("debe ingresar un numero valido ")
#         exit()

#     if op == 1:
#         total += 1500 + 400
#     elif op == 2:
#         total += 2000 + 400
#     elif op == 3:
#         total += 5000 + 400
#     else:
#         print("opcion invalida ")
#         exit()

# elif cat == 3:
#     print("""
#           1.- pelota puma $5500
#           2.- pelota nike $6000
#           3.- pelota de playa $1000
#           """)
#     try:
#         op = int(input("seleccione un producto "))
#     except ValueError:
#         print("debe ingresar un numero valido ")
#         exit()

#     if op == 1:
#         total += 5500 + 600
#     elif op == 2:
#         total += 6000 + 600
#     elif op == 3:
#         total += 1000 + 600
#     else:
#         print("opcion invalida ")
#         exit()
# else:
#     print(" opcion de categoria invalida ")
#     exit()

# if total <= 1000:
#     total = total * 0.97

# print(f" su total a pegar es de ${total}")
#----------------------------------------------------------------------

creditos = 0
nacionalida = int(input("ingrese su nacionalidad: 1. chilena, 2. extranjera:"))
sueldo = int(int("ingrese su sueldo mensual"))
nivel_educacional = int(input("ingrese su nivel edudacional: 1. basico, 2.medio, 3. superior "))

if nacionalida == 1:
    creditos += 300000
elif nacionalida == 2:
    creditos += 0
else:
    print("nacionalidad no valida")
    exit()

if sueldo < 500000:
    creditos += 0
elif sueldo <= 1000000:
    creditos += 300000
elif sueldo <= 1500000:
    creditos += 500000
elif sueldo <= 2000000:
    creditos += 1000000
else:
    creditos += 0
    print("sieldo no valido")
    exit()

if nivel_educacional == 1:
    creditos += 1
elif nivel_educacional == 2:
    creditos += 1.3
elif nivel_educacional == 3:
    creditos += 1.5
else:
    print("nivel educacional no valido ")
    exit()

print(f"su puntajes de creditos es de {creditos}")



