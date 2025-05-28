# def suma ():
#     n1 = int(input("ingrese un numero "))
#     n2 = int(input("ingrese otro numero numero "))
#     print("la suma es ", n1 + n2)

# def resta ():
#         n1 = int(input("ingrese un numero "))
#         n2 = int(input("ingrese otro numero numero "))
#         print("la suma es ", n1 - n2)
   

# def multi ():
#         n1 = int(input("ingrese un numero "))
#         n2 = int(input("ingrese otro numero numero "))
#         print("la suma es ", n1 * n2)
   

# def div ():
#     n1 = int(input("ingrese un numero "))
#     n2 = int(input("ingrese otro numero numero "))
#     try:
#         resultado = n1/n2
#         print("la division es ",resultado)
#     except ZeroDivisionError:
#          print("la division por error no esta permitida ")        
        
    
# #  suma()


# # while True:
    
# #     op = int(input("seleccione una funcion "))
# #     match op:
# #         case 1:
# #             print("opcion 1")
# #         case 2:
# #             print("opcion 2")
# #         case 3:
# #             print("opcion 3")
# #         case 4:
# #             print("saliendo ")
# #             break
# #         case _:
# #             print("opcion no valida")

# def calcu():
#     while True:
#         op = int(input("""seleccione una operacion 
#                     1.- suma
#                     2.- resta 
#                     3.- multi
#                     4.- div
#                     5.- salir
#                     """))
#         match op:
#             case 1:
#                 print("suma ")
#                 suma()
#             case 2:
#                 print("resta ")
#                 resta()
#             case 3:
#                 print("multi ")
#                 multi()
#             case 4:
#                 print("div ")
#                 div()
#             case 5:
#                 print("saliendo ")
#                 break

# calcu()

# deuda = 100000

# def pago():
#     global deuda
#     print("\n--- Pago de Tarjeta de Crédito ---")
#     print(f"Deuda actual: ${deuda}")
#     try:
#         monto = float(input("Ingrese el monto a pagar: "))
#         if monto < 0:
#             print("El monto debe ser mayor o igual a cero.")
#             return
#         if monto > deuda:
#             print("El monto no puede exceder la deuda actual.")
#             return
#         deuda -= monto
#         print(f"Pago realizado. Nueva deuda: ${deuda}")
#     except ValueError:
#         print("Por favor, ingrese un valor numérico válido.")

# def compras():
#     global deuda
#     print("\n--- Simulación de Compras ---")
#     while True:
#         try:
#             monto = float(input("Ingrese el monto de la compra (0 para salir): "))
#             if monto == 0:
#                 break
#             if monto < 0:
#                 print("El monto debe ser mayor o igual a cero.")
#                 continue
#             deuda += monto
#             print(f"Compra realizada. Nueva deuda: ${deuda}")
#         except ValueError:
#             print("Por favor, ingrese un valor numérico válido.")

# def menu():
#     while True:
#         print("\n--- Menú ---")
#         print("1. Pago de Tarjeta de Crédito")
#         print("2. Simulación de Compras")
#         print("3. Salir")
#         opcion = input("Seleccione una opción: ")
#         if opcion == "1":
#             pago()
#         elif opcion == "2":
#             compras()
#         elif opcion == "3":
#             print("Saliendo del programa.")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# if __name__ == "__main__":
#     menu()
#---------------------------------------------------------------------------------

# user1 = None
# user2 = None
# user3 = None

# pass1 = None
# pass2 = None
# pass3 = None

# def registrar_usuario():
#     global user1, user2, user3, pass1, pass2, pass3
#     while True:
#         try:
#             nuevo_usuario = input("Ingrese nuevo nombre de usuario: ").strip()
#             nueva_contrasena = input("Ingrese nueva contraseña: ").strip()
#             if not nuevo_usuario or not nueva_contrasena:
#                 print("Usuario y contraseña no pueden estar vacíos.")
#                 continue
#             if user1 is None:
#                 user1, pass1 = nuevo_usuario, nueva_contrasena
#                 print("Usuario registrado exitosamente.")
#                 break
#             elif user2 is None:
#                 user2, pass2 = nuevo_usuario, nueva_contrasena
#                 print("Usuario registrado exitosamente.")
#                 break
#             elif user3 is None:
#                 user3, pass3 = nuevo_usuario, nueva_contrasena
#                 print("Usuario registrado exitosamente.")
#                 break
#             else:
#                 print("Ya existen 3 usuarios registrados.")
#                 break
#         except Exception:
#             print("Error al registrar usuario. Intente nuevamente.")

# def iniciar_sesion():
#     global user1, user2, user3, pass1, pass2, pass3
#     if all(u is None for u in [user1, user2, user3]):
#         print("Debe registrar un usuario antes de iniciar sesión.")
#         return
#     usuario = input("Ingrese su usuario: ").strip()
#     contrasena = input("Ingrese su contraseña: ").strip()
#     if (usuario == user1 and contrasena == pass1) or \
#        (usuario == user2 and contrasena == pass2) or \
#        (usuario == user3 and contrasena == pass3):
#         print("Inicio de sesión exitoso.")
#         menu_usuario()
#     else:
#         print("Usuario o contraseña incorrectos.")

# def menu_usuario():
#     while True:
#         try:
#             print("\n--- Menú de Usuario ---")
#             print("1) Realizar llamada")
#             print("2) Enviar correo electrónico")
#             print("3) Cerrar sesión")
#             opcion = input("Seleccione una opción: ").strip()
#             if opcion == "1":
#                 while True:
#                     numero = input("Ingrese número de celular (9 dígitos, comienza con 9): ").strip()
#                     if len(numero) == 9 and numero.isdigit() and numero[0] == "9":
#                         print(f"Llamando al número {numero}...")
#                         break
#                     else:
#                         print("Número inválido. Debe comenzar con 9 y tener 9 dígitos.")
#             elif opcion == "2":
#                 while True:
#                     correo = input("Ingrese correo electrónico: ").strip()
#                     if "@" in correo:
#                         break
#                     else:
#                         print("Correo inválido. Debe contener '@'.")
#                 mensaje = input("Ingrese el mensaje a enviar: ")
#                 print(f"Correo enviado a {correo} con mensaje: {mensaje}")
#             elif opcion == "3":
#                 print("Cerrando sesión...")
#                 break
#             else:
#                 print("Opción inválida. Intente nuevamente.")
#         except Exception:
#             print("Error. Intente nuevamente.")

# def menu_principal():
#     while True:
#         try:
#             print("\n--- Menú Principal ---")
#             print("1) Iniciar sesión")
#             print("2) Registrar usuario")
#             print("3) Salir")
#             opcion = input("Seleccione una opción: ").strip()
#             if opcion == "1":
#                 iniciar_sesion()
#             elif opcion == "2":
#                 registrar_usuario()
#             elif opcion == "3":
#                 print("Saliendo del programa.")
#                 break
#             else:
#                 print("Opción inválida. Intente nuevamente.")
#         except Exception:
#             print("Error. Intente nuevamente.")

# if __name__ == "__main__":
#     menu_principal()








