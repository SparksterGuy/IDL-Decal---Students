import numpy as np
def finalcountdown():
    "function for the final countdown as written in Python"
    "This function will commense a countdown from 100 to 0, and then ends at 0."
    for i in np.arange(100):
        print 100 - i
