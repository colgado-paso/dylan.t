# siempre esta acompañado de una palabra clave
# por ejemplo {"nombre": "juan"}


# dic = {"nombre ": "ernesto chalan", 
#        "numero ": 937859517,
#        "casado": False
#        }

# print(dic)

# for key, value in dic.items():
#     print(key, value)
#---------------------------------------------------

# persona = {"nombre": "david",
#            "edad": 20,
#            "apellido": "lopez"
#            }

# print(persona["nombre"]+ ["edad"])
#----------------------------------------------------------

def suma_print():
    n1 = int(input("ingrese un numero "))
    n2 = int(input("ingrese otro numero "))
    print(n1+n2)

suma_print()

# def resta(n1,n2):
#     print(n1-n2)

# num1 = int(input("ingrese un numero "))
# num2 = int(input("ingrese otro numero "))

# resta(num1,num2)
#-------------------------------------------------------------

# def calculadora():
#     num1 = int(input("numero 1 ")) 
#     num2 = int(input("numero 2 ")) 

#     operacion = input("introduce una operacion (+ - * /)")

#     match operacion:
#         case "+":
#             res = num1+num2
#         case "-":
#             res = num1-num2
#         case "*":
#             res = num1*num2
#         case "/":
#             res = num1/num2
#         case _:
#             print("Operacion no valida")
#             return

#     print(f"resultado de {num1} {operacion} {num2} = {res}")

# calculadora()
#-----------------------------------------------------------------------
def suma_return():
        n1 = int(input("ingrese un numero "))
        n2 = int(input("ingrese otro numero "))
        return n1+n2

print(suma_return())
#----------------------------------------------------------------------------------

def promedio(x,y,z):
      return (x+y+z)/3

if promedio(40, 70, 25) > 40:
      print("el alumno aprobo ")
else:
      print("el alumno reprobo ")

print(promedio())
#------------------------------------------------------------------------------
# crear un programa para calcular un descuento 
# pedir al usuario el precio, y el descuento 
# aplicar .mostrar los resultados 

# def descuento():
#     precio = float(input("Por favor, ingrese el precio: "))
#     desc = float(input("Ingrese el porcentaje de descuento: "))
#     monto_descuento = precio * (desc / 100)
#     precio_final = precio - monto_descuento
#     print(f"El descuento es: {monto_descuento}")
#     print(f"El precio final es: {precio_final}")

# descuento()

# def calc_desc(precio, desc):
#       return precio*(desc/100)

# p = int(input("ingrese el precio "))
# d = int(input("ingrese el descuento "))

# print("el descuento es de ",calc_desc(p,d))
# print("el descuento a pagar es ", p-calc_desc(p,d))
#-------------------------------------------------------------
# producto = ["zapato"]
# precio = [20000]

list_prod = [
      {"nombre":"zapato", "precio": 20000},
      {"nombre": "pelota", "precio":240000}
]

print(list_prod)

list_prod.insert(0,{"nombre":"paleta", "precio":14000})

print(list_prod)

while True:
    print("""f
          1.- agregar producto
          2.- mostrar producto
          3.- actualizar producto
          4.- salir  
          """)
    op = int(input("seleccione un producto "))
    match op:
          
          case 1:
                nom = input("ingrese el nombre del producto ")
                pre = int(input("ingrese el precio "))
                list_prod.insert(0,{"nombre":nom, "precio":pre})
                
          case 2:
                for p in list_prod:
                      print(p)
                
          case 3:
                for p in enumerate(list_prod):
                      print(n+1, ".- ", p)
                      opc = input("seleccion el producto a actualizar: ")
                      print(list_prod[opc-1])
                      nn = input("ingrese nuevo nombre: ")
                      np = int(input("ingrese nuevo precio: "))
                      list_prod[opc-1]["nombre"]=nn
                      list_prod[opc-1]["precio"]=np
                      print("articulo actualizado ")
          case 4:
                
                break
          case _:
                print("opcion invalida ")       
