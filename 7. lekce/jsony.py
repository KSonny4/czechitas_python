import json
hodiny = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8, 'pravda': True}
soubor = open('hodiny.json', 'a', encoding='utf-8')
json.dump(hodiny, soubor)
soubor.close()

hodiny = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
json.dumps(hodiny)