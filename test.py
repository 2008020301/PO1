import json
import matplotlib.pyplot as plt
from pandas import DataFrame as DF

with open("PO1/results.json") as data:
    data = json.load(data) #Laadt de dataset

names = [(data[i]["name"]) for i in range(len(data))] #Maakt lijst met sporten aan

table = DF(names, columns=["Sports"])
#print(table) #Maakt lijst met namen overzichtelijk bij printen

'''while True:
    try:
        index = int(input("0-46: "))
        if index > 46:
            raise ValueError    
        break
    except:
        pass'''

#years = [(data[index]["games"][i]["year"]) for i in range(len(data[index]["games"]))]
#print(years) #x-as

#first_place = (data[0]["games"][0]["results"][0]["result"]) #laadt eerste plek
#years = (data[0]["games"][0]["year"])

#x, y = years, first_place
#print(x, y)

for i in (data[0]["games"]):
    print(i)
    break

#print(len(data[0]["games"][0]["results"]))