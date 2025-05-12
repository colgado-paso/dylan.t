def suma ():
    n1 = int(input("ingrese un numero "))
    n2 = int(input("ingrese otro numero numero "))
    print("la suma es ", n1 + n2)

def resta ():
        n1 = int(input("ingrese un numero "))
        n2 = int(input("ingrese otro numero numero "))
        print("la suma es ", n1 - n2)
   

def multi ():
        n1 = int(input("ingrese un numero "))
        n2 = int(input("ingrese otro numero numero "))
        print("la suma es ", n1 * n2)
   

def div ():
    n1 = int(input("ingrese un numero "))
    n2 = int(input("ingrese otro numero numero "))
    try:
        resultado = n1/n2
        print("la division es ",resultado)
    except ZeroDivisionError:
         print("la division por error no esta permitida ")        
        
    
#  suma()


# while True:
    
#     op = int(input("seleccione una funcion "))
#     match op:
#         case 1:
#             print("opcion 1")
#         case 2:
#             print("opcion 2")
#         case 3:
#             print("opcion 3")
#         case 4:
#             print("saliendo ")
#             break
#         case _:
#             print("opcion no valida")

def calcu():
    while True:
        op = int(input("""seleccione una operacion 
                    1.- suma
                    2.- resta 
                    3.- multi
                    4.- div
                    5.- salir
                    """))
        match op:
            case 1:
                print("suma ")
                suma()
            case 2:
                print("resta ")
                resta()
            case 3:
                print("multi ")
                multi()
            case 4:
                print("div ")
                div()
            case 5:
                print("saliendo ")
                break

calcu()