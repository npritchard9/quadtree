from dataclasses import dataclass
from bounds import Bounds, BoundsKind


@dataclass
class Coord:
    x: int
    y: int

    def in_bounds(self, bounds: Bounds):
        if (
            self.x == bounds.max_x
            or self.x == bounds.min_x
            or self.y == bounds.max_y
            or self.y == bounds.min_y
        ):
            return BoundsKind.BORDERING
        elif (
            self.x > bounds.min_x
            and self.x < bounds.max_x
            and self.y > bounds.min_y
            and self.y < bounds.max_y
        ):
            return BoundsKind.INBOUNDS
        else:
            return BoundsKind.OUTOFBOUNDS

    def find_quadrant(self, bounds: Bounds):
        if self.x > bounds.mid_x and self.x < bounds.max_x and self.y > bounds.mid_y:
            return 0
        elif self.x < bounds.mid_x and self.x > bounds.min_x and self.y > bounds.mid_y:
            return 1
        elif self.x < bounds.mid_x and self.x > bounds.min_x and self.y < bounds.mid_y:
            return 2
        else:
            return 3

    def find_quadrant_bordering(self, bounds: Bounds):
        if self.x == bounds.max_x:
            if self.y >= bounds.mid_y:
                return 0
            else:
                return 3
        elif self.x == bounds.min_x:
            if self.y >= bounds.mid_y:
                return 1
            else:
                return 2
        elif self.y == bounds.max_y:
            if self.x >= bounds.mid_x:
                return 0
            else:
                return 1
        else:
            if self.x >= bounds.mid_x:
                return 3
            else:
                return 2
