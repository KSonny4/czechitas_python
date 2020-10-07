import requests
import json

response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)
print(f"delka dat {len(data)}")
#print(data)

spatna_data = '[{asdasd}]'
data = json.loads(spatna_data)

poleee = [{"jmeno": "petr", "prijmeni": "kubelka"},
        {"jmeno": "petr", "prijmeni": "kubelka", "vek": "25"},
        {"jmeno": "petr"}]