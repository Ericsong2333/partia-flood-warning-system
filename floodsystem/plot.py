from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib.dates as dat

def plot_water_levels(station, dates, levels):
    """This function will display a plot of the water level data agianst time for a
    station, and include on the plot lines for the typical low and high levels.
    """
    #Plot
    plt.plot(dates, levels)
    plt.plot([min(dates),max(dates)], [station.typical_range[1]]*2, label="$typical high$")
    plt.plot([min(dates),max(dates)], [station.typical_range[0]]*2, label ="$typical low$")

    #Add axis labels, rotate labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    #Display plot
    plt.tight_layout() #This will make sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels,p):
    """This function will display a plot of the water level data agianst time for a
    station, and include on the plot lines for the typical low and high levels.
    """
    #Plot
    plt.plot(dates, levels)

    ndates = dat.date2num(dates)

    t = np.linspace(min(ndates),max(ndates),10000)
    pf = polyfit(ndates,levels,p)

    plt.plot(dat.num2date(t),pf[0](t-pf[1]))

    plt.plot(dat.num2date(dat.date2num([min(dates),max(dates)])), [station.typical_range[1]]*2,label="$typical high$")
    plt.plot(dat.num2date(dat.date2num([min(dates),max(dates)])), [station.typical_range[0]]*2, label ="$typical low$")

    #Add axis labels, rotate labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    #Display plot
    plt.tight_layout() #This will make sure plot does not cut off date labels

    plt.show()

