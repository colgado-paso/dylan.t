# siempre esta acompañado de una palabra clave
# por ejemplo {"nombre": "juan"}


# dic = {"nombre ": "ernesto chalan", 
#        "numero ": 937859517,
#        "casado": true
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

# def suma_print():
#     n1 = int(input("ingrese un numero "))
#     n2 = int(input("ingrese otro numero "))
#     print(n1+n2)

# suma_print()

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
# def suma_return():
#         n1 = int(input("ingrese un numero "))
#         n2 = int(input("ingrese otro numero "))
#         return n1+n2

# print(suma_return())
# #----------------------------------------------------------------------------------

# def promedio(x,y,z):
#       return (x+y+z)/3

# if promedio(40, 70, 25) > 40:
#       print("el alumno aprobo ")
# else:
#       print("el alumno reprobo ")

# print(promedio())
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

# lista = [
#       {"nombre":"lapiz", "precio": 20000},

#       {"nombre": "goma", "precio":240000},

#       {"nombre": "estuche", "precio":640000}
# ]

# print(lista)

# # lista.insert(0,{"nombre":"paleta", "precio":14000})

# # print(lista)

# def mostra_art(lista):
#       for n,p in enumerate(lista):
#                       print(n+1, ".- ", p["nombre"], "$", p["precio"])
# def insertar(lista):
#                 nom = input("ingrese el nombre del producto ")
#                 pre = int(input("ingrese el precio "))
#                 lista.insert(0,{"nombre":nom, "precio":pre})
# def actualizar(lista):
#       for n,p in enumerate(lista):  
#             print(n+1, ".- ", p["nombre"], "$", p["precio"])
#             opc = input("seleccion el producto a actualizar: ")
#             print(lista[opc-1])
#             nn = input("ingrese nuevo nombre: ")
#             np = int(input("ingrese nuevo precio: "))
#             lista[opc-1]["nombre"]=nn
#             lista[opc-1]["precio"]=np
#             print("!articulo actualizado¡ ")
# def borrar(lista):
#        for n,p in enumerate(lista):
#                       print(n+1, ".- ", p["nombre"], "$", p["precio"])
#                       opc = input("selccione el producto a borrar: ")
#                       lista.pop(opc-1)
          
       

# def menu(lista):
#       while True:
#             print("""f
#                   1.- agregar producto
#                   2.- mostrar producto
#                   3.- actualizar producto
#                   4.- borrar productos 
#                   5.- salir   
#                   """)
#             op = int(input("seleccione un producto "))
#             match op:
                  
#                   case 1:
#                         insertar(lista)
                        
#                   case 2:
#                         mostra_art(lista)
#                   case 3:
#                               actualizar(lista)
#                   case 4:
#                         borrar(lista)
#                   case 5:
                        
#                         break
#                   case _:
#                         print("opcion invalida ")   
# print()    
#----------------------------------------------------------------------------------------
# crear programa CRUID del siguente 
# diccionario

personas = {
    1.-"dato1", {"nombre": "dilan tordecilla",
                 "numero": [9194,8871],
                 "estadoCivil": "soltero",
                 "trabajo": True},

    2.-"dato2", {"nombre": "ignacio flores",
                 "numero": [5566,7788],
                 "estadoCivil": "soltero",
                 "trabajo": True},

    3.-"dato3",{"nombre": "ernesto chalan",
                 "numero": [2233,4455],
                 "estadoCivil": "casado",
                 "trabajo": True},
}



while True:
      try:
        print("""
                  1.- igrese perfil
                  2.- mostrar perfiles
                  3.- borrar perfiles
                  4.- salir""")
        op = input("porfavor, seleccione una opcion ")

        match op:
            case 1:
                  nombre = input("ingrese el nombre: ")
                  numero = int(input("ingrese un numero: "))
                  est = input("estado civil 1.- casado, 2.- soltero: ")
                  if est == 1:
                        estadoCivil = "casado"
                  else:
                        estadoCivil = "soltero"

                  edad = int(input("ingrese la edad"))
                  nextkey = len(personas)
                  personas[nextkey+1]={"nombre": nombre,
                                       "numero": [numero],
                                       "estadoCivil": estadoCivil,
                                       "trabajo": True,
                                       "edad": edad}
            case 2:
                  for persona,val in personas.items():
                        print(personas,val )
            case 3:
                  for persona,val in personas.items():
                        print(personas,val )
                  dell = int(input(" seleccione cual desea borrar"))
                  del personas[dell]
            case 4:
                  break
              case _:
                    print("saliendo del sistema ")
                      
                  
                        
                        
                  
      
                  
      except Exception as e:
            print("el error es ", e)           