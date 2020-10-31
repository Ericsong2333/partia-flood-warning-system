from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)
names = [
        'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge', 'Hemingford',
        'Swindon'
    ]
def take_second(elem):
    return elem[1]
Rank = []
for station in stations:
    if station.relative_water_level() != None:
        Rank.append((station.name, station.relative_water_level()))
        #print("Station name and relative water level: {}, {}".format(
            #station.name, station.relative_water_level()))
Rank.sort(key = take_second, reverse=True)
Ranking_N = []
count = 0
N = 10
for station in Rank:
    if count < N:
        Ranking_N.append(Rank[count])
        count += 1
    else:
        break

print(Ranking_N)
