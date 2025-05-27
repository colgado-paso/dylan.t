# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados

# deuda = 1000000

# while True:
#     while True:
#         try:
#             op = input(""" d
#                     seleccione ina opcion 
#                     1.- pago 
#                     2.- compra 
#                     3.- salir """)
#             break
#         except Exception:
#             print(" solo se aceptan numeros enteros ")

#     match op:
#         case 1:
#             print(f"la deuda actual es {deuda}")
#             pago = int(input("ingrese el monto a pagar "))
#             if pago > 0 and pago <= deuda:
#                 deuda=deuda-pago
#             else:
#                 print(f"el pago no debe ser mayor a 0 y no debe exceder ${deuda}")
#         case 2:
#             print(" comprando ")
#             monto = int(input("ingrese el nombre de la compra "))
#             deuda += monto 
#             print(f"la deuda actual es ${deuda}")
#         case 3:
#             print("saliendo ")
#         case _:
#             print("opcion invalida ")

#---------------------------------------------------------------------------------
# Esta actividad formativa tiene como objetivo resolver actividades propuestas usando el editor
# de texto Visual Studio Code en lenguaje de programación Python. Trabajo individual.
# Descripción de la Actividad:
# los estudiantes deberán formar grupos de trabajos de un mínimo de 2 alumnos y un máximo
# de 3 alumnos.
# ETAPAS:
# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario.
# Instrucciones para el envío de la actividad
# El representante del grupo deberá comprimir los programas y enviar al docente a través de
# Mensajes de AVA, utilizando el siguiente formato para el nombre del archivo:
# NombreApellido.RAR

user1 = None
user2 = None
user3 = None

pass1 = None
pass2 = None
pass3 = None

def registrar_usuario():
    global user1, user2, user3, pass1, pass2, pass3
    while True:
        try:
            nuevo_usuario = input("ingrese un nuevo nombre de usuario ").strip()
            nueva_contraseña = input("ingrese una nueva contraseña ").strip()

            if not nuevo_usuario or not nueva_contraseña:
                print("usuario y contraseña no pueden estar vacios ")
                continue
            if user1 is None:
                user1, pass1 = nuevo_usuario, nueva_contraseña
                print("usuario registrado exitosamente ")
                break
            elif user2 is None:
                user2, pass2 = nuevo_usuario, nueva_contraseña
                print("usuario reagistrado exitosamenete ")
                break
            elif user3 is None:
                user3, pass3 = nuevo_usuario, nueva_contraseña
                print("usuario registrado exitosamente ")
                break
            else:
                print("ya existen 3 usuarios registrados ")
                break
        except Exception:
            print("error al registrar usuarios, intente nuevamente ")

def menu_usuario():
    global user1, user2, user3, pass1, pass2, pass3
    







































































