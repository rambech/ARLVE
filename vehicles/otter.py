from vehicle import Vehicle
from control import Utils
import numpy as np


class Otter(Vehicle):
    """
    Based on Thor I. Fossen's implementation of the Otter USV
    in MSS Matlab Toolbox
    https://github.com/cybergalactic/MSS/blob/master/VESSELS/otter.m
    """
    def __init__(self) -> None:
        mass = 63       # kg
        length = 2      # m
        width = 1       # m

        max_speed = 2.5 # m/s

        ly = 0.395
        self.B_config = np.array([1,   1],
                                 [0,   0],
                                 [-ly, ly])

        self.MRB = self.mass_matrix(mass,r_bg, I_bb)


