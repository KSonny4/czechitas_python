import sys

vstup = sys.argv

jmeno_souboru = vstup[1]

if jmeno_souboru.endswith(".csv"):
    print(jmeno_souboru)
else:
    print("Neumime zpracovat")

    
print("nepotrebuju exit")