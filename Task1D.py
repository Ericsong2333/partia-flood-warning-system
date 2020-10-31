import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()

    rivs = sorted(geo.rivers_with_station(stations))

    print(len(rivs),"\n")

    print(rivs[:10],"\n")

    riv_stats = geo.stations_by_river(stations)

    for i in ["River Aire","River Cam","River Thames"]:
        print(i,sorted([j.name for j in riv_stats[i]]),"\n")


if __name__ == '__main__':
    run()