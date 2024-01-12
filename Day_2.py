#Create a program to calculate the area of a circle given its radius

#Variables
radius = int(input("Enter the radius of a circle: "))
CONSTANT_PI = 3.14

#Calculate area
Area = CONSTANT_PI * (radius**2)

print("The area of the circle is:", Area)