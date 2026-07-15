Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# String Methods
# len()
a = "codegnan"
len(a)
8
b = "Python course"
len(b)
13
c = ""
len(c)
0
d = " "
len(d)
1
e = "  "
len(e)
2
# count()
x = "twinkle twinkle little star"
count(x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(x)
NameError: name 'count' is not defined. Did you mean: 'round'?
x.count("twinkle")
2
x.count("t")
5
x.count(" ")
3
x.count("")
28
x.count("m")
0
x.count()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x.count()
TypeError: count expected at least 1 argument, got 0
# find the string
a = "vijayawada"
a.find("y")
4
a.find("a")
3
a.find("x")
-1
# escape sequences
# \n --> new line or next line
# \t --> tab space(4 to 8)
M = "name:\nemailid:\tmobile no:\ncollege name:\tbranch:
SyntaxError: unterminated string literal (detected at line 1)
M = "name:\nemailid:\tmobile no:\ncollege name:\tbranch:"
print(M)
name:
emailid:	mobile no:
college name:	branch:
M
'name:\nemailid:\tmobile no:\ncollege name:\tbranch:'
N = "name: G.Malavika\n emailid: malu@gmail.com\tmobile no:8688472532\ncollege name: VITW\tbranch:CSE-DS"
print(N)
name: G.Malavika
 emailid: malu@gmail.com	mobile no:8688472532
college name: VITW	branch:CSE-DS
# replace()
a = "Coding is the key to success"
a.replace("Coding","Practice")
'Practice is the key to success'
b = "Practice"
b.replace("Practice","work hard")
'work hard'
c = "python java"
c.replace("p","c")
'cython java'
d = "wait wait until you succeed"
d.replace("wait","work")
'work work until you succeed'
d.replace("wait","work",1)
'work wait until you succeed'
e = "work work until you succeed"
e.replace("work","wait",1)
'wait work until you succeed'
#upper()
x = "code"
x.upper()
'CODE'
y = "malu"
y[0].upper()
'M'
y.upper(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    y.upper(a)
TypeError: str.upper() takes no arguments (1 given)
#lower()
a = "PYTHON"
a.lower()
'python'
b = "MANGO"
b.lower()
'mango'
#Capitalize()
c = "python"
c.captalize()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'Python'
d = "html"
d.capitalize()
'Html'
#title() method
x = "i love python"
x.title()
'I Love Python'
y = "codegnan"
y.title()
'Codegnan'
#isupper(),#islower(),#isalpha(),#isdigit(),#isalnum() methods
A = "MALAVIKA"
A.isupper()
True
B = "apple"
B.islower()
True
C = "123malu"
C.isalpha()
False
D = "banana"
D.isalpha
<built-in method isalpha of str object at 0x0000013F95BD22B0>
D.isalpha()
True
E = 123456789
E.isdigit()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    E.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
F = "563611"
F.isdigit()
True
G= "123 456 789"
G.isdigit()
False
H = "malu123"
H.isalnum()
True
I = "apple 01"
I.isalnum()
False
J = "good girl"
J.isalpha()
False
#startswith() and #endswith()
a = "data science"
a.startswith("d")
True
a.endswith("e")
True
a.endswith("m")
False
a.startswith("s")
False
# strip()
#lstrip()
#rstrip()
x = "               malavika              "
x.strip()
'malavika'
x.lstrip()
'malavika              '
x.rstrip()
'               malavika'
#split()
a = "python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b = "i love python"
b.split()
['i', 'love', 'python']
#join
b = "html","css","java","c"
"".join(b)
'htmlcssjavac'
"m".join(b)
'htmlmcssmjavamc'
c = "python"
"l".join(c)
'plyltlhloln'
" ".join(c)
'p y t h o n'
#concatenation()
a = "code"
b = "gnan"
print(a+b)
codegnan
b = "python"
c = "course"
print(b+" "+c)
python course
fname = "malu"
lname = "gopu"
print(fname+lname)
malugopu
print(fname+" "+lname)
malu gopu
#formatting()
a = 5
b = 6
print(a+b)
11
print("Sum is ",a+b)
Sum is  11
city = "vijayawada"
print("city is",city)
city is vijayawada
#format()
a = "motu"
b = "patlu"
print("hello {} {}".format(a,b))
hello motu patlu
print("hello{} hello{}".format(a,b))
hellomotu hellopatlu
print("hello { } hello { }".format(a,b))
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    print("hello { } hello { }".format(a,b))
KeyError: ' '
>>> print("hello+ " "+{}+hello+" "+{}".format(a,b))
hello+ +motu+hello++patlu
>>> print("hello\t{}\thello\t{}".format(a,b))
hello	motu	hello	patlu
>>> print("hello{}\nhello{}".format(a,b))
hellomotu
hellopatlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring()
>>> a = "malu"
>>> b = "gopu"
>>> print(f"hello{a} {b}")
hellomalu gopu
>>> print(f"hello {a} {b}")
hello malu gopu
>>> print((f"hello {a} {b}"),title())
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    print((f"hello {a} {b}"),title())
NameError: name 'title' is not defined. Did you mean: 'tuple'?
>>> print((f"hello {a} {b}").title())
Hello Malu Gopu
>>> print(("hello {} hello {}".format(a,b)).title())
Hello Malu Hello Gopu
