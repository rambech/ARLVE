import signal
import sys
import vehicles
import env
import control
import numpy as np


def main():
    
    # # Reinforcement learning options 
    # rl = False 


    # # Vehicle variables
    # vehicle = vehicles.Otter


    # # Initialize control
    # x = np.zeros(3,1)
    # controller = control.Control(vehicle)

    # # Initialize environment
    # environment = env.Ocean()

    # # Simulating options
    # N = 10000           # Number of samples
    # dt = 0.1            # Sample rate

    # for n in N:
    #     if rl == True:
    #         pass

    #     else:
    #         controller.step(dt)

    environment = env.Parkinglot()

    environment.plot


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exited')
        sys.exit(0)