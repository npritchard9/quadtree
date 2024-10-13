from typing import List
from bounds import Bounds
from coord import Coord
from levels import Levels
from node import Node


class QuadTree:
    head: Node

    def __init__(self, items):
        head_bounds = Bounds(12, 12, -12, -12)
        head_levels = Levels()
        self.head = Node(head_bounds, head_levels)
        for item in items:
            self.add(item)

    def __repr__(self):
        return "Tree:\n" + "\n".join(self.head.get_all_children([]))

    def add(self, item):
        print(f"Adding {item}")
        self.head.add_item(item)

    def find(self, item) -> bool:
        print(f"Searching for {item}")
        return self.head.find_item(item)
