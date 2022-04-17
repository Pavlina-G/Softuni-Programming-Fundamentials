from math import floor


def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})")


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
center_point(num1, num2, num3, num4)
