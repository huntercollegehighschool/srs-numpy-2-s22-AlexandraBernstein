""" 
Percent Daily Return Exercise

In this exercise, you are given the stock values for several consecutive days for acme corporation. Your job is to calculate the "percent daily return" for each day. The percent daily return is the percentage that the stock changes each compared to the day before.

Note: the percent daily return = 100 * (current day - previous day)/previous day

Below you are given the stock prices (there are only 4 days in this example). First convert to a numpy array. Then use slicing and numeric operations to calculate the percent daily return (no for loops!).
"""

acme = [10, 11.5, 11, 10, 12]
import numpy as np
acme = np.array(acme)
today = acme[1:]  # from index 1 to end
previous = acme[:4]  # start at beginning, go up to but not include index 4
pcd = 100 * (today - previous)/previous  
print(pcd)