import json
import csv

# importing the needed data files
with open("precipitation.json", encoding="utf-8") as file:
    measurements = json.load(file)
with open("stations.csv", encoding="utf-8") as file:
    stations = list(csv.DictReader(file))

# opening a results dictionary
results = {}

for station in stations:
    location = station['Location']
    # making a list of all the data for a station
    all_entries_per_station = []
    count_stations = len(measurements)
    for measurement in measurements:
        if (measurement["station"]) == (station["Station"]):
            all_entries_per_station.append(measurement) 

    # calculate total_monthly_precipation
    # first i made a list containing all the months by number so we can cycle through that in the next step
    #       it repeats for every station but it felt more logically here than at the start of the file
    total_monthly_precipitation = []
    months = []
    for measurement in all_entries_per_station:
        month = (int(measurement["date"].split("-")[1]))
        if month not in months:
            months.append(month)

    for month in months:
        month_precipitation_per_month = [] # name is a bit long but at least it's a bit more clear
        for measurement in all_entries_per_station:
            if (int(measurement["date"].split("-")[1])) == month:
                month_precipitation_per_month.append(measurement["value"])
        total_month = sum(month_precipitation_per_month)
        total_monthly_precipitation.append(total_month)

    # calculating the total yearly preoueopraioe per station
    year_precipitation_station = []
    for measurement in all_entries_per_station:
        year_precipitation_station.append(measurement["value"])
    total_yearly_precipitation_station = sum(year_precipitation_station)

    # calculating the monthly rain relative to the total year downfall                                     
    relative_monthly_precipitation = []
    for measurement in total_monthly_precipitation:
        relative_per_month = int(measurement) / int(total_yearly_precipitation_station)
        relative_monthly_precipitation.append(relative_per_month)
    
    # calculating the relative_yearly_precipitation relative to the other stations
    # first calculate the total values of the ALL the measurements then divede total year through that
    all_values = []
    for measurement in measurements:
        all_values.append(measurement["value"])
    all_precipitation_all_stations = sum(all_values)
   # then divede total year of that station to total year all stations
    relative_yearly_precipitation = int(total_yearly_precipitation_station) / int(all_precipitation_all_stations)

    # putting the calculated results in the results dictionary
    results[location] = {
        "station"                           : station["Station"],
        "state"                             : station["State"],
        "total_monthly_precipitation"         : total_monthly_precipitation,
        "total_yearly_precipitation"        : total_yearly_precipitation_station,
        "relative_monthly_precipitation"    : relative_monthly_precipitation,
        "relative_yearly_precipitation"     : relative_yearly_precipitation
    }
    
# storing the results in a .json file
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)