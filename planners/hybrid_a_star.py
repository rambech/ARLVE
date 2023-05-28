from planners import Planner
from planners import SimpleAStar


class HybridAStar(Planner):
    def __init__(self) -> None:
        super().__init__()

        self.a_star = SimpleAStar()
