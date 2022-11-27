import numpy as np
from control import Utils

class Vehicle():
    def __init__(self):
        g = 9.81    # Gravity [m/s^2]
        self.x = np.zeros(6,1)

    def mass_matrix(self, mass, r_bg, I_bb, I_z):
        """
        Based on information from the 2021 book by Fossen:
        Handbook of Marine Craft Hydrodynamics and Motion Control
        """
        # return np.array([mass*np.eye(3), -mass*Utils.Smtrx(r_bg)],
        #                 [mass*Utils.Smtrx(r_bg), I_bb])

        # For simplicity we start of with the 3-DOF version,
        # assuming xz-plane symmetry!
        x_g = r_bg(1)
        return np.array([mass, 0, 0],
                        [0, mass, mass*x_g],
                        [0, mass*x_g, I_z])

    def added_mass(self):
        pass

    def inertia_CO(self):
        pass

    def inertia_CG(self):
        pass