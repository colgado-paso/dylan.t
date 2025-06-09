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

productos = []
precios = []

while True:
    print("""
Seleccione una opción:
    1.- Agregar producto (nombre del producto y precio)
    2.- Mostrar productos
    3.- Crear boleta
    4.- Salir
""")
    op = input("Opción seleccionada: ")

    match op:
        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                productos.append(nombre)
                precios.append(precio)
                print("El producto se agregó correctamente.")
            except ValueError:
                print("Precio inválido.")
        case "2":
            if productos:
                print("Productos disponibles:")
                for i in range(len(productos)):
                    print(f"{i+1}. {productos[i]} - ${precios[i]}")
            else:
                print("No hay productos en el carrito.")
        case "3":
            if productos:
                print("----- Boleta -----")
                total = 0
                for i in range(len(productos)):
                    print(f"{productos[i]}: ${precios[i]}")
                    total += precios[i]
                print(f"Total a pagar: ${total}")
            else:
                print("No hay productos para generar boleta.")
        case "4":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida.")




            

