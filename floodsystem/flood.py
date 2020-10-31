#This module contains a collection of functions related to flood data.


def stations_highest_rel_level(stations, N):
    def take_second(elem):
        return elem[1]
    Ranking = []
    for station in stations:
        if station.relative_water_level() != None: #exclude those data with none value in their relative height
             Ranking.append((station.name, station.relative_water_level()))

    Ranking.sort(key = take_second, reverse=True)
    Ranking_N = []
    count = 0
    for station in Ranking:
        if count < N:
            Ranking_N.append(Ranking[count])
            count += 1
        else:
            break
    return Ranking_N

def stations_level_over_threshold(stations, tol):
    list_over_threshold = []
    def take_second(elem):
        return elem[1]
    for station in stations:
        if station.relative_water_level != None: 
            if station.relative_water_level > tol:
                list_over_threshold.append((station.name, station.relative_water_level()))
    list_over_threshold.sort(key = take_second, reverse=True)
    return list_over_threshold
