import json
import click

@click.command()
@click.argument("file", nargs=1)
def main(file):
    with open(file, encoding="utf-8") as input_file:
        content = input_file.read()
    data = json.loads(content)
    clean_notebook(data)
    result = json.dumps(data, ensure_ascii=False, indent=4)
    print(result)

def clean_notebook(data):
    if data["nbformat"] != 4 or data["nbformat_minor"] < 2:
        raise ValueError("bad version of notebook")
    for cell in data["cells"]:
        if "execution_count" in cell:
            cell["execution_count"] = None
        for output in cell.get("outputs", []):
            if "execution_count" in output:
                output["execution_count"] = None

main()
