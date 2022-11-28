import numpy as np

class Utils():
    def __init__(self):
        pass

    def Rzyx(self, phi, theta, psi):
        return self.Rz(psi).dot(self.Ry(theta)).dot(self.Rx(phi))

    def Smtrx(self, x):
        """
        Based on Fossen 2001
        https://github.com/cybergalactic/MSS/blob/master/GNC/Smtrx.m
        """
        return np.array([0, -x(3), x(2)],
                        [x(3), 0, -x(1)],
                        [-x(2), x(1), 0])

    def deg2rad(self, deg):
        return deg * np.pi/180

    def rad2deg(self, rad):
        return rad * 180/np.pi

    def Rx(self, phi):
        return np.array([[1, 0, 0],
                         [0, np.cos(phi), -np.sin(phi)],
                         [0, np.sin(phi), np.cos(phi)]])

    def Ry(self, theta):
        return np.array([[np.cos(theta), 0, np.sin(theta)],
                         [0, 1, 0],
                         [-np.sin(theta), 0, np.cos(theta)]])

    def Rz(self, psi):
        return np.array([[np.cos(psi), -np.sin(psi), 0],
                         [np.sin(psi), np.cos(psi), 0],
                         [0, 0, 1]])