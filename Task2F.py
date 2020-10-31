import datetime
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit 

def run():
    

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    # Find station
    stations_highrisk = stations_highest_rel_level(stations, 5)

    #seperate station
    stations_highrisk_ST = []
    
    for station in stations_highrisk:
        stations_highrisk_ST.append(station[0])

    #retrieve the level history for each station
    dt = 30
    p = 4
    for station in stations:
        if station.name in stations_highrisk_ST:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #print(polyfit(dates,levels,p))
            plot_water_level_with_fit(station, dates, levels,p)

    

if __name__ == "__main__":
    run()