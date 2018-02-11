import json

def clean_notebook(data):
    if data["nbformat"] != 4 or data["nbformat_minor"] <2:
        raise ValueError("bad version of notebook")


with open("test_data.ipynb", encoding="utf-8") as soubor:
    obsah = soubor.read()
data = json.loads(obsah)
clean_notebook(data)

vysledek = json.dumps(data, ensure_ascii=False, indent=2 )
print(vysledek)
