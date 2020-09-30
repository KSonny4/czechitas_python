import statistics

soubor = open('hody.txt')
hody = [int(hod) for hod in soubor]
soubor.close()

print(hody)

print(f"hody {len(hody)}")

if len(hody) > 1000:
  print('Nespolehlivý výsledek kvůli nedostatku dat.')
  exit()
else:
  print("Jsme v else, ach jo")
  exit()


print(statistics.mean(hody))