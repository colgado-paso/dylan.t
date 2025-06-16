# # uso y ejemplo de listas

# # una listas cuenta con indices negativos y positivos

# numeros = [2,5,12,8,7.9]

# # # n      0 1  2 3  4
# #  print(numeros[3])

# # for numero in numeros:
# #     print("Numero x 2 =", numero*2)

# nombres = ["felipe","larry","ernesto","moe"]

# print(nombres)

# nombres.append("luthien")

# print(nombres)
#---------------------------------------------------------

# crea un menu 
#
# n = ["dilan","daniel","jonny","charles"]
# a = ["tordecilla","gallardo","bravo","chaplin"]

# c = 0 

# for i in n:
#     print(n[c], a[c])
#     c+=1






# nombres = []
# apellidos = []
# while True:
#     print("""Seleccione una opción:
#     1.- Ingresar un nombre
#     2.- mostrar nombre y apellidos
#     3.- buscar nombre
#     4.- Salir""")
#     op = input("Opción seleccionada: ")
#     match op:
#         case 1:
#              nom= input("ingrese un nombre ")
#              nombres.append(nombres)
#              apellido= input("ingrese su apellido ")
#              apellidos.append(apellidos)
             
#         case 2:
#             c = 0 

#             for i in n:
#                 print(nombres[c], apellidos[c])
#                 c+=1
#         case 3:
#             busca = input("indique el nombre que buscara ")
#             if busca in nombres:
#                 print(F"el nombre {busca} esta en la lista ")
#             else:
#                 print(f"el nombre {busca} no esta en la lista ")
#         case 4:
#             print("saliendo del programa... ")
#             break
#         case _:
#             print("opcion invalida ")
#---------------------------------------------------------------------------------------
# crea una carrito de compra 
# usando listas, while true, match
# seleccione una opcion 
# agregar productos (nombre del producto y precio )
# comprar (sub menu mostrando productos y precio )
# crear boleta 
# salir 

# productos = []
# precios = []

# while True:
#     print("""
# Seleccione una opción:
#     1.- Agregar producto (nombre del producto y precio)
#     2.- Mostrar productos
#     3.- Crear boleta
#     4.- Salir
# """)
#     op = input("Opción seleccionada: ")

#     match op:
#         case "1":
#             nombre = input("Ingrese el nombre del producto: ")
#             try:
#                 precio = float(input("Ingrese el precio del producto: "))
#                 productos.append(nombre)
#                 precios.append(precio)
#                 print("El producto se agregó correctamente.")
#             except ValueError:
#                 print("Precio inválido.")
#         case "2":
#             if productos:
#                 print("Productos disponibles:")
#                 for i in range(len(productos)):
#                     print(f"{i+1}. {productos[i]} - ${precios[i]}")
#             else:
#                 print("No hay productos en el carrito.")
#         case "3":
#             if productos:
#                 print("----- Boleta -----")
#                 total = 0
#                 for i in range(len(productos)):
#                     print(f"{productos[i]}: ${precios[i]}")
#                     total += precios[i]
#                 print(f"Total a pagar: ${total}")
#             else:
#                 print("No hay productos para generar boleta.")
#         case "4":
#             print("Saliendo del programa...")
#             break
#         case _:
#             print("Opción inválida.")
#---------------------------------------------------------------------------------------
# crea un programa de manejo de notas 
#  ingresa nota 
# borrar nota
# mostrar nota 
# sacar promedio, notas mayor y notas menor 
# limpiar todas las notas 

# notas = []

# while True:
#     print("""
# Seleccione una opción:
#     1.- Ingresar una nota
#     2.- Borrar una nota
#     3.- Mostrar notas
#     4.- Sacar promedio, nota mayor y nota menor
#     5.- Limpiar todas las notas
#     6.- Salir
# """)
#     op = input("Seleccione una opción: ")

#     match op:
#         case 1:
#             try:
#                 nota = float(input("ingrese la nota "))
#                 notas.append(nota)
#                 print("la nota se ha agregado correctamente ")
#             except ValueError:
#                 print("errro, porfavor intente nuevamente ")
#         case 2:
#             if notas:
#                 for n in notas:
#                     print(n)
#                 try:
#                     nota_borrar = float(input("ingrese la nota que desea borrar "))
#                     if nota_borrar in notas:
#                         notas.remove(nota_borrar)
#                         print(f"nota {nota_borrar} borrada ")
#                     else:
#                         print("la nota no esta en la lista ")
#                 except ValueError:
#                     print("nota invalida")
#             else:
#                 print("no hay notas para borrar ")
#         case 3:
#             if notas:
#                 print("nota ingresada ")
#                 for n in notas:
#                     print(n)
#             else:
#                 print("no hay notas ingresadas ")
#         case 4:
#             if notas:
#                 promedio = sum(notas) / len(notas)
#                 mayor = max(notas)
#                 menor = min(notas)
#                 print(f"promedio {promedio} ")
#                 print(f"nota mayor {mayor}")
#                 print(f"nota menor {menor} ")
#             else:
#                 print("no hay notas para calcular ")
#         case 5:
#             notas.clear()
#             print("todas las notas han sido eliminadas ")
#         case 6:
#             print("saliendo del programa ...")
#             break
#         case _:
#             print("opcin invalida ")
#---------------------------------------------------------------------------


entrada = input("Por favor, ingrese un número: ")

try:
    numero = int(entrada)
    if numero in numeros:
        print(f"El número {numero} sí está en la lista.")
    else:
        print(f"El número {numero} no está en la lista.")
except ValueError:
    print("Por favor, ingrese un número válido.")
            





            

