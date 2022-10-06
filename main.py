import signal
import sys

def main():

    while (True):
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exited')
        sys.exit(0)