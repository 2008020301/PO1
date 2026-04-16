import json
import matplotlib.pyplot as plt
import pandas as pd
import re
from bubblesort import bubble_sort

with open("PO1/results.json") as data:
    data = json.load(data) #Laadt de dataset

def sport_names(data):
    names = []
    for n in range(len(data)):
        if n in [14, 39]:
            continue
        names.append(data[n]["name"])

    for n in range(len(names)):
        print(f"{n}. {names[n]}")

def user_input(data):
    while True: #Vraagt de gebruiker om een sport
        try:
            sport = int(input("0-44: "))
            if sport > 44:
                raise ValueError  
            if sport == 14 or sport == 39:
                sport += 1
            break
        except:
            pass
    y = []
    for i in (data[sport]["games"]):
        try:
            u = i["year"]
            gsb = ["none", "none", "none"]
            for n in range(len(i["results"])):
                if n < 3:
                    gsb[n] = i["results"][n]["result"]
            v, w, x = gsb[0], gsb[1], gsb[2]
        except IndexError:
            print(i)

        y.append([u, [v, w, x]])
    return y
    
def result_correction(n:str):
    if ",+" in n:
        n = n.split(",+")[0]
    if "." not in n:
        n = n + ".0"
    stringsplit = re.compile(r"\d+").findall
    return stringsplit(n)
    
def string_to_seconds(str):
    conversion = [3600, 60, 1, 0.01]
    seconds = 0
    for i, _ in enumerate(str):
        seconds += int(str[-(i+1)]) * conversion[-(i+1)]
    return seconds

sport_names(data)
year = user_input(data)    

for y in year:
    v = result_correction(str(y[1][0]))
    w = result_correction(str(y[1][1]))
    x = result_correction(str(y[1][2]))

    y[1][0] = string_to_seconds(v)
    y[1][1] = string_to_seconds(w)
    y[1][2] = string_to_seconds(x)

for y in year:
    print(y)

print(bubble_sort(year))

