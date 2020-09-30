
# nove_jmena = [jmeno.upper() for jmeno in jmena]
# print(nove_jmena)

jmena = ['petr', 'pavel', 'jitka', 'jana']

# for jmeno in jmena:
#     # print(jmeno.upper())
#     # print(jmeno[:2])
#     # print(jmeno + "asdas")

#     if jmeno == "jitka":
#         print("JITKA JE VE SEZNAMU")

jmena = ['petr', 'pavel', 'jitka', 'jana']

for jmeno in jmena:
    if jmeno == "jitka" or jmeno == "pavel":
        print("JITKA NEBO PAVEL JE VE SEZNAMU")

cisla = [1,2,3,4,5]

soucet = 0
for cislo in cisla:
  soucet = soucet + cislo

print(soucet)

sum(cisla)