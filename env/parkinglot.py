from env.env import Env

class Parkinglot(Env):
    '''
    Based on code form the course TTK4192 Mission Planning 
    of Autonomous Systems at NTNU

    Contains a map 
    '''

    def __init__(self):
        self.dimensions = [40.2, 22.7]
        self.obstacles = [
            [0, 0, 25.2, 0.1],  # wall1
            [25.1, 0.1, 0.1, 2],
            [25.1, 2, 15.1, 0.1],
            [40.1, 2.1, 0.1, 20.6],
            [0, 22.6, 40.1, 0.1],
            [0, 9.9, 0.1, 12.7],
            [0.1, 9.9, 3.8, 0.1],
            [3.8, 8.1, 0.1, 1.8],
            [0, 8.1, 3.8, 0.1],
            [0, 0.1, 0.1, 8.1],  # wall10
            [2.3, 11.2, 5.7, 6.4],  # room1
            [8.5, 12, 3.6, 6],
            [12.6, 12, 3, 6],
            [16.1, 12, 5.6, 6],  # room4
            [10.95, 3.9, 7.3, 2.8],  # box1
            [20.5, 4.4, 7.3, 2.8],
            [26.1, 14.6, 6, 4],
            [0.1, 0.1, 1, 1],  # wp box 1
            [39.1, 2.1, 1, 1],
            [25.8, 21.6, 1, 1]
        ]
