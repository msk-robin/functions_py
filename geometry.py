from utilities import rectangle_area , triangle_area , circle_area 

area = 0
 
shape_choice =input("Enter the shape to find its area: \nCircle \nRectangle \nTriangle \n")

if shape_choice.lower() =='circle':
    radius = float(input("Please enter the radius of the needed Circle: "))
    area = circle_area(radius)

elif shape_choice.lower() == 'rectangle':
    length = float(input("Please enter the lenght of the needed rectanglen: "))
    width = float(input("Please enter the width of the needed rectangle: "))
    area = rectangle_area(length,width)

elif shape_choice.lower() == 'triangle':
    height = float(input("Please enter the height of the needed triangle: "))
    base = float(input("Please enter the base of the needed triangle: "))
    area = triangle_area(base,height)

else:
    print(f"Selected shape is not supported {shape_choice} - Please choose an item from the list")

print(f"Calculated area for {shape_choice} is {area}")


#This code needs a helper function to work (visit the utilities file)

