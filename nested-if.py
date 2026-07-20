# nested-if
# using comparision operators
# < , > , <= , >= ,==,!=
a = 2
b = 4
if a < b:
    print(" a less than b")
    if b > a:
        print("b greater than a")

a = 2
b = 4
if a == b:
    print("a less than b")
    if b>a:
        print("b greater than a")

a = 12
b = 14
if a < b:
    print("a less than b ")
    if b<a:
        print("less than")

a = 15
b = 20
if a < b:
    print("a less than b")
    if b < a:
        print(" b less than a")
    else:
        print("true")

a = 2
b = 4
if a == b:
    print("a equal to  b")
    if b>a:
        print("b greater than a")
else:
    print("true")

a = 2
b = 4
if a < b:
    print("a less than b")
    if b>a:
        print("b greater than a")
    elif a!=b:
        print("not equal")

    
# nested-if
# using logical operators
# and, or,not

a = 2
b = 4
if a < b and b < a:
    print("a less than b")
    if b>a or a!=b:
        print("b greater than a")
elif  not a==b:
    print("not equal")

# nested-if
# using identify operators
#is, is not
a = 9
b = 6
if a is not  b:
    print("a is b")
    if b  is  a:
        print("b is a")
        
# nested-if
# using membership operators
#in, not in
a = 9, 8,16,47,56,36,11
if 11 in a:
    print("11 in b")
    if 25  not in  a:
        print("36 not in  a")


