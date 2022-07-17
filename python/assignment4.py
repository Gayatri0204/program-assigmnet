# 1 WAP to demonstrate uses of arithmetic operators(numeric as well as str object)
print(f"\n{'='*10}arithmetic Operators{'='*10}")
num1 = 10
num2 = 2
print(f"addition : {num1+num2}")
print(f"subtraction : {num1-num2}")
print(f"multiplication : {num1*num2}")
print(f"division : {num1/num2}")
print(f"modulo: {num1%num2}")
print(f"clearFloor division : {num1//num2}")
print(f" {num1} raised to {num2} : {num1**num2}")

# WAP to demonstrate uses of assigment operators(numeric as well as str object)
print(f"\n{'='*10}assigment Operators{'='*10}")
a=10
print(f"value of a:{a}")
a+=10
print(f"after a+=10:{a}")
a-=10
print(f"after a-=10:{a}")
a*=10
print(f"after a*=10::{a}")
a**=10
print(f"after a**=10::{a}")
a/=10
print(f"after a/-=10::{a}")
a%=10
print(f"after a%-=10::{a}")


# WAP to demonstrate uses of comparison  operators(numeric as well as str object)

print(f"\n{'='*10}comparison Operators{'='*10}")
num1 = 10
num2 = 2
print(f"{num1} > {num2} : {num1>num2}")
print(f"{num1} < {num2} : {num1<num2}")
print(f"{num1} >= {num2} : {num1>=num2}")
print(f"{num1} < {num2} : {num1<=num2}")
print(f"{num1} == {num2} : {num1==num2}")
print(f"{num1} != {num2} : {num1!=num2}")

# WAP to demonstrate uses oflogical operators(numeric as well as str object)

print(f"\n{'='*10}logical Operators{'='*10}")
result = num1 >=19 and num1 <=50
result = num1 >=19 or  num1 <=50
print(f" {num1} >=19 and {num1} <=50: {result}")
print(f" {num1} >=19 or {num1} <=50: {result}")
print(f"  not {num1} >20 : {not num1>20}")