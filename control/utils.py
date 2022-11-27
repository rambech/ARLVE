import numpy as np

class Utils():
    def __init__(self):
        pass

    def Rzyx():
        pass

    def Smtrx(x):
        """
        Based on Fossen 2001
        https://github.com/cybergalactic/MSS/blob/master/GNC/Smtrx.m
        """
        return np.array([0, -x(3), x(2)],
                        [x(3), 0, -x(1)],
                        [-x(2), x(1), 0])
