from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.station import MonitoringStation
"""This is a test for module flood"""

def test_station_level_over_threshold():
    """test for stations_level_over _threshold function"""

    #Create three imaginary stations
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Testing station-1"
    coord = (-2.0,4.0)
    typical_range = (0,1)
    river = "River A"
    town = "Town 1"
    station1 = MonitoringStation(s_id, m_id, label, coord, typical_range,river, town)
    station1.latest_level = None

    s_id = "test-s-id-2"
    m_id = "test-m-id-2"
    label = "Testing station-2"
    coord = (-1.0,3.0)
    typical_range = (0,1)
    river = "River B"
    town = "Town 2"
    station2 = MonitoringStation(s_id, m_id, label, coord, typical_range,river, town)
    station2.latest_level = 1

    s_id = "test-s-id-3"
    m_id = "test-m-id-3"
    label = "Testing station-3"
    coord = (-9.0,8.0)
    typical_range = (0,1)
    river = "River C"
    town = "Town 3"
    station3 = MonitoringStation(s_id, m_id, label, coord, typical_range,river, town)
    station3.latest_level = 2

    stations = [station1, station2, station3]
    highest_stations = stations_highest_rel_level(stations,2)
    print(highest_stations)

    assert len(highest_stations) == 2
    assert highest_stations[0][0] == "Testing station-3"
    assert highest_stations[1][0] == "Testing station-2"

test_station_level_over_threshold()