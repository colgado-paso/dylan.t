import random
import time

hp1 = 80
hp2 = 80


print(" bienvenidos a la batalla de dragones ")
print("-------------------------------------------------")
dragon1 = input("como se llama tu dragon ")
dragon2 = input("como se llama el dragon rival ")
turno = 0

while hp1 > 0 and hp2 > 0:
    if turno % 2 == 0:
        print(f"turno de {dragon1}")
        atk = random.randint(10, 18)
        critico = random.randint(1, 5)
        if critico == 3:
            atk *= 3
            print("has hecho ataque critico ")
        hp2 -= atk
        print(f"el daño de {dragon1} fue de {atk} a {dragon2}")
        print(f"vida de {dragon2}: {"|" * (hp2 // 4)}")
    else:
        print(f"turno de {dragon2}")
        atk = random.randint(10, 18)
        critico = random.randint(1, 5)
        if critico == 3:
            atk *= 3
            print("has hecho ataque critico ")
        hp2 -= atk
        print(f"el daño de {dragon2} fue de {atk} a {dragon1}")
        print(f"vida de {dragon1}: {"|" * (hp1 // 4)}")
    turno += 1
    time.sleep(1.5)

print("la pelea ha terminado ")
print("------------------------------------------------")
if hp1 > hp2:
    print(f"ha ganado el {dragon1} ")
else:
    print(f"ha ganado el {dragon2} ")
