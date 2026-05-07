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
    return y, sport
    
def result_correction(n:str):
    if ",+" in n:
        n = n.split(",+")[0]
    if ",-" in n:
        n = n.split(",-")[0]
    stringsplit = re.compile(r"\d+").findall
    return stringsplit(n)


sport_names(data)
year, sport = user_input(data,)
print(sport)
if sport in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 41]:
    year = quick_sort(year)
    gold = [[y[0], result_correction(str(y[1][0]))] for y in year]
    silver = [[y[0], result_correction(str(y[1][1]))] for y in year]
    bronze = [[y[0], result_correction(str(y[1][1]))] for y in year]
    print(gold, silver, bronze)
    
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