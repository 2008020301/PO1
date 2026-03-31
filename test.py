import json
with open("PO1/results.json") as data:
    data = json.load(data)

print(data[1])