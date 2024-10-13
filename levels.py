class Levels:
    level: int
    max_level: int

    def __init__(self, level: int = 0, max_level: int = 3):
        self.level = level
        self.max_level = max_level

    def __str__(self):
        return f"Level: {self.level}"

    def is_max(self):
        return self.level == self.max_level

    def past_max(self):
        return self.level > self.max_level

    def next(self):
        return self.level + 1
