import matplotlib.pyplot as plt
import numpy as np

def polyfit(dates, levels, p):
    return np.poly1d(np.polyfit(np.array(dates)-min(dates), levels,p)),min(dates)

