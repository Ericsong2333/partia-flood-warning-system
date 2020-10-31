# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key  # noqa
import math

def hav(theta):
    return math.sin(theta*0.5)**2

def r(theta):
    return math.radians(theta)

def dist(coor1,coor2):
    hav_phi = hav(r(coor1[0]-coor2[0])) + math.cos(r(coor1[0]))*math.cos(r(coor2[0]))*hav(r(coor1[1]-coor2[1]))
    return 2*6371*math.asin(math.sqrt(hav_phi))

def stations_by_distance(stations,p):
    ret = []
    for i in stations:
        c = i.coord
        distance = dist(c,p)
        ret.append((i,distance))
    return sorted_by_key(ret,1)

def rivers_with_station(stations):
    return {stat.river for stat in stations}

def stations_by_river(stations):
    retdict = {}
    for i in rivers_with_station(stations):
        stats = []
        for j in stations:
            if j.river == i:
                stats.append(j)
        retdict[i] = stats
    return retdict
                

from haversine import haversine,Unit

def stations_within_radius(stations, centre, r):
    """This function returns a list of all station (type MonitoringStation),
     within radius r of a geographic coordinate x.
    """
    coordinates_results = []
    for i in stations:
        if haversine(i.coord, centre) < r:
            coordinates_results.append(i.name)

    coordinates_results.sort()

    return coordinates_results


def rivers_by_station_number(stations, N):
    """This fuction determines the N rivers with the greatest number of monitoring stations.
    In the case that there are more rivers with the same number of stations as the N th entry, include these rivers in the list. 
    """
    river_number = []
    for key,value in stations_by_river(stations).items():
        river_number.append((key,len(value)))
    
    river_number_sorted = sorted_by_key(river_number,1,reverse=True)
    river_final = []
    count = 0
    for river in river_number_sorted:
        if count < N:
           river_final.append(river) 
           count += 1
        elif count == N:
            if river[1] == river_final[-1][1]:
                river_final.append(river)
            else:
                break
               

        else:
            break
        
    return river_final
