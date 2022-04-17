from math import sqrt, floor


def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Calculating distance
    # return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
num7 = float(input())
num8 = float(input())

if distance(num1, num2, num3, num4) >= distance(num5, num6, num7, num8):
    center_point(num1, num2, num3, num4)
else:
    center_point(num5, num6, num7, num8)
