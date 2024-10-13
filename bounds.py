from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Bounds:
    max_x: int
    max_y: int
    min_x: int
    min_y: int
    mid_x: int = field(init=False)
    mid_y: int = field(init=False)

    def __post_init__(self):
        self.mid_x = (self.max_x + self.min_x) // 2
        self.mid_y = (self.max_y + self.min_y) // 2


class BoundsKind(Enum):
    OUTOFBOUNDS = "Out"
    INBOUNDS = "In"
    BORDERING = "Border"
