# 1.WAP to detemine input number is even or odd
num=int(input(f"enter the number : "))
if num % 2==0:
    print("num is even")
else:
    print("num is odd")

# 2.find out if agiven year is a leap year or not

year= 2004
if year % 4==0:
    print("year is leap year")
else:
    print("year is not leap year")

# 3 Writw a program to check if a triangle is valid  or not (input 3 angles of triangle)

a=int(input(f"enter first angle"))
b=int(input(f"enter second angle"))
c=int(input(f"enter third angle"))
sum = a+b+c
if sum==180:
    print("triangle is valid ")
else:
    print("triangle is not valid")

# 4  write  to detemine if seller has made profit or loss. display amount of profit/loss
# input:cost pricw and selling price.
cost_price = float(input(f"enter the costprice"))
selling_price = float(input(f"enter the selling price"))
if selling_price >cost_price:
    print(f"profit {selling_price-cost_price}")
else:
    print(f"loss{cost_price - selling_price}")

# 5.wap  to detemine if the given number is the armstrong number or not (153 is the armstrong number as )
num =153
sum = 0
temp = num
while temp > 0:
       digit = temp % 10
       sum +=digit ** 3
       temp //= 10
if num == sum:
      print(f"{num} armstrong number")
else:
      print(f"{num} is not armstrong number")
# 6 detemine if the input number is positive or negative

num =int(input(f"enter the number"))
if num>0:
    print(f"postivie number {num}")
else:
    print(f"negaive number {num}")

# 7 wap to check if a candidate is eligible for vOTING OR NOT.

age = 20
if age>=18:
    print(f"eligible for voting")
else:
    print(f"eligible for not voting")
# 8 wap to find the largest among 3 number
num1 = 50
num2 = 30
num3 = 89
if num1>num2 and num1>num3:
    print(f"largest number is num1")
elif num2>num1 and num2>num3:
    print(f"largest number is num2")
if num3>num1 and num>2:
    print(f"largest number is num3")
# 9  categorize  the person depending on the height.
#      a.<150 dwaf
#      b.=150 average heighted
#      c.>=165  tall

height = 200
if height<150:
    print("dwaf")
elif height== 150:
    print("average heighted")
if height>=165:
    print("tall")

# 10 Wap to accept cooordinates of a point and detemine in which Quadrant it lies


# 11 wap to check  if the alpabet is vowel or consonant
ch ='a'
if (ch=='a'or ch=='u' or ch=='i' or ch=='o' ):
    print("vowel")
else:
    print("consonant")
#12 accept the month number and print its name and number of days in it.
month =int(input(f"enter the month number"))
match month:
     case 1:
          print("januray and 31 day\n")
     case 2:
          print("february and 28 day\n")
     case 3:
          print("march and 31 day\n")
     case 4:
          print("april  and 30 day\n")
     case 5:
          print("may  and 31 day\n")
     case 6:
          print("june  and 30 day\n")
     case 7:
          print("july  and 31 day\n")
     case 8:
          print("august  and 31 day\n")
     case 9:
          print("september and 30 day\n")
     case 10:
          print("october  and 31 day\n")
     case 11:
          print("november  and 30 day\n")
     case 12:
          print("december  and 31 day\n")
    
# acccept maritial status and print miss or mrs in front of name

# write a menu driven program for following
# - area of  circle
#  -area of  rectangle
#   -area of  triangle
#   -area of  square
num = 3
match num:
      case 1:
         r = 2
         pi =3.14
         ans =pi*r
         print(f"area of circle {ans}")
      case 2:
         l= 30
         b= 40
         ans =l*b
         print(f"area of rectangle {ans}")
      case 3:
         base = 3
         height = 5
         ans =(1/2*base*height)
         print(f"area of triangle {ans}")
      case 4:
         s= 4
         ans =s*s
         print(f"area of square {ans}")
    
