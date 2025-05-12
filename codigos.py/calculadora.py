print("bienvenido a la calculadora")
print(" para salir escriba salir")
print("las operaciones que se ocuparan son suma,resta,multi,div")

resultado=""
while True:
    if not resultado:
        resultado= input("ingrese numer: ")
        if resultado.lower() == "salir":
            break
        resultado = input(resultado)
    op = input("ingrse operacion: ")
    if op.lower() == "salir":
        break
    n2 = input(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2 
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break

    print(f"el resultado es {resultado} ")