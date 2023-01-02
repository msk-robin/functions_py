from math import pi
def circle_area(r):
    area = float(pi*r*r)
    return round(area,3)

def rectangle_area(l, w):
    area = float(l * w)
    return round(area,3)

def triangle_area(b,h):
    area = float((b*h)/2)
    return round (area,3)

# add a helper function for it to work
