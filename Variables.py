Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(3+3)
6
a=1
b=2
print(a+b)
3
name= Malavika
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name= Malavika
NameError: name 'Malavika' is not defined
name = "Malavika"
print(name)
Malavika
_ = "HI"
print(_)
HI
_ =5
print(_)
5
city="vijayawada"
print(city)
vijayawada
A = 100
A
100
2 = 200
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2 = 200
print(a2)
200
 r = 100
 
SyntaxError: unexpected indent
a = 1,2,3,4,5,6
print(a)
(1, 2, 3, 4, 5, 6)
@ = 500
SyntaxError: invalid syntax
firstname = "Gopu"
lastname = "Malavika"
print(firstname+lastname)
GopuMalavika
firstname = "Gopu"
lastname = "Malavika"
print(firstname " " lastname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
firstname = "Gopu"
lastname = "Malavika"
print(firstname + " " lastname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: invalid syntax
firstname = "Gopu"
lastname = "Malavika"
print(firstname+" "+lastname)
Gopu Malavika
a =4 , b =6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a = 5 ;b = 10
print(a+b)
15
a=5:b=8
SyntaxError: invalid syntax
a,b,c = 5,4,9
print(a+b+c)
18
a,b,c = 1,5,8,7,4,3
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a,b,c = 1,5,8,7,4,3
ValueError: too many values to unpack (expected 3, got 6)
a,b,c = (6,5,8)
print(a+b+c)
19
a,b,c = (6,5,8)
print(a,b,c)
SyntaxError: multiple statements found while compiling a single statement
a =6
print(a)
6
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'A'?
>>> a,b,c = (6,5,8)
... print(a,b,c)
SyntaxError: multiple statements found while compiling a single statement
>>> a,b,c = (5,4,8)
>>> print(a,b,c)
5 4 8
>>> fname = "Gopu"
>>> lname = "Malavika"
>>> print(fname , lname)
Gopu Malavika
>>> if = 50
SyntaxError: invalid syntax
>>> name = "Malu"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> NAME = "malu"
>>> print(NAME)
malu
