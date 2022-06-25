# Write a Python program that takes the height h and base a of a triangle (where h and a are integers) 
# from the user and calculates its area. Print the text "The area of triangle is {P}" (P is the area of the given triangle) on the screen.

print("The base is: ")
a = int(input())
print("The height is: ")
h = int(input())

area = 1/2 * a * h

print("The area of triangle is " + str(area))