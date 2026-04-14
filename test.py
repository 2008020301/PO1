import json
import matplotlib.pyplot as plt
import pandas as pd
import re

with open("PO1/results.json") as data:
    data = json.load(data) #Laadt de dataset

for n in range(len(data)):
    print(f"{n}. {data[n]['name']}")

while True: #Vraagt de gebruiker om een sport
    try:
        sport = int(input("0-46: "))
        if sport > 46:
            raise ValueError    
        break
    except:
        pass

y = []; g = []; s = []; b = [] #Maakt lijsten met tijden en jaren aan
for i in (data[sport]["games"]):
    try:
        u = i["year"]
        gsb = ["none", "none", "none"]
        for n in range(len(i["results"])):
            gsb[n] = i["results"][n]["result"]
        v, w, x = gsb[0], gsb[1], gsb[2]
    except IndexError:
        print(i)

    y.append(u)
    stringsplit = re.compile(r"\d+").findall
    
    def result_correction(n:str):
        if ",+" in n:
            n = n.split(",+")[0]
        return stringsplit(n)
    
    v = result_correction(str(v))
    w = result_correction(str(w))
    x = result_correction(str(x))

    def string_to_seconds(str):
        conversion = [3600, 60, 1, 0.01]
        seconds = 0
        for i, _ in enumerate(str):
            seconds += int(str[-(i+1)]) * conversion[-(i+1)]
        return seconds

    g.append(string_to_seconds(v))
    s.append(string_to_seconds(w))
    b.append(string_to_seconds(x))


timetable = pd.DataFrame()
timetable = timetable.assign( #Maakt het tabel met pandas aan
    year = y,
    gold = g,
    silver = s,
    bronze = b
)

print(data[sport]["name"])
print(timetable)
