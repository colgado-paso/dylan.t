# crear un codigo que pida al usuario ingresar su nombre, su edad y su ciudad de residencia
# nombre = input("ingrese su nombre")
# edad = int(input("ingrese su edad"))
# ciudad = input("ingrese su  ciudad de residencia ")
# print(f" hola mi nombre es {nombre}, mi edad es {edad} y vivo en {ciudad}")
# -------------------------------------------------------
# n2 crea u nprograma que pregunte un numero al usuario y muestre si es par o impar
# numero = int(input("ingrese un numero"))

# if numero % 2 == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")
# ---------------------------------------------------------
# n3 haz un programa que imprima los numero del 1 al 10 pero usando for
# for i in range(1, 11):
#     print(i)
# n3.1 haz un programa que imprima los numeros del 1 al 10 pero usando un while
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# -----------------------------------------------------------
# n4
# pedir al usuario que genere un numero random entre 1 y 50
# luego pedir al usuario que adivine el numero
# y mostrar si es correcto o no

# --- Configuración del cajero ---
billetes = {
    20000: 30,  # 600.000
    10000: 30,  # 300.000
    5000: 30    # 150.000
}

# Usuarios registrados
usuarios = {
    "1234": 500000,  # clave : saldo
    "5678": 300000,                             
    "9012": 100000
}

# Función para calcular si el cajero puede entregar el dinero


def puede_entregar(monto):
    for billete in sorted(billetes.keys(), reverse=True):
        cantidad_necesaria = monto // billete
        if cantidad_necesaria > billetes[billete]:
            cantidad_necesaria = billetes[billete]
        monto -= cantidad_necesaria * billete
    return monto == 0

# Función para descontar billetes


def entregar_dinero(monto):
    entrega = {}
    for billete in sorted(billetes.keys(), reverse=True):
        cantidad_necesaria = monto // billete
        if cantidad_necesaria > billetes[billete]:
            cantidad_necesaria = billetes[billete]
        if cantidad_necesaria > 0:
            entrega[billete] = cantidad_necesaria
            billetes[billete] -= cantidad_necesaria
            monto -= cantidad_necesaria * billete
    return entrega


# --- Inicio del programa ---
print("Bienvenido al cajero automático")

clave = input("Ingrese su clave secreta: ")

if clave in usuarios:
    saldo_usuario = usuarios[clave]
    while True:
        print(f"\nSu saldo actual es: {saldo_usuario}")
        monto = int(
            input("Ingrese el monto que desea retirar (0 para salir): "))

        if monto == 0:
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        total_cajero = sum(b * c for b, c in billetes.items())

        if monto > saldo_usuario:
            print("Error: No tiene suficiente saldo.")
        elif monto > total_cajero:
            print("Error: El cajero no tiene suficiente dinero.")
        elif monto % 5000 != 0:
            print("Error: El monto debe ser múltiplo de 5000.")
        elif not puede_entregar(monto):
            print("Error: No se puede entregar el monto con los billetes disponibles.")
        else:
            entrega = entregar_dinero(monto)
            saldo_usuario -= monto
            usuarios[clave] = saldo_usuario  # Actualiza el saldo del usuario

            print("Retire su dinero:")
            for billete, cantidad in entrega.items():
                print(f"{cantidad} billete(s) de ${billete}")

            print("\nSaldo del cajero ahora es:")
            for b, c in billetes.items():
                print(f"${b}: {c} billetes")

else:
    print("Clave incorrecta. Acceso denegado.")
