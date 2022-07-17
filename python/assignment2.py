# 1 assign three different values to three different variables and print them.
 

name,Rollno,Percentage  = 'Gayatri  Mankar',34,89.00
print(name)
print(Rollno)
print(Percentage)
 
# 2   Write a program to demonstrate single and multiple assignments of values to a variables
a = 10,20,30
print(a)
# 3 Write a program to swap two variables
x, y = 15, 35
print(f"{x} {y}")
x, y = 15, 35
x,y =y,x
print(f"{x} {y}")

# 4 write program to demonstrate that a single variable can store different type of values at different instance  of a time

a ='string',90,0.8

# 5 write a program to conatenatie two string

name =  'python'
print("welcome to "+name)


# 6 wap to assign different  type of values to one variable at one variable at different instance of and print its type each time
  
a = 'Name',90,9.0,+0j
print(a)

#  7 Write a program to calculate simple interest .Accept values cfrom user.(si = pnr/100) 

P =float(input("enter the principal amount"))
N =float(input("enter the year"))
R =float(input("enter the rate"))
SI = (P*N*R)/100 
print(SI)  


# 8  use type casting to check every possiblity of type casting (int  to other type ,float to other type...)
#     from a table as below to maintanin track (p: possible n: not possible)
#   cast to -      int      float       bool        complex        str
#    int            P         P          p            N             P
#    float          P         P          p            N             P
#    bool           p         P          p            P             P
#   complex         p         P          p            P             p
#     str           P         p          p            P             P

# int to float

print(f"\n{'='*10}int to float{'='*10}")
a = 14
print(f"{a} \t\t {type(a)}")
a =float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# int to bool
print(f"\n{'='*10}int to bool{'='*10}")
a = 14
print(f"{a} \t\t {type(a)}")
a =bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# int to complex
print(f"\n{'='*10}int to complex{'='*10}")
a = 14
print(f"{a} \t\t {type(a)}")
a =complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# int to str
print(f"\n{'='*10}int to str{'='*10}")
a = 14
print(f"{a} \t\t {type(a)}")
a =str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# float to int

print(f"\n{'='*10}float to int{'='*10}")
a = 14.0
print(f"{a} \t\t {type(a)}")
a =int(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")


#  float to float

print(f"\n{'='*10}float to float{'='*10}")
a = 14.0
print(f"{a} \t\t {type(a)}")
a =float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# float to bool

print(f"\n{'='*10}float to bool{'='*10}")
a = 14.0
print(f"{a} \t\t {type(a)}")
a =bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")



#  float to complex

print(f"\n{'='*10}float to complex{'='*10}")
a = 14.0
print(f"{a} \t\t {type(a)}")
a =complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")


# float to  str 

print(f"\n{'='*10}float to str{'='*10}")
a = 14.0
print(f"{a} \t\t {type(a)}")
a =str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")


# bool to int

print(f"\n{'='*10}bool to int{'='*10}")
a =False
print(f"{a} \t\t {type(a)}")
a =int(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# bool to float
print(f"\n{'='*10}bool to float{'='*10}")
a =True
print(f"{a} \t\t {type(a)}")
a =float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# bool to bool
print(f"\n{'='*10}bool to bool{'='*10}")
a =False
print(f"{a} \t\t {type(a)}")
a =bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# bool to complex
print(f"\n{'='*10}bool to complex{'='*10}")
a =False
print(f"{a} \t\t {type(a)}")
a =complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# bool to str
print(f"\n{'='*10}bool to str{'='*10}")
a =True
print(f"{a} \t\t {type(a)}")
a =str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")




# complex to bool
print(f"\n{'='*10}complex to bool{'='*10}")
a =+0j
print(f"{a} \t\t {type(a)}")
a =bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# complex to complex
print(f"\n{'='*10}complex to complex{'='*10}")
a =+0j
print(f"{a} \t\t {type(a)}")
a =complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

# complex to str
print(f"\n{'='*10}complex to str{'='*10}")
a =+0j
print(f"{a} \t\t {type(a)}")
a =str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")




# str to int
print(f"\n{'='*10}str to int{'='*10}")
a ='10'
print(f"{a} \t\t {type(a)}")
a =int(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")



#  str to float
print(f"\n{'='*10}str to float{'='*10}")
a ='10'
print(f"{a} \t\t {type(a)}")
a =float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")


#  str  to bool
print(f"\n{'='*10}str to bool{'='*10}")
a ='10'
print(f"{a} \t\t {type(a)}")
a =bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#  str to complex
print(f"\n{'='*10}str to complex{'='*10}")
a ='10'
print(f"{a} \t\t {type(a)}")
a =complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#  str to str
print(f"\n{'='*10}str to str{'='*10}")
a ='20'
print(f"{a} \t\t {type(a)}")
a =str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

