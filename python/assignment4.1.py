# 1 WAP to calulate x raised to the power n(x^n). Accept the value of x and n from the user.
x = int(input("enter x value"))
n = int(input("enter n value"))
print(f"{x} rasied to {n}  :{x**n}")
# 2 WAP to calulate average of three numbers.accept number from uuser

num1 = int(input("enter the first value"))
num2= int(input("enter the second value"))
num3 = int(input("enter the third value"))
print(f"average of three numbers : {(num1+num2+num3)/3}") 

# 3 Write a python program to convert degree to radian.

degree = 9
pi = 22/7
radian = degree*(pi/180)
print(f"degree to radian {radian}")

# 4 Write a python program to convert  radian to degree.

radian = 2
pi = 22/7
degree =radian*(180/pi)
print(f"radian to degree {degree}")


# 5 Write ab python program to calculate the area of a trapezoid.

base1 = 10
base2  = 20
height = 4
ans = (base1+base2/2)*height
print(f"area of trapezim {ans}")

# 6  Write ab python program to calculate the area of a parallelogram.

base = 50
height = 6
ans = base*height
print(f"area of parallelogram {ans}")

# 7  Write ab python program to calculate surface area and volume of a cylinder.

pi =22/7
r = 4
h =15
ans = (2*pi*r*h)+(2*pi*r*r)
print(f"surface area of cylinder {ans}")


pi =3.14
r= 3
h = 2
ans = pi*r*r*h
print(f"volume of cylinder {ans}")

# 8  Write ab python program to calculate surface area and volume of a sphere.

pi = 3.14
r =4
ans = 4*pi*r*r 
print(f"surface are of sphere {ans}")



pi= 3.14
r = 4
ans = (4/3*pi*r*r*r)
print(f"volume of sphere {ans}")