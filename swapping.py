#swapping

# Method 1 swapping of two variables without using third variable
a = int(input("enter A value:"))
b = int(input("enter B value:"))
a,b=b,a
print("updated A value:",a)
print("updated B value:",b)
print("------------------------------------------------")
#Method 2 swapping of two variables using third variable
x = int(input("enter x value:"))
y = int(input("enter y value:"))
temp = x
x = y
y =temp
print("updated A value:",x)
print("updated A value:",y)
print("--------------------------------------------------")
# Method 3 swapping of two variables using arthematic operators
a = 8
b = 10
a = a+b
b = a-b
a = a-b
print("a value is:",a)
print("b value is:",b)
print("---------------------------------------------------")
# Method 4 swapping of two variables using numbering format
a = 8
b = 10
a = a+b
b = a-b
a = a-b
print("after swapping a=%d,b = %d " %(a,b))

