#N1
def menu_frutas():
    frutas = ["manzana", "platanos", "kiwis","naranja"]
    while True:
        print("""\n --Menu de Frutas 
              1.- ver todas las frutas 
              2.- agregar frutas 
              3.- eliminar fruta 
              4.- salir """)
        op = input("elija una opcion ")

        match op:
            case "1":
                print("frutas",frutas )
            case "2":
                nueva = input("ingrese el nombre de la fruta ")
                frutas.append(nueva)
                print(f"{nueva} agregada ")
            case "3":
                eliminar = input("que fruta desea eliminar? ")
                if eliminar in frutas:
                    frutas.remove(eliminar)
                    print(f"{eliminar} eliminada ")
                else:
                    print("fruta no encontrada ")
            case "4":
                print("saliendo del programa...")
                break
            case _:
                print("opcion invalida...")
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








        
     