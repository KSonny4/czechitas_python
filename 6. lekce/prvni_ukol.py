import sys
hodnoty = sys.argv

hodnoty = hodnoty[1:]
print(hodnoty)

cisla = [int(x) for x in hodnoty] 

print(cisla)

if cisla[1] == 0:
    print("Druhe cislo je nula")
    exit()

podil = round(cisla[0]/cisla[1], 3)

print(f"podil {podil}")
