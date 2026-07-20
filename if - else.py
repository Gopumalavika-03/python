# if - else conditions by using comparision operators
a = 2
b = 4
if a < b:
    print(" a less than b")
else:
    print(" b greater than a")
print("---------------------------------")
a = 2
b = 4
if a == b:
    print("a is equal to b")
else:
    print("b greater than a")
print("-----------------------------------")
a = 6
b = 10
if a >= b:
    print(" a greater than or equal to  b")
else:
    print("a less than or equal to  b")

# if - else conditions by using logical operators
a = 8
b = 10
if a>b and b<a:
    print("True")
else:
    print("b greater than a")

a = 15
b = 6
if a<b or b<a:
    print("False")
else:
    print("a is equal to  b")

a = 2
b = 4
if not a == b:
    print("True")
else:
    print("a less than b")

# if - else  conditions by using identify operators
a = 6
b = 12
if a  is b:
    print("a is b")
else:
    print("a is not b")


# if - else  conditions by using Membership operators

a = 6, 8, 10,5,3
if 1  in  a:
    print("6 in a")
else:
    print("2 not in a")    

