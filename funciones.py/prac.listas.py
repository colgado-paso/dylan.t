#N1
    # def menu_frutas():
    #     frutas = ["manzana", "platanos", "kiwis","naranja"]
    #     while True:
    #         print("""\n --Menu de Frutas 
    #               1.- ver todas las frutas 
    #               2.- agregar frutas 
    #               3.- eliminar fruta 
    #               4.- salir """)
    #         op = input("elija una opcion ")

    #         match op:
    #             case "1":
    #                 print("frutas",frutas )
    #             case "2":
    #                 nueva = input("ingrese el nombre de la fruta ")
    #                 frutas.append(nueva)
    #                 print(f"{nueva} agregada ")
    #             case "3":
    #                 eliminar = input("que fruta desea eliminar? ")
    #                 if eliminar in frutas:
    #                     frutas.remove(eliminar)
    #                     print(f"{eliminar} eliminada ")
    #                 else:
    #                     print("fruta no encontrada ")
    #             case "4":
    #                 print("saliendo del programa...")
    #                 break
    #             case _:
    #                 print("opcion invalida...")
#---------------------------------------------------------------------------------
#N2 sistema educativo 

# def sistema_notas():
#     estudiantes = []

#     while True:
#         print("""\n MENU DEL SISTEMA DE NOTAS 
#               1.- agregar estudiante 
#               2.- ver todos los estudiantes 
#               3.- buscar por nombre 
#               4.- clasificar por caificaciones 
#               5.- salir """)
        
#         op = input("elija una opcion ")

#         match op:
#             case "1":
#                 nombre = input("ingrese el nombre de estudiante ")
#                 try:
#                     nota = float(input("nota (0 a 10 )"))
#                     if 0 <= nota <= 10:
#                         estudiantes.append({"nombre": nombre, "nota": nota })
#                         print("estudiante agregado ")
#                     else:
#                         print("la nota debe estar entre 0 y 10 ")
#                 except ValueError:
#                     print("nota invalida ")
#             case "2":
#                 if estudiantes:
#                     print("\n listas de estudiantes ")
#                     for e in estudiantes:
#                         print(f"{e['nombre']} : {e['nota']}")
#                 else:
#                     print("no hay estudiantes registrados ")
#             case "3":
#                 buscar = input("Nombre del estudiantes ")
#                 encontrado = [e for e in estudiantes if e["nombre"].lower() == buscar.lower() ]
#                 if encontrado:
#                     for e in encontrado:
#                         print(f"{e['nombre']}: {e['nota']}")
#                 else:
#                     print("estudiantes no encontrado ")
#             case "4":
#                 print("\n Clasificacion ")
#                 for e in estudiantes:
#                     match e["nota"]:
#                         case n if n >=9:
#                             categoria = "excelente"
#                         case n if n >=7:
#                             categoria = "bueno"
#                         case n if n >=5:
#                             categoria = "regular"
#                         case _:
#                             categoria = "insuficiente"
#                     print(f"{e['nombre']} - notas: {e['nota']} - {categoria} ")
#             case "5":
#                 print("cerrando el sistema ")
#                 break
#             case _:
#                 print("opcion no reconocida ")


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
#         case "1":
#             try:
#                 nota = float(input("Ingrese la nota: "))
#                 notas.append(nota)
#                 print("Nota agregada correctamente.")
#             except ValueError:
#                 print("Nota inválida.")
#         case "2":
#             if notas:
#                 for n in notas:
#                     print(n)
#                 try:
#                     nota_borrar = float(input("Ingrese la nota a borrar: "))
#                     if nota_borrar in notas:
#                         notas.remove(nota_borrar)
#                         print(f"Nota {nota_borrar} borrada.")
#                     else:
#                         print("La nota no está en la lista.")
#                 except ValueError:
#                     print("Nota inválida.")
#             else:
#                 print("No hay notas para borrar.")
#         case "3":
#             if notas:
#                 print("Notas ingresadas:")
#                 for n in notas:
#                     print(n)
#             else:
#                 print("No hay notas ingresadas.")
#         case "4":
#             if notas:
#                 promedio = sum(notas) / len(notas)
#                 mayor = max(notas)
#                 menor = min(notas)
#                 print(f"Promedio: {promedio}")
#                 print(f"Nota mayor: {mayor}")
#                 print(f"Nota menor: {menor}")
#             else:
#                 print("No hay notas para calcular.")
#         case "5":
#             notas.clear()
#             print("Todas las notas han sido eliminadas.")
#         case "6":
#             print("Saliendo del programa...")
#             break
#         case _:
#             print("Opción inválida.")
#--------------------------------------------------------------------

# agenda = []

# def agregar_contacto():
#     nombre = input("Nombre del contacto: ")
#     telefonos = input("Introduce teléfonos separados por comas: ").split(",")
#     telefonos = [t.strip() for t in telefonos]
#     agenda.append({"nombre": nombre, "telefonos": telefonos})
#     print("Contacto agregado.\n")

# def buscar_contacto():
#     nombre = input("Nombre del contacto a buscar: ")
#     for contacto in agenda:
#         if contacto["nombre"].lower() == nombre.lower():
#             print(f"{contacto['nombre']} - Teléfonos: {', '.join(contacto['telefonos'])}")
#             return
#     print("Contacto no encontrado.")

# def mostrar_agenda():
#     if not agenda:
#         print("Agenda vacía.")
#         return
#     for contacto in agenda:
#         print(f"{contacto['nombre']} - Teléfonos: {', '.join(contacto['telefonos'])}")

# while True:
#     print("\n--- Agenda Telefónica ---")
#     print("1. Agregar contacto")
#     print("2. Buscar contacto")
#     print("3. Mostrar agenda")
#     print("4. Salir")
#     opcion = input("Elige una opción: ")

#     if opcion == "1":
#         agregar_contacto()
#     elif opcion == "2":
#         buscar_contacto()
#     elif opcion == "3":
#         mostrar_agenda()
#     elif opcion == "4":
#         print("Saliendo de la agenda.")
#         break
#     else:
#         print("Opción inválida.")
#------------------------------------------------------------------------------------------

numeros = [1, 3, 7, 8, 9, 5, 4, 6]

entrada = input("porfavor, ingrese un numero ")

try:
    numero = input(entrada)
    if numero in numeros:
        print(f"el numero {numero} si esta en la lista ")
    else:
        print(f"el numero {numero} no se encuentra en la lista")
except ValueError:
    print("error, porvafor ingrese un numero valido ")
    












        
     