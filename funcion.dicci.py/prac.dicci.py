personas = {
    1: {"nombre": "dilan tordecilla",
        "numero": [9194, 8871],
        "estadoCivil": "soltero",
        "trabajo": False},

    2: {"nombre": "ignacio flores",
        "numero": [5566, 7788],
        "estadoCivil": "soltero",
        "trabajo": False},

    3: {"nombre": "ernesto chalan",
        "numero": [2233, 4455],
        "estadoCivil": "casado",
        "trabajo": False},
}

def ingresar():
    idx = max(personas.keys(), default=0) + 1
    nombre = input("Nombre: ")
    numeros = input("Números (separados por coma): ")
    numeros = [int(n.strip()) for n in numeros.split(",")]
    estado = input("Estado civil: ")
    trabajo = input("¿Trabaja? (s/n): ").lower() == "s"
    personas[idx] = {
        "nombre": nombre,
        "numero": numeros,
        "estadoCivil": estado,
        "trabajo": trabajo
    }
    print("Perfil agregado.")

def mostrar():
    for idx, datos in personas.items():
        print(f"ID: {idx}")
        for k, v in datos.items():
            print(f"  {k}: {v}")
        print("-" * 20)

def borrar():
    mostrar()
    idx = int(input("Ingrese el ID del perfil a borrar: "))
    if idx in personas:
        del personas[idx]
        print("Perfil borrado.")
    else:
        print("ID no encontrado.")

def principal():
    while True:
        print("""
1.- Ingresar perfil
2.- Mostrar perfiles
3.- Borrar perfil
4.- Salir
""")
        op = input("Por favor, seleccione una opción: ")
        if op == "1":
            ingresar()
        elif op == "2":
            mostrar()
        elif op == "3":
            borrar()
        elif op == "4":
            print("Saliendo...")
            break
        else:
            print("Selección inválida.")

if __name__ == "__main__":
    principal() 