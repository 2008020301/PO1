import json  # Laadt JSON-bestanden in
import matplotlib.pyplot as plt  # Voor het maken van grafieken
import pandas as pd  # Voor tabelstructuren en data-analyse
import re  # Voor regex (tekstverwerking)
from quicksort import quick_sort  # Eigen sorteeralgoritme
from itertools import chain  # Om meerdere lijsten als één te behandelen

with open(".venv/results.json") as data: # Klik met de rechtermuisknop op 'result.json' -> kies: copy relative path. Plak die tussen de haakjes.
    data = json.load(data)  # Laadt de dataset uit JSON bestand

def sport_names(data):
    # DATA: Heel de dataset
    names = []  # Lijst voor sportnamen
    for n in range(len(data)):  # Loop door alle sporten
        if n in [14, 39]:  # Sla bepaalde sporten over
            continue
        names.append(data[n]["name"])  # Voeg sportnaam toe

    for i, name in enumerate(names):  # Print genummerde lijst van sporten
        print(i, name)

def user_input(data):
    # DATA: Heel de dataset
    while True:  # Blijf vragen tot geldige input
        try:
            sport = int(input("0-44: "))  # Vraag gebruiker om sportnummer
            if sport > 44:  # Als buiten bereik
                raise ValueError  
            if sport == 14 or sport == 39:  # Corrigeer ontbrekende indexen
                sport += 1
            break  # Stop loop bij geldige input
        except ValueError:
            pass  # Bij fout opnieuw vragen

    y = []  # Resultatenlijst
    countries = []
    for i in data[sport]["games"]:  # Loop door wedstrijden
        try:
            u = i["year"]  # Jaar van wedstrijd
            gsb = ["none", "none", "none"]  # Placeholder voor gold/silver/bronze

            for n in range(len(i["results"])):  # Loop door resultaten
                if n < 3:  # Alleen top 3
                    gsb[n] = i["results"][n]["result"]  # Vul resultaat in

            v, w, x = gsb[0], gsb[1], gsb[2]  # Splits in 3 variabelen
            countries.append(list([i["results"][n]["nationality"]] for n in range(len(i["results"]))))

        except IndexError:
            print(i)  # Debug bij fout

        y.append([u, [v, w, x]])  # Voeg jaar + resultaten toe
    countries_tally = [{}, {}, {}]

    # Sorteert de landen.
    for result in countries:
        for medal_index, country in enumerate(result):
            country = country[0]
            try:
                if country not in countries_tally[medal_index]:
                    countries_tally[medal_index][country] = 0

                countries_tally[medal_index][country] += 1
            except:
                pass
    for n, res in enumerate(countries_tally):
        print(n+1, res) # Print 1e, 2e, 3e gevolgd met de hoeveelheid elk land gewonnen voor die medailles.

    return y, sport  # Geef data en sport terug
    # OUTPUT:
    # y: [[2016, ['25:05.17', '27:05.64', '27:06.26']], [2008, ['27:01.17', '27:02.77', '27:04.11']],... 
    # sport: user input

def result_correction(n:str):
    if ",+" in n:  # Verwijder extra data na ",+"
        n = n.split(",+")[0]
    if ",-" in n:  # Verwijder extra data na ",-"
        n = n.split(",-")[0]
    stringsplit = re.compile(r"\d+").findall  # Haal alleen cijfers uit string
    return stringsplit(n)  # Return lijst van getallen
    # stringsplit(n) INPUT:
    # '31:20.8'
    # stringsplit(n) OUTPUT:
    # ['31', '20', '8']

def data_conversion(data, conversion):
    # data INPUT:
    # [[1912, ['31', '20', '8']], [1920, ['31', '45', '8']],...
    for i, res in enumerate(data):  # Loop door alle rijen
        data_sec = [int(value) * factor for value, factor in zip(reversed(res[1]), reversed(conversion))][::-1]  # Converteer naar seconden
        decimal = data_sec[-1] / (10 ** len(str(res[1][-1])))  # Bereken decimale waarde
        data[i] = [res[0], sum(data_sec[:-1]) + decimal]  # Zet om naar totaal in seconden
    return data  # Return geconverteerde data
    # data OUTPUT:
    # [[1912, 1880.8], [1920, 1905.8],...

def zero_conversion(data):
    # data INPUT:
    # ...[1904, 11.2], [1908, 0.0], [1912, 10.9],...
    last_value = None  # Laatste bekende waarde
    fallback = next((res[1] for res in data if res[1] != 0), None)  # Eerste niet-0 waarde als fallback

    for res in data:  # Loop door alle waarden
        if res[1] != 0:  # Als waarde geldig is
            last_value = res[1]  # Update laatste waarde
        else:
            res[1] = last_value if last_value is not None else fallback  # Vul 0 in met vorige of fallback

    return data  # Return aangepaste data
    # data OUTPUT:
    # ...[1904, 11.2], [1908, 11.2], [1912, 10.9],...

def prediction(data):
    min_year = data[0][0]
    max_year = data[-1][0]

    weighted_changes = []
    weights = []

    for i in range(1, len(data)):
        previous_year, previous_value = data[i - 1]
        current_year, current_value = data[i]

        # Lineair gewicht van 0 -> 1
        weight = (current_year - min_year) / (max_year - min_year)

        # Verschil tussen resultaten
        change = current_value - previous_value

        weighted_changes.append(change * weight)
        weights.append(weight)

    # Gewogen gemiddelde verandering
    average_change = sum(weighted_changes) / sum(weights)

    # Voorspelling maken
    predicted_value = data[-1][1] + average_change

    # Voeg voorspelling toe aan dataset
    data.append([max_year + 4, predicted_value])

    return data

sport_names(data)  # Toon sportnamen
year, sport = user_input(data)  # Vraag gebruiker input

year = quick_sort(year)  # Sorteer op jaar

if sport in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 41]:
    gold = [[y[0], result_correction(str(y[1][0]))] for y in year]  # Gold resultaten
    silver = [[y[0], result_correction(str(y[1][1]))] for y in year]  # Silver resultaten
    bronze = [[y[0], result_correction(str(y[1][2]))] for y in year]  # Bronze resultaten

    label = "seconds (s)"

    length = max(len(x[1]) for x in chain(gold, silver, bronze))  # Max lengte bepalen

    for result in gold:
        if len(result[1]) < length:
            result[1].extend((length - len(result[1])) * ['00'])  # Padding toevoegen om rekenfouten te voorkomen bij conversie

    for result in silver:
        if len(result[1]) < length:
            result[1].extend((length - len(result[1])) * ['00'])  # Padding toevoegen om rekenfouten te voorkomen bij conversie

    for result in bronze:
        if len(result[1]) < length:
            result[1].extend((length - len(result[1])) * ['00'])  # Padding toevoegen om rekenfouten te voorkomen bij conversie
    
    conversion = [3600, 60, 1, 1]  # Conversiefactoren (uren, minuten, seconden, fractie)

    gold = zero_conversion(data_conversion(gold, conversion))  # Converteer + vul gaten
    silver = zero_conversion(data_conversion(silver, conversion))  # Converteer + vul gaten
    bronze = zero_conversion(data_conversion(bronze, conversion))  # Converteer + vul gaten

elif sport in [14, 15, 16, 17, 18, 20, 21, 22, 36, 37, 38, 39, 40, 42, 43, 44]:  # Sporten waarbij resultaten niet to seconden omgezet hoeven worden
    gold = [[res[0], res[1][0]] for res in year]  # Maak lijst met [jaar, goud-resultaat]
    silver = [[res[0], res[1][1]] for res in year]  # Maak lijst met [jaar, zilver-resultaat]
    bronze = [[res[0], res[1][2]] for res in year]  # Maak lijst met [jaar, brons-resultaat]

    label = "meters (m)"  # Label voor y-as van grafiek


gold = prediction(gold)
silver = prediction(silver)
bronze = prediction(bronze)
years = [y[0] for y in gold]  # Haal jaartallen uit data

timetable = pd.DataFrame()  # Maak lege DataFrame

timetable = timetable.assign(  # Vul DataFrame
    year = years,  # Jaar kolom
    gold = [time[1] for time in gold],  # Gold waarden
    silver = [time[1] for time in silver],  # Silver waarden
    bronze = [time[1] for time in bronze]  # Bronze waarden
)

print(timetable)  # Print tabel

timetable.plot(x="year", y=["gold", "silver", "bronze"], kind="line", marker="o", color=["gold", "silver", "peru"])  # Plot grafiek
plt.title(data[sport]["name"])  # Titel grafiek
plt.ylabel(label)  # Y-as label
plt.show()  # Toon grafiek
