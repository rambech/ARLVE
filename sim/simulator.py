import pygame
from planners import Planner


class Simulator:
    '''
    Simulator, this class coordinates the vehicle and the environment.
    it takes in the vehicle and the environment and steps them further along.
    '''

    def __init__(self, manual=False, Planner: Planner = None) -> None:
        self.manual = manual
        self.planner = Planner

        pygame.init()

    def simulate(self) -> None:
        screen = pygame.display.set_mode([500, 500])

        running = True

        while running:
            if self.manual:
                # Based on example from Real Python
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            screen.fill((255, 255, 255))

            pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

            pygame.display.flip()

        pygame.quit()
        print(self.stop_message())

    def stop_message(self, error_code=None) -> str:
        stopped = "-------- Simulation has stopped ------- \n"

        if error_code != None:
            error = f"\n Stopped with error: {str(error_code)}"
            stopped = stopped + error

        return stopped
