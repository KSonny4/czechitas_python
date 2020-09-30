# and a or
jmena = ['petr', 'pavel', 'jitka', 'jana', 'jarmila']
for jmeno in jmena:
    if 'a' in jmeno and len(jmeno) > 4:
        print(jmeno)

print("===============")

for jmeno in jmena:
    if 'p' in jmeno or len(jmeno) > 5:
        print(jmeno)

print("===============")

# range
jmena = ['petr', 'pavel', 'jitka', 'jana', 'jarmila']
for jmeno in jmena:
    print(jmeno)

mesice = ["leden", "unor", "brezen"]
for cislo in range(len(jmena)):    
    for mesic in mesice:
        print(f"cislo: {cislo} jmeno: {jmena[cislo]} mesic: {mesic}")


list_listu = [[1,2,3], [4,5,6]]

for prvni_list in list_listu:
    print(prvni_list)
    for prvek in prvni_list:
        print(prvek)






# append

jmena = ['petr', 'pavel', 'jitka', 'jana', 'jarmila']
vsechny_a = [jmeno for jmeno in jmena if 'a' in jmeno]
print(vsechny_a)

seznam = []
for jmeno in jmena:
    if 'a' in jmeno:
        seznam.append(jmeno)
print(seznam)
