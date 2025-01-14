import json

with open("precipitation.json", encoding="utf-8") as file:
    measurements = json.load(file)


# if (all_stations[]["station"]) == "GHCND:US1WAKG0038":
#     print(all_stations[])

# all_stations[4]["station"]

all_seattle = []
count_stations = len(measurements)
for measurement in measurements:
    if (measurement["station"]) == "GHCND:US1WAKG0038":
        all_seattle.append(measurement) 

# calculate total_monthly_precipation
total_monthly_precipation = []

months = []
for measurement in all_seattle:
    month = (int(measurement["date"].split("-")[1]))
    if month not in months:
        months.append(month)

for month in months:
    month_precipation = []
    for measurement in all_seattle:
        if (int(measurement["date"].split("-")[1])) == month:
            month_precipation.append(measurement["value"])
    total_month = sum(month_precipation)
    print(total_month)
    total_monthly_precipation.append(total_month)
print(total_monthly_precipation)


results = {}
results["Seattle"] = {
    "station"                   :  "GHCND:US1WAKG0038",
    "state"                     :   "WA",
    "total_monthly_precipation" :   total_monthly_precipation
}

# storing the results in a .json file
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)