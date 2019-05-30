from math import sqrt, sin, cos, radians

# ((x1, y1), (x2, y2)) joone formaat
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def point_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def point_generator(angle, hypo_length):
    return hypo_length * sin(radians(angle)), hypo_length * cos(radians(angle))


def equation_generator(point1, point2):
    dif_x_1 = point2[0] - point1[0]
    dif_y_1 = point2[1] - point1[1]
    if dif_x_1 == 0:
        return [0, point1[0]]
    try:
        equation_a = (point2[1] - point1[1]) / (point2[0] - point1[0])
        equation_c = (point2[1] - point1[1]) * point1[0] / (point2[0] - point1[0])
        return [equation_a, equation_c]
    except:
        print(e)
        print(point1)
        print(point2)
    #return [equation_a, equation_c]

def intersection(equation_a_a, equation_a_c, equation_b_a, equation_b_c):
    x = (-equation_a_c + equation_b_c) / (equation_a_a - equation_b_a)
    y = equation_a_a * x + equation_a_c
    return tuple(x, y)


def intersect_check(line, start, intersect):
    if (line[0][0] < intersect[0] and line[1][0] > intersect[0]) or (line[0][0] > intersect[0] and line[1][0] < intersect[0]):
        if (line[0][1] < intersect[1] and line[1][1] > intersect[1]) or (line[0][1] > intersect[1] and line[1][1] < intersect[1]):
            return True, point_distance(start, intersect)