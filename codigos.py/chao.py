
num1 = int(input("ingrese el primer numero "))
num2 = int(input("ingrese el segundo numero "))
intentos = 3
for i in range(num1,num2):
 
import random
 
numaleatorio = random.randint(num1,num2)
while True:
 
numadiv = int(input("ingrese un numero "))
 
if numadiv == numaleatorio:
 
print("felicidades has adivinado el numero al primer intento s ")
 
break
 
elif numadiv < numaleatorio:
 
print(f"el numero es mayor, esta mas cerca de {num2}")
 
elif numadiv > numaleatorio:
 
print(f"el numero es mayor, esta mas cerca de {num2}")
 
else:
 
print(f"el numero es menor, esta mas cerca de {num1}")
intentos -=1
if intentos == 0:
 
print(f"perdiste el numero era {numadiv} ")
else: 
 
