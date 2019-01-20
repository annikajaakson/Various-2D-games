from math import isclose


# Find the distance between two points
def length(p1, p2):
    x_len = p1[0] - p2[0]
    y_len = p1[1] - p2[1]
    return (x_len ** 2 + y_len ** 2) ** 0.5


# Find the area of a triangle
def area(p1, p2, p3):
    a = length(p1, p2)
    b = length(p2, p3)
    c = length(p3, p1)

    p = (a + b + c) / 2

    return abs(p * (p - a) * (p - b) * (p - c)) ** 0.5


# Find whether a point is inside a triangle or not
def point_inside_triangle(p1, p2, p3, p):
    s = area(p1, p2, p3)
    s1 = area(p1, p2, p)
    s2 = area(p2, p3, p)
    s3 = area(p3, p1, p)

    return isclose(s, s1 + s2 + s3)
