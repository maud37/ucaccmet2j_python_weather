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
total_monthly_precipitation = []

months = []
for measurement in all_seattle:
    month = (int(measurement["date"].split("-")[1]))
    if month not in months:
        months.append(month)

for month in months:
    month_precipitation = []
    for measurement in all_seattle:
        if (int(measurement["date"].split("-")[1])) == month:
            month_precipitation.append(measurement["value"])
    total_month = sum(month_precipitation)
    total_monthly_precipitation.append(total_month)

year_precipitation_seattle = []
for measurement in all_seattle:
    year_precipitation_seattle.append(measurement["value"])
total_yearly_precipitation_seattle = sum(year_precipitation_seattle)
                                          
# print(total_yearly_precipitation_seattle)

relative_monthly_precipitation = []
for measurement in total_monthly_precipitation:
    relative_per_month = int(measurement) / int(total_yearly_precipitation_seattle)
    relative_monthly_precipitation.append(relative_per_month)
# print(relative_monthly_precipitation)
# print(sum(relative_monthly_precipitation))


# locations = []
# for measurement in measurements:
#     location = (measurement["station"])
#     if location not in locations:
#         locations.append(location)
# print(locations)

# total_yearly_precipation = []
# for location in locations:
#     location_precipation = []
#     for measurement in measurements:
#         if measurement["station"] == location:
#             location_precipation.append(measurement["value"])
#     total_year_location = sum(location_precipation)
#     print(total_year_location)
#     total_yearly_precipation.append(total_year_location)
# print(total_yearly_precipation)

results = {}
results["Seattle"] = {
    "station"                           : "GHCND:US1WAKG0038",
    "state"                             : "WA",
    "total_monthly_precipation"         : total_monthly_precipitation,
    "total_yearly_precipipation"        : total_yearly_precipitation_seattle,
    "relative_monthly_precipitation"    : relative_monthly_precipitation
}

# storing the results in a .json file
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)