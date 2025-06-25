# def parImpar():
#     num = int(input("ingrese un numero "))
#     if num % 2 ==0:
#         print("su numero es par ")
#     else:
#         print("su numero es impar ")


# def verEdad():
#     edad = int(input("ingrese su edad "))
#     if edad >= 18:
#         print("usted es mayor de edad ")
#     else:
#         print(" usted es menor de edad ")
#---------------------------------------------------------

# perros={
#     1:{"nombre":"snoppy",
#       "raza":"salchicha",
#       "codigo":"Dphh06"},
#     2:{"nombre":"pepe",
#       "raza":"bull dog",
#       "codigo":"BDil77"}
#       }

# def mostrar_perros(perros):
#     for key, perro in dict.items():
#         print(key, perro)

# def valida_pass(perros):
#     Mayuscula = False
#     Minuscula = False
#     Numero = False
#     for palabra in clave:
#         if palabra.isupper():
#             Mayuscula = True
#         if palabra.islower():
#             Minuscula = True
#         if palabra.isdigit():
#             Numero = True
#     if Mayuscula and Minuscula and Numero and len(clave)==6:
#         print("la clave esta bien escrita: ")
#         return True
#     else:
#         print("la clave esta mal escrita: ")
#         return False
    
# def ingrese_perro(perros):
#     nombre = input("ingrese el nombre de su perro: ")
#     raza = input("ingrese la raza de su perro: ")
#     codigo = input("ingrese el codigo de su perro: ")
#     if valida_pass(codigo):
#         largo = list(dict.key())[-1]
#         dict[largo+1]={"nombre":nombre,
#                        "raza":raza,
#                        "codigo":codigo}
#     else:
#         print("el parametro de la clave no esta correcta ")
#         print("""g
#               el codigo debe tener, una mayuscula, una minuscula, 
#               un numero y un largo exacto de 6""")
        
# def act_perros(perros):
#     mostrar_perros(dict)
#     act=int(input("selecciona el perroa a actualizar: "))
#     while True:
#         print("""f
#               1.- Nombre
#               2.- Raza
#               3.- Codigo
#               4.- Salir""")
#         dato = int(input("ingrese el dato a actualizar: "))
#         match dato:
#             case 1:
#                 n = input("ingrese el nuevo nombre ")
#                 dict[act]["nombre"]=n
#             case 2:
#                 n = input("ingrese la nueva raza ")
#                 dict[act]["raza"]=n
#             case 3:
#                 n = input("ingrese el nuevo codigo ")
#                 if valida_pass(n):
#                     dict["codigo"]=n
#                 else:
#                     print("el parametro del codigo no es correcto ")
#                     print("""
#                          el codigo debe tener, una mayuscula, una minuscula, 
#                          un numero y un largo exacto de 6 """)
#             case 4:
#                 break
#             case _:
#                 print("opcion invalida")

# def borrar_perros(perros):
#     mostrar_perros(dict)
#     borrar = int(input("selecciona el perro a borrar "))
#     del dict[borrar]

# while True:
    # try:
    #     print("""f
    #           1.- Registra un perro 
    #           2.- Mostrar un perro 
    #           3.- Actualizar perro 
    #           4.- Borrar perro 
    #           5.- Salir """)
    #     op = int(input("por favor seleccion eun aopcion: "))
    #     match op:
    #         case 1:
    #             ingrese_perro(perros)
    #         case 2:
    #             mostrar_perros(perros)
    #         case 3:
    #             act_perros(perros)
    #         case 4:
    #             borrar_perros(perros)
    #         case 5:
    #             print("saliendo..")
    #             break
    #         case _:
    #             print("opcion invalida ")
    # except Exception as e:
    #     print("el error es",e)
#-------------------------------------------------------------------------------

vehiculo = {
    1:{"marca":"jeep",
       "año":"2025",
       "patente":"evch23",
       "tipo":"camioneta"},
    2:{"marca":"suzuki",
       "año":"2020",
       "patente":"eevv11",
       "tipo":"moto"},
     3:{"marca":"chevrolet",
       "año":"2023",
       "patente":"cchh22",
       "tipo":"sub"}
}

def mostrar_vehiculo(dict):
    for key, auto in dict.items():
        print(key, auto)

def validar_pass(clave):
    Mayuscula = False
    Minusculas = False
    Numero = False
    for palabra in clave:
        if palabra.isupper():
            Mayuscula = True
        if palabra.islower():
            Minusculas = True
        if palabra.isdigit():
            Numero = True
    if Mayuscula and Minusculas and Numero and len(clave)==6:
        print("esta bien escrito ")
        return True
    else:
        print("esta mal escrito ")
        return False
    
def ingrese_vehiculo(dict):
    marca = input("ingrese la marca de auto: ")
    año = input("ingrese el año del auto: ")
    patente = input("ingrese la patente del auto: ")
    print("seleccione el tipo del producto ")
    print(" s -sedan")
    print(" c -camioneta")
    print(" m -moto")
    tipo = input("ingrese el tipo (s/c/m): ").lower()
    while tipo not in ["s", "c", "m"]:
        print("tipo invalido. debe ser: \n s \n c \n m \n o")
        tipo = input("ingrese el tipo (s/c/m): ").lower()

    if validar_pass(patente):
        nuevo_id = max(dict.keys(), default=0)+ 1
        dict[nuevo_id] = {
            "marca":marca,
            "año":año,
            "patente":patente,
            "tipo":tipo
        }
    else:
        print("error no cumple con el parametro ")

def actualizar_vehiculo(dict):
    mostrar_vehiculo(dict)
    actualizar = int(input("¿ que vehiculo deseas actualizar? "))
    while True:
        print("""f
              1.- marca 
              2.- año
              3.- patente
              4.- tipo 
              5.- salir
              """)
        
        dato = int(input("¿ que dato quieres actualizar ? "))
        match dato:
            case 1:
                act = input("actualizar marca: ")
                dict[actualizar]["marca"] = act
            case 2:
                

