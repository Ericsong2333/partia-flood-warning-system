from haversine import haversine, Unit
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def test_station_within_radius():
    stations = list()
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053,0.1218), 10)

    assert ("Bin Brook") in x
    assert ("Stapleford") in x
    assert ("Boscadjack") not in x
    assert ("Pemberth") not in x

def test_rivers_by_station_number():
    stations = []
    for station in build_station_list():
        if station.name in ["Bourton Dickler", "Surfleet Sluice", "Gaw Bridge"]:
            stations.append(station)
    test_list = rivers_by_station_number(stations,1)
    assert ("River Dikler",1) in test_list
    assert ("River Glen",1) in test_list
    assert ("River Parrett",1) in test_list


import floodsystem.geo as geo

from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_sbd():  # Testing Stations_by_distance function
    examples = geo.stations_by_distance(stations[:10],(52.2053,0.1218))
    assert examples[0][1] < examples[1][1]
    assert type(examples[0]) == tuple

test_sbd()
