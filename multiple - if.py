# multiple if
#using comparision operators
# < , > ,<= ,>= , == , !=
a = 9
b = 15
if a > b:
    print("a is greater")
if a == b:
    print("a is equal to b")
if a < b:
    print("a less than b")
if a!=b:
    print("a is not equal to b")

a = 2
b = 4
if a >= b:
    print("a is greater")
if a == b:
    print("a is equal to b")
if b >= a:
    print("b greater than a")
if a!=b:
    print("a is not equal to b")

# multiple if
#using logical operators
# and, or, not
x = 10
y = 15
if x>y and y<x:
    print("False")
if x!=y or x<y:
    print("True")
if not y>x:
    print("False")
if not y != 15:
    print("False")

# multiple if
#using identity operators
# is , is not
y = 3
z = 6
if y is z:
    print("y is z")
if y is not z:
    print("y is not z")
if z is y:
    print("z is y")
# multiple if
#using membership operators
# in , not in
y = [13,6,8,4,7,1,62]
if 1 in y :
    print("y is z")
if 13 not in y :
    print("y is not z")
if 8 in y:
    print("z is 6")
