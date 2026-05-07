import json
import matplotlib.pyplot as plt
import pandas as pd
import re
from quicksort import quick_sort

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
        return n

def user_input(data, i):
    while True: #Vraagt de gebruiker om een sport
        try:
            sport = i
            if sport > 44:
                raise ValueError  
            if 13 < sport <= 38:
                sport += 1
            elif sport > 38:
                sport += 2
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
    return y, sport
    
def result_correction(n:str):
    if ",+" in n:
        n = n.split(",+")[0]
    if ",-" in n:
        n = n.split(",-")[0]
    if "." not in n:
        n = n + ".0"
    stringsplit = re.compile(r"\d+").findall
    return stringsplit(n)
    
def string_to_seconds(string):
    conversion = [3600, 60, 1, 0.01]
    seconds = 0
    for i, _ in enumerate(string):
        print(string)
        if i == 2:
            print(int(str(round(float(f"0.{string[-(i+1)]}"), 2)).split("0.")[1]) * conversion[-(i+1)])
            seconds += int(str(round(float(f"0.{string[-(i+1)]}"), 2)).split("0.")[1]) * conversion[-(i+1)]
        else:
            seconds += int(string[-(i+1)]) * conversion[-(i+1)]
    return seconds

for i in range(44):
    sport_names(data)
    year, sport = user_input(data, i)

    print(sport)
    if sport in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 41]:
        for y in year:
            v = result_correction(str(y[1][0]))
            w = result_correction(str(y[1][1]))
            x = result_correction(str(y[1][2]))

            y[1][0] = string_to_seconds(v)
            y[1][1] = string_to_seconds(w)
            y[1][2] = string_to_seconds(x)
    elif sport in [14, 15, 16, 17, 18, 20, 21, 22, 36, 37, 38, 39, 40, 42, 43, 44]:
        for y in year:
            y[1][0] = float(y[1][0])
            y[1][1] = float(y[1][1])
            y[1][2] = float(y[1][2])

    sorted_data = quick_sort(year)

    years = [data[0] for data in sorted_data]
    gold = []
    silver = []
    bronze = []

    for n in range(len(sorted_data)):
        i = n
        if sorted_data[n][1][0] == 0:
            if i == 0:
                while sorted_data[i+1][1][0] == 0:
                    i += 1
                sorted_data[n][1][0] = sorted_data[i+1][1][0]
            else:
                while sorted_data[i-1][1][0] == 0 and i != 0:
                    i -= 1
                sorted_data[n][1][0] = sorted_data[i-1][1][0]
        if sorted_data[n][1][1] == 0:
            if i == 0:
                while sorted_data[i+1][1][1] == 0:
                    i += 1
                sorted_data[n][1][1] = sorted_data[i+1][1][1]
            else:
                while sorted_data[i-1][1][1] == 0 and i != 0:
                    i -= 1
                sorted_data[n][1][1] = sorted_data[i-1][1][1]
        if sorted_data[n][1][2] == 0:
            if i == 0:
                while sorted_data[i+1][1][2] == 0:
                    i += 1
                sorted_data[n][1][2] = sorted_data[i+1][1][2]
            else:
                while sorted_data[i-1][1][2] == 0 and i != 0:
                    i -= 1
                sorted_data[n][1][2] = sorted_data[i-1][1][2]


        gold.append(sorted_data[n][1][0])
        silver.append(sorted_data[n][1][1])
        bronze.append(sorted_data[n][1][2])


    timetable = pd.DataFrame()
    timetable = timetable.assign( #Maakt het tabel met pandas aan
        year = years,
        gold = gold,
        silver = silver,
        bronze = bronze
    )

    timetable.plot(x="year", y=["gold", "silver", "bronze"], kind="line", marker="o")
    plt.title(data[sport]["name"])
    plt.ylabel("Number of medals")
    plt.show()

    print(timetable)