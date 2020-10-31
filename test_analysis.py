from floodsystem.analysis import polyfit
import numpy as np

def test_polyfit():
    t = [0,1,2,6,3,4]
    t0 = [2,3,4,5,6,5]
    p = polyfit(t,t0,6)
    for i in range(len(t)):
        assert np.isclose(p[0](t[i]),t0[i])

test_polyfit()
