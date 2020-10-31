
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance

def run():
    stations = stations_by_distance(build_station_list(),(52.2053,0.1218))

    ret = []

    for i in (stations[:10]+stations[-10:]):
        ret.append((i[0].name,i[0].town,i[1]))

    print(ret[:10])
    print(ret[10:])

if __name__ == '__main__':
    run()
    


