import datetime
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
import matplotlib.dates as dat


import datetime
dt = 5
p = 1

def run():

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)
    stat_dat = []

    for stat in stations:
        try:
            dates, levels = fetch_measure_levels(stat.measure_id,dt=datetime.timedelta(days=dt))
        except:
            dates = []
        if len(dates) != 0:
            pf = polyfit(dat.date2num(dates),levels,p)
            i = (stat.name, pf[0](max(dat.date2num(dates))+1-pf[1]))
        else:
            i = (stat.name, "No Data")

        stat_dat.append(i)
        if i[1] != "No Data":
            if i[1] > 5:
                print(i[0], "\t\t SEVERE RISK")
            elif i[1] > 2:
                print(i[0], "\t High Risk")
            elif i[1] >0.8:
                print(i[0],"\t Medium Risk")
            else:
                print(i[0],"\t Low Risk")



if __name__ == "__main__":
    run()