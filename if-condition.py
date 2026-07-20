# if - condition by using comparision operators
# < , >,<= ,>=,!=,==
a = 10
b = 15
if a<b:
    print("True")
print("------------------------------")
a = 6
b = 9
if a > b:
    print("True")
print("------------------------------")
a = 12
b =14
if a <= b:
    print("True")
print("------------------------------")
a = 10
b= 12
if a>=b:
    print("True")
print("------------------------------")
a = 20
b = 40
if a!=b:
    print("a is not equal to b")
print("------------------------------")
a = 5
b = 5
if a==b:
    print("a is equal to b")
print("------------------------------")
a = 3
if a>5:
    print("a is greaterthan 5")
print("------------------------------")
a = "python"
if a == "python":
    print(" Equal")
print("------------------------------")
a = "python"
if a!= "java":
    print("equal")
print("------------------------------")
a = int(input(" a value:"))
b = int(input("b value"))
if a < b:
        priny("less")
print("------------------------------")
a = int(input(" a value:"))
if a < 40:
        priny("true")
print("------------------------------")
a = input("data")
if a== "python":
        print("true")
print("------------------------------")
# if - condition by using logical operators
# and, or, not

a = 5
b = 7
if a<b and b>a:
    print("true")
print("------------------------------")
a = 9
b = 11
if a<=b and b>=a:
    print("true")
print("------------------------------")
a = 4
b = 6
if a!=b and a==b:
    print("false")
print("------------------------------")
a = 8
b = 12
if a!=b or b == a:
    print("true")
print("------------------------------")
a = 5
b = 9
if not a<b:
    print("less")
print("------------------------------")
a = 11
b = 6
if not a<b and b>a:
    print("True")
print("------------------------------")

# if - condition by using identify  operators
# is , is not

a = 7
if type(a) is int:
    print("It is a int")
print("------------------------------")
a = 9
if type(a) is not int:
    print("false")
print("------------------------------")

a = int(input("a value:"))
if type(a) is int:
    print("true")
print("------------------------------")
b = float(input("Enter b value:"))
if type(b) is float:
    print("It is a float")
print("------------------------------")
c = str(input("Enter a string:"))
if type(c) is str:
    print(" It is a string")
print("------------------------------")
c = str(input("enter a string:"))
if type(c) is not str:
    print("False")
print("------------------------------")
# if - condition by using membership  operators
# in , not in
x = 1,3,5,7,8,10,4
if 3 in x:
    print("True")
print("------------------------------")
y = 1,8,7,2,4,6,3,9,10,15
if 36 in y:
    print("True")
print("------------------------------")
z = 1,56,78,3,4,6,8,10
if 56 not in z:
    print("False")
print("------------------------------")
z = 5,6,8,1,7,36,4
if 11 not in z:
    print("True")
print("------------------------------")
a = int(input("enter a number"))
if 30 in a:
    print("True")#error
print("------------------------------")
b = [1,6,8,7,14,36,9]
c = int(input("enter a number:"))
if c in b:
    print("True")
print("------------------------------")
# if - else condition by using comparision operators
# < , >, <= , >=, !=, ==
a = 11
b = 36
if a<b:
    print("True")
else:
    print("False")
print("------------------------------")
c = 1
d = 3
if c>d:
    print("True")
else:
    print("False")
print("------------------------------")
e = 5
f = 15
if e <= f:
    print("True")
else:
    print("False")
print("------------------------------")
g = 56
h = 36
if g >= h:
    print("True")
else:
    print("False")
print("------------------------------")
i = 5
j = 16
if i!= j:
    print("True")
else:
    print("False")
print("------------------------------")
k = 6
l = 6
if k == l:
    print("True")




    
        
        
    


