import json
with open("test_data.ipynb", encoding="utf-8") as soubor:
    obsah = soubor.read()
data = json.loads(obsah)


vysledek = json.dumps(data, ensure_ascii=False, indent=2 )
print(vysledek)
