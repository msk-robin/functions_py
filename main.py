#  A fuction that calculates the number of vowels in a password.

# Note functions RETURN values not printing
# to print a funtion return_value use:
#  print(function_name("input"))

# def vowel_counter(password):
#     vowel="aeiouAEIOU"
#     count = 0
#     for i in password:
#         if i in vowel:
#          count+=1
#     return  count
# print(vowel_counter("robinTheRocks"))

# A loop in a function

# def add_up_to(number):
#     total = 0
#     for i in range(1,number):
#         total += number
#     return total

# print(add_up_to(5)) 

# Gread 7th student calculator for Case Study: Geometry Tutor

Rectangle = "1"
Circle = "2"
Triangle ="3"
geometry= [Rectangle,Circle, Triangle]
print("welcome to Geometry !\n")
while True:
    print(f"{Rectangle}.Rectangle")
    print(f"{Circle}.Circle")
    print(f"{Triangle}.Triangle")
    
    choice =input("Select the shape you are working on.\n")

    if choice not in geometry:
        print("Invalid choice!")
        continue
    elif choice == Rectangle:
        length_rectangle = float(input("Enter length :"))
        width_rectangle = float(input("Enter width :"))
        area = length_rectangle * width_rectangle
        print("Area of a rectangle is (A=lw) :",area)
        continue
    
    elif  choice == Circle:
        radius = float(input("Enter radius :"))
        phy = 3.1416
        area_circle= (radius*radius)*phy
        print("Are if a circle :",area_circle)
        continue

    else:

        base = float(input("Enter base of the Triangle :"))
        height =float(input("Enter height of the Triangle :"))
        area_triangle= (base*height)//2
        print("Area of a Triangle is :",area_triangle)
        break
    exit