from pprint import pprint
absolvent_pole = ['Petr', 'Roman', 2017, 0.95, True]

absolvent = {
  'jmeno': 'Petr',
  'prijmeni': 'Roman',
  'rok': 2017,
  'dochazka': 0.95,
  'vyznamenani': True
}

# print(absolvent)

# print(absolvent['vyznamenani'])


absolventi = [
  {'jmeno': 'Petr', 'prijmeni': 'Roman', 'rok': 2017, 'dochazka': 0.95, 'vyznamenani': True},
  {'jmeno': 'Jana', 'prijmeni': 'Kočanská', 'rok': 2015, 'dochazka': 0.92, 'vyznamenani': True},
  {'jmeno': 'Eva', 'prijmeni': 'Horká', 'rok': 2014, 'dochazka': 0.85, 'vyznamenani': False},
  {'jmeno': 'Ivo', 'prijmeni': 'Roubeník', 'rok': 2017, 'dochazka': 0.75, 'vyznamenani': False}
]

# print(absolventi[-1]["dochazka"])


from statistics import mean

dochazka = mean([absolvent["dochazka"] for absolvent in absolventi])



# print(f"dochazka {dochazka}")


kurz = {
  'nazev': 'Úvod do programování',
  'lektor': 'Martin Podloucký',
  'konani': [
    {
      'misto': 'T-Mobile',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Martina Nemčoková'
      ],
      'ucastnic': 30
    },
    {
      'misto': 'MSD IT',
      'koucove': [
        'Dan Vrátil',
        'Zuzana Tučková',
        'Martina Nemčoková'
      ],
      'ucastnic': 25
    },
    {
      'misto': 'Škoda DigiLab',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Kateřina Kalášková'
      ],
      'ucastnic': 41
    }
  ]
}

# print("==================")
# pprint(kurz['konani'])
# print()
# pprint(kurz['konani'][1])
# print()
# pprint(kurz['konani'][1]['misto'])
# print("==================")

# # print(kurz["konani"][1]["misto"])

# # #konani = [misto for misto in kurz["konani"]]
# # #print(konani)


# keyerror == neexistuje klic

# 1. kurz

print(kurz["konani"])
print(kurz["konani"][-1])
print(kurz["konani"][-1]["ucastnic"])

print()
# 2. kurz
print(kurz["konani"])
print(kurz["konani"][0])
print(kurz["konani"][0]["koucove"])
print(kurz["konani"][0]["koucove"][-1])

print()

# 3. kurz
pocet_konani = len(kurz["konani"])
print(pocet_konani)

print()
# 4. kurz

for k in kurz['konani']:
    print(k['misto']) 


#pprint(kurz["konani"])

mista = [konani["misto"] for konani in kurz["konani"]]

pprint(mista)


# knihovna

knihovna = {
    "pocet_pater" : 3,
    "pocet_knih" : 1312313,
    "oddeleni" : ["naucne", "detske"],
    "otevrena" : True
}