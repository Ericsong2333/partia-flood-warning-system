from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import datetime
import matplotlib.pyplot as plt

def test_plot_water_levels():
    """This is a test for plot_water_levels function"""

    #create one imaginary test station
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Testing station-1"
    coord = (-2.0,4.0)
    typical_range = (0,1)
    river = "River A"
    town = "Town 1"
    station1 = MonitoringStation(s_id, m_id, label, coord, typical_range,river, town)
    station1.latest_level = 0

    dates = [datetime.datetime(2020,2,26,18,0), datetime.datetime(2020,2,27,18,0), datetime.datetime(2020,2,28,18,0)]
    levels = [0, 0.5, 1]
    plot_water_levels(station1, dates, levels)
    lmin, lmax = plt.gca().get_ylim()

    assert int(lmax) == 1
    assert int(lmin) == 0

test_plot_water_levels()

def test_plot_water_level_with_fit():
    """This is a test for test_plot_water_level_with_fit"""
     #create one imaginary station
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Testing station-1"
    coord = (-2.0,4.0)
    typical_range = (0,1)
    river = "River A"
    town = "Town 1"
    station1 = MonitoringStation(s_id, m_id, label, coord, typical_range,river, town)
    station1.latest_level = 0

    dates = [datetime.datetime(2020,2,26,18,0), datetime.datetime(2020,2,27,18,0), datetime.datetime(2020,2,28,18,0)]
    levels = [0, 0.5, 1]
    plot_water_level_with_fit(station1, dates, levels,4)
    lmin, lmax = plt.gca().get_ylim()

    print(plt.gca().get_ylim())

    assert int(lmax) == 1
    assert int(lmin) == 0