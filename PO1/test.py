import json
import matplotlib.pyplot as plt
import pandas as pd

with open("PO1/results.json") as data:
    data = json.load(data) #Laadt de dataset

while True: #Vraagt de gebruiker om een sport
    try:
        sport = int(input("0-46: "))
        if sport > 46:
            raise ValueError    
        break
    except ValueError:
        pass

y = []; g = []; s = []; b = [] #Maakt lijsten met tijden en jaren aan
for i in (data[sport]["games"]):
    u, v, w, x = i["year"], i["results"][0]["result"], i["results"][1]["result"], i["results"][2]["result"]
    y.append(u); g.append(v); s.append(w); b.append(x)

timetable = pd.DataFrame()
timetable = timetable.assign( #Maakt het tabel met pandas aan
    year = y,
    gold = g,
    silver = s,
    bronze = b
)

print(data[sport]["name"])
print(timetable)
