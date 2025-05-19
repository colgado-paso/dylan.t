# import random
# while True:
#     try:
#         cant=int(input("ingrese un numero de perros "))
#         cuota=3
#         cumple=0

#         for i in range(cant):
#             con=random.randint(0.5)
#             print(f"el perro {i+1} trajo {con} conejos ")
#             if con>=cuota:
#                 print("el perro gana filete ")
#             else:
#                 print("se quedo sin cane de res ")
#         print(f"la cantidad de perros que cumplen la cuota es {cumple}")
#         print(f"la cantidad de perros que no cumplen la cuota es {cant-cumple}")
#         break
#     except Exception:
#         print("solo se aceptan numeros enteros ")

#---------------------------------------------------------------------------------

#quiere pasar el ramo 
#pregunte la cantidad de rojos en rl curso
#indique cuantos talleres hay en el semestre
#por cada taller asistido obtiene 0.3 decimas
#si el alumno tiene mas de 1 punto 
#tiene la bendicion del profe 
#sino no se le puede ayudar 
#ingrese la nota final y sume las decimas acumuladas 
#muestre si aprueba o reprueba 

# import time
# while True:
#     try:
#         cant = int(input("Ingresa la cantidad de rojos en el curso: "))
#         tall = int(input("Ingrese a cuantos de los 4 talleres asistió: "))

#         while tall>4:
#             print("Solo hubieron 4 talleres, ingrese la cantidad correcta")
#             tall = int(input("Ingrese a cuantos de los 4 talleres asistió: "))

#         decimas = 0

#         for i in range(tall):
#             print(f"Has asistido al taller {i+1}, has obtenido 0.3 decimas")
#             time.sleep(1)
#             decimas+=0.3
#         if decimas>=1:
#             print("Usted tiene la bendicion del profesor")
#             nota = float(input("Ingresa la nota que quieres subir: "))
#             resultado = nota+decimas
#             print(f"El total de su nota con las decimas aplicadas es de: {resultado}")
#         else:
#             print("No se le puede ayudar")
#             break

#         if nota>=4:
#             print("Usted Aprobo")
#             break
#         else:
#             print("Usted reprobo")
#             break
#     except Exception:
#         print("Ingrese un dato valido")
#------------------------------------------------------------


# rojos = int(input("diga la cantidad de rojos "))
# talleres=4
# tdecimas=0

# for i in range(rojos):
#     for t in range(talleres):
#         asist=input(f"asistio al taller {t+1} si/no ")
#         if asist.lower()=="si":
#             tdecimas+=0.3
#     if tdecimas>=1:
#         print("TIENE LA BENDICION DEL PROFE ")
#     else:
#         print("NADA MAS QUE HACER ")

#     nf=float(input("ingrese su nota final "))
#     nf+=tdecimas
#     print(f"su nota final es {nf}" )
#     if nf>=4:
#         print("el alumno aprobo ")
#     else:
#         print("el alumno reprobo")
#-----------------------------------------------------------

#lavados de sutos 
#crear un meno para lavar autos 
#1.- cursar pago del lavado 
#2.- ver ventas diarias 
#3.- salir 
#el lavado tiene 3 niveles 
#1.- full 15.000, 2.- standar 10.000, 3.- basico 7.000
#al mostrar las ventas diarias, debe mostrar la 
#cantidad de autos que ahn ingresado y el momto total 
#recaudado tambien debe mostrar el monto a pagar 


# print("bienvenidos al autolavado \n1.- cursar el pago del lavado \n2.- ver ventas diarias \n3.- salir  ")

# while True:
#     op = int(input(""" seleccione el nivel del lavado que quiere para su auto 
#                    1.- full $15000
#                    2.- standar $10000
#                    3.- basico $7000
#                    4.- salir """))
#     match op:
#         case 1:
#             print("usted quiere el nivel full ")


    




    






























































































# #lavados de sutos 
# #crear un meno para lavar autos 
# #1.- cursar pago del lavado 
# #2.- ver ventas diarias 
# #3.- salir 
# #el lavado tiene 3 niveles 
# #1.- full 15.000, 2.- standar 10.000, 3.- basico 7.000
# #al mostrar las ventas diarias, debe mostrar la 
# #cantidad de autos que ahn ingresado y el momto total 
# #recaudado tambien debe mostrar el monto a pagar 

# print("bienvenidos al autolavado \n1.- cursar el pago del lavado \n2.- ver ventas diarias \n3.- salir  ")
# while True:
#     op = int(input(""" seleccione el nivel del lavado que quiere para su auto 
#                    1.- full $15000
#                    2.- standar $10000
#                    3.- basico $7000
#                    4.- salir """))
#     match op:
#         case 1:
#             print("usted quiere el nivel full ")
#         case 2:
#             print("usted quiere el nivel standar ")
#         case 3:
#             print("usted quiere el nivel basico ")
#         case 4:
#             print("saliendo ")
#             break
#         case _:
#             print("opcion no valida ")
#             if op==1:
#                 print("usted quiere el nivel full ")
#         case 2:
#             print("usted quiere el nivel standar ")
#         case 3:
#             print("usted qiere el nivel basico ")
#         case 4:
#             print("saliendo ")
#             break
#         case _:
#             prjint("opcion no valida ")
#             break

