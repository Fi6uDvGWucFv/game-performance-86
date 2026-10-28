import math
from typing import Dict, List, Tuple

class SpatialHashGrid:
    """Spatial hashing grid for fast 2D spatial queries and collision optimization."""

    def __init__(self, cell_size: float = 64.0):
        self.cell_size = cell_size
        self.grid: Dict[Tuple[int, int], List[Tuple[str, float, float]]] = {}

    def _hash(self, x: float, y: float) -> Tuple[int, int]:
        """Map world coordinates to grid cell indices."""
        return (int(x // self.cell_size), int(y // self.cell_size))

    def clear(self) -> None:
        """Reset the grid bucket storage for a new frame."""
        self.grid.clear()

    def insert(self, entity_id: str, x: float, y: float) -> None:
        """Insert an entity position into the appropriate spatial cell."""
        cell = self._hash(x, y)
        if cell not in self.grid:
            self.grid[cell] = []
        self.grid[cell].append((entity_id, x, y))

    def get_nearby(self, x: float, y: float, radius: float) -> List[str]:
        """Retrieve entity IDs within neighboring cells based on radius query."""
        min_cell = self._hash(x - radius, y - radius)
        max_cell = self._hash(x + radius, y + radius)
        nearby_ids = []
        radius_sq = radius ** 2

        for cx in range(min_cell[0], max_cell[0] + 1):
            for cy in range(min_cell[1], max_cell[1] + 1):
                cell = (cx, cy)
                if cell in self.grid:
                    for entity_id, ex, ey in self.grid[cell]:
                        dist_sq = (x - ex) ** 2 + (y - ey) ** 2
                        if dist_sq <= radius_sq:
                            nearby_ids.append(entity_id)

        return nearby_ids
