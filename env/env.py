import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from .obstacle import Obstacle


class Env():
    def __init__(self) -> None:
        self.dimensions = []
        self.obstacles = []

    def plot(self) -> None:
        obstacles = self.make_obstacles()

        _, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(0, self.dimensions[0])
        ax.set_ylim(0, self.dimensions[1])
        ax.set_aspect("equal")

        print(f"obstacles[0] {obstacles[0].x}")
        for obstacle in obstacles:
            ax.add_patch(Rectangle((obstacle.x, obstacle.y),
                         obstacle.width, obstacle.height))

        plt.show()

    def make_obstacles(self) -> list:
        obstacles = []
        for obstacle in self.obstacles:
            obstacles.append(
                Obstacle(obstacle[0], obstacle[1], obstacle[2], obstacle[3]))

        return obstacles
