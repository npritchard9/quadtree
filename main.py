from coord import Coord
from quadtree import QuadTree


def main():
    points = [Coord(0, 0), Coord(0, 1), Coord(3, 3), Coord(-3, 4)]

    tree = QuadTree(points)
    print(tree)
    print(f"Found? {tree.find(Coord(-3, 4))}\n")
    print(f"Found? {tree.find(Coord(5, 5))}\n")


if __name__ == "__main__":
    main()
