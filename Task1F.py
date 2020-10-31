import floodsystem.stationdata as stat
import floodsystem.station as station

def run():
    stations = stat.build_station_list()

    #print(stations[:10])

    print(sorted([i.name for i in station.inconsistent_typical_range_stations(stations)]))

if __name__ == '__main__':
    run()