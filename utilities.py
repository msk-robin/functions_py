from math import pi
def circle_area(radius):
    area = float(pi*radius*radius)
    return round(area,3)

def rectangle_area(length, width):
    area = float(length * width)
    return round(area,3)

def triangle_area(base,height):
    area = float((base*height)/2)
    return round (area,3)

# add a helper function for it to work
