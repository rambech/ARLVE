import signal
import sys
import vehicles

def main():
    
    # Reinforcement learning options 
    rl = False 


    # Vehicle variables
    vehicle = vehicles.Otter


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