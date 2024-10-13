from typing import List
from bounds import Bounds
from coord import Coord
from levels import Levels
from node import Node


class QuadTree:
    root: Node

    def __init__(self, items):
        root_bounds = Bounds(12, 12, -12, -12)
        root_levels = Levels()
        self.root = Node(root_bounds, root_levels)
        for item in items:
            self.add(item)

    def __repr__(self):
        return "Tree:\n" + "\n".join(self.root.get_all_children([]))

    def add(self, item):
        print(f"Adding {item}")
        self.root.add_item(item)

    def find(self, item) -> bool:
        print(f"Searching for {item}")
        return self.root.find_item(item)
