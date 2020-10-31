from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    """requirements for Task1E"""


    stations = build_station_list() #build list of stations
    
    print(rivers_by_station_number(stations,14))






if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()