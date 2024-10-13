from typing import List, Optional
from bounds import Bounds, BoundsKind
from coord import Coord
from levels import Levels


class Node:
    bounds: Bounds
    levels: Levels
    items: List[Coord]
    children: List["Node"]

    def __init__(self, bounds: Bounds, levels: Levels):
        self.bounds = bounds
        self.levels = levels
        self.items = []
        self.children = []

    def add_item(self, item: Coord):
        match item.in_bounds(self.bounds):
            case BoundsKind.INBOUNDS:
                print("in bounds")
                if self.levels.is_max():
                    print("adding at max level")
                    self.items.append(item)
                else:
                    if not self.children:
                        self.create_children()
                    quadrant = item.find_quadrant(self.bounds)
                    self.children[quadrant].add_item(item)
            case BoundsKind.BORDERING:
                print("bordering")
                if self.levels.is_max():
                    print("adding at max level")
                    self.items.append(item)
                else:
                    if not self.children:
                        self.create_children()
                    quadrant = item.find_quadrant_bordering(self.bounds)
                    self.children[quadrant].add_item(item)
            case BoundsKind.OUTOFBOUNDS:
                print("out of bounds")
                self.items.append(item)
                return

    def find_item(self, item: Coord) -> bool:
        match item.in_bounds(self.bounds):
            case BoundsKind.INBOUNDS:
                print("in bounds")
                if self.levels.is_max():
                    print("searching at max level")
                    return item in self.items
                quadrant = item.find_quadrant(self.bounds)
                return self.children[quadrant].find_item(item)
            case BoundsKind.BORDERING:
                print("bordering")
                if self.levels.is_max():
                    print("searching at max level")
                    return item in self.items
                quadrant = item.find_quadrant_bordering(self.bounds)
                return self.children[quadrant].find_item(item)
            case BoundsKind.OUTOFBOUNDS:
                print("out of bounds")
                return False

    def __repr__(self) -> str:
        items = ", ".join([str(x) for x in self.items])
        return f"level={self.levels.level}\nbounds={self.bounds}\n{items=}\n"

    def get_all_children(self, strings: List[str]) -> List[str]:
        if self.levels.past_max():
            return strings
        if self.items:
            strings.append(repr(self))
        for child in self.children:
            child.get_all_children(strings)
        return strings

    def create_children(self):
        a_bounds = Bounds(
            max_x=self.bounds.max_x,
            max_y=self.bounds.max_y,
            min_x=self.bounds.mid_x,
            min_y=self.bounds.mid_y,
        )
        b_bounds = Bounds(
            max_x=self.bounds.mid_x,
            max_y=self.bounds.max_y,
            min_x=self.bounds.min_x,
            min_y=self.bounds.mid_y,
        )
        c_bounds = Bounds(
            max_x=self.bounds.mid_x,
            max_y=self.bounds.mid_y,
            min_x=self.bounds.min_x,
            min_y=self.bounds.min_y,
        )
        d_bounds = Bounds(
            max_x=self.bounds.max_x,
            max_y=self.bounds.mid_y,
            min_x=self.bounds.mid_x,
            min_y=self.bounds.min_y,
        )
        next_level = Levels(self.levels.next())
        self.children.append(Node(a_bounds, next_level))
        self.children.append(Node(b_bounds, next_level))
        self.children.append(Node(c_bounds, next_level))
        self.children.append(Node(d_bounds, next_level))
