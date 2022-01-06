from kgmk.dsa.algebra.vector import Vector2D
from kgmk.dsa.geometry.segment2d import Segment2D


def test():
    v0 = Vector2D(0, 0)
    v1 = Vector2D(5, 4)
    v2 = Vector2D(4, -1)
    v3 = Vector2D(2, 5)
    s0 = Segment2D(v0, v1)
    s1 = Segment2D(v2, v3)
    print(s0.intersect(s1))
    print(s0)


if __name__ == "__main__":
    test()
