# if - elif - else  conditions by using comparision operators
a = 2
b = 8
if a > b:
    print(" a greater than b")
elif a < b:
    print("a less than b")
else:
    print("True")

x = 9
y =16
if x >= y:
    print("x greater than or equal to  y")
elif x <= y:
    print(" x less than  or equal to  y")
elif x!=y:
    print("x not equal to y")
else:
    print("equal to")


# if - elif - else  conditions by using logical operators        
    
x = 9
y =16
if x >= y and y<=x:
    print("False")
elif x >= y or y>=x:
    print(" x greater than  or equal to  y")
elif x!=y:
    print("x not equal to y")
else:
    print("equal to")


x = 9
y =16
if not y>=x:
    print("True")
elif x >= y or y<=x:
    print(" x greater than  or equal to  y")
elif not x==y:
    print("x not equal to y")
else:
    print("equal to")

# if - elif - else  conditions by using identity operators
a = 6
b = 18
if a is b:
    print("a is b")
elif b is a:
    print("b is a")
else:
    print("a is not b")

c = 18
d = 30
if a is b:
    print("a is b")
elif a is not b:
    print("a is not b")
else:
    print("True")

# if - elif - else  conditions by using Membership operators
a = 6,8,3,7,61
if 5 in a:
    print("5 in a")
elif 11 not in a:
    print("11 not in a")
else:
    print("nothing")

a = 6,8,3,7,61,1,36,56,11
if 100 in a:
    print("100 in a")
elif 11 not in a:
    print("11 not in a")
else:
    print("nothing")

