# if - elif conditions by using comparision operators
a = 2
b = 4
if a < b:
    print(" a less than b")
elif b > a:
    print(" b greater than a")
print("---------------------------------")
a = 2
b = 4
if a == b:
    print("a is equal to b")
elif b > a:
    print("b greater than a")
elif a!=b:
    print(" a not equal to b")
print("-----------------------------------")
a = 6
b = 10
if a >= b:
    print(" a greater than or equal to  b")
elif a <= b:
    print("a less than or equal to  b")

# if - elif conditions by using logical operators
a = 8
b = 10
if a>b and b<a:
    print("True")
elif b > a:
    print("b greater than a")

a = 15
b = 6
if a<b or b<a:
    print("False")
elif a == b:
    print("a is equal to  b")

a = 2
b = 4
if not a == b:
    print("True")
elif a<b:
    print("a lessthan b")

# if - elif  conditions by using identify operators
a = 6
b = 12
if a  is b:
    print("a is b")
elif a is not b:
    print("a is not b")


# if - elif  conditions by using Membership operators

a = 6, 8, 10,5,3
if 1  in  a:
    print("6 in a")
elif 2 not in a:
    print("2 not in a")    

