import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)

# 1.
print(f"Lidi celkem: {len(data)}")

# 2.
print("Informace o lidech:")
print(data[0])
print(data[0].keys())
print(data[0].values())

# 3.

# Chroustani
pohlavi = [clovek["gender"] for clovek in data]
print(pohlavi)

females = [x for x in pohlavi if x == "Female"]
print(f"Zen: {len(females)}")

males = [x for x in pohlavi if x == "Male"]
print(f"Muzu: {len(males)}")


# For cyklus
muzi = 0
zeny = 0
jine_pohlavi = 0
for clovek in data:
    pohlavi = clovek["gender"]
    if pohlavi == "Female":
        zeny = zeny + 1
    elif pohlavi == "Male":
        muzi = muzi + 1
    else:
        jine_pohlavi = jine_pohlavi + 1

print(f"muzi {muzi} zeny {zeny} jine_pohlavi {jine_pohlavi}")

stringg = "http://svatky.adresa.info/json?date=" + "0410"



