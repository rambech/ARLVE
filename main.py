import signal
import sys
import vehicles
import numpy as np
from control import Control

def main():
    
    # Reinforcement learning options 
    rl = False 


    # Vehicle variables
    vehicle = vehicles.Otter


    # Initialize control
    x = np.zeros(3,1)
    controller = Control()

    # Simulating options
    Simulating = True

    while Simulating == True:
        if rl == True:

            step = 0


        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exited')
        sys.exit(0)