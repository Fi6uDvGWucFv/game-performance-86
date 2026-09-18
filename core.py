from typing import Dict, Set, Tuple, Any

class SpatialHashGrid:
    """
    A 2D spatial hash grid to optimize entity proximity and collision queries.
    Reduces neighbor lookup complexity from O(N^2) to near O(1) per entity.
    """
    def __init__(self, cell_size: int = 64):
        self.cell_size = cell_size
        self.grid: Dict[Tuple[int, int], Set[Any]] = {}

    def _get_cell_coords(self, x: float, y: float) -> Tuple[int, int]:
        """Maps continuous 2D float coordinates to discrete integer cell coordinates."""
        return (int(x // self.cell_size), int(y // self.cell_size))

    def clear(self) -> None:
        """Resets the spatial partition index."""
        self.grid.clear()

    def insert(self, entity_id: Any, x: float, y: float) -> None:
        """Registers an entity into the grid based on its 2D coordinates."""
        cell = self._get_cell_coords(x, y)
        if cell not in self.grid:
            self.grid[cell] = set()
        self.grid[cell].add(entity_id)

    def query_nearby(self, x: float, y: float, radius: float) -> Set[Any]:
        """Retrieves all entities stored in cells overlapping the query bounding box."""
        nearby_entities: Set[Any] = set()
        
        # Determine minimum and maximum grid indices overlapping the radius boundary
        min_cell_x = int((x - radius) // self.cell_size)
        max_cell_x = int((x + radius) // self.cell_size)
        min_cell_y = int((y - radius) // self.cell_size)
        max_cell_y = int((y + radius) // self.cell_size)

        for cx in range(min_cell_x, max_cell_x + 1):
            for cy in range(min_cell_y, max_cell_y + 1):
                cell = (cx, cy)
                if cell in self.grid:
                    nearby_entities.update(self.grid[cell])
        
        return nearby_entities