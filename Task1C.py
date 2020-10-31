from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def run():
    """requirements for Task1C"""

    Cambridge_coordinate = (52.2058,0.1218)

    stations = build_station_list() #build list of stations
    
    print(stations_within_radius(stations, Cambridge_coordinate, 10))






if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()