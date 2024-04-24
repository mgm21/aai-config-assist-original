import numpy as np

from src.rectangular_cuboid import RectangularCuboid
from src.separating_axis_theorem import apply_separating_axis_theorem


class Checker:
    @staticmethod
    def check_overlaps_between_cuboids(cuboids: list[RectangularCuboid]) -> set[str]:
        """Displays a log of possible overlaps in the cuboids list to the terminal.

        Args:
            cuboids (list[RectangularCuboid]): The RectangularCuboid instances to be visualised.

        Returns:
            (set[str]): Names of the items which have an overlap.
        """
        items_with_overlap = set()

        n = len(cuboids)
        for i in range(n):
            for j in range(i + 1, n):
                item1 = cuboids[i]
                item2 = cuboids[j]
                mtv = apply_separating_axis_theorem(item1, item2)

                # If there is an overlap, add the items in question
                if not np.all(np.isclose(mtv, np.array([0, 0]))):
                    items_with_overlap.add(item1.name)
                    items_with_overlap.add(item2.name)

        return items_with_overlap
