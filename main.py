a = int(input("Enter side A: ")) # This will be the value of side A
b = int(input("Enter side B: ")) # This will be the value of side B
c = int(input("Enter side C: ")) # This will be the value of side C
d = int(input("Enter side D: ")) # This will be the value of side D
e = int(input("Enter side E: ")) # This will be the value of side E
first = a*b # This will be the value of the first shape
triangle = 0.5*e*(a-c) # This will be the value of the triangle
remainder = (d-(b+e))*(a-c) # This will be the value of the remainder
area = first + triangle + remainder # The formula for area
print("Room Area: " + str(area)) # This will be the output of the area