Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Operators
# Arithmetic operators
a = 3
b = 6
print(a+b)
9
print(a-b)
-3
print(a*b)
18
print(a//b)
0
print(a/b)
0.5
print(a%b)
3
# Assignment operators
a = 5
b = 2
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
a-=b
a
5
a*=b
a
10
a//=b
a
5
a/=b
a
2.5
a%=b
a
0.5
b = 4
c = 8
print(b+=c)
SyntaxError: invalid syntax
b+=2
b
6
b-=3
b
3
b*=2
b
6
b//=8
b
0
b/=2
b
0.0
b%=5
b
0.0
# Comparison operators
a = 5
b = 3
a>b
True
b<a
True
a>b
True
b>a
False
a<b
False
a>=b
True
a<=b
False
a!=b
True
a==b
False
a=10
b=10
a==b
True
# Logical operators
a = 11
b = 36
a<b and a>b
False
b>a and a<b
True
a!=b and a<b
True
not True
False
not False
True
# Identity operators
a = 3
type(a) is int
True
type(a) is not int
False
a = "malu"
type(a) is str
True
type(a)is not str
False
c = 5.6
type(c) is float
True
type(c) is not float
False
d = 5+3j
type(d) is complex
True
type(d) is not complex
False
e = True
type(e) is bool
True
type(e) is not bool
False
f = False
type(f) is bool
True
type(f) is not bool
False
# Membership operators
a = 11,36,56,22,3,16,1,20
11 in a
True
9 in a
False
3  not in a
False
56 in a
True
1 not in a
False
b = 3.14,"apple",3+5j , 2,True
joy in b
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    joy in b
NameError: name 'joy' is not defined
"joy" in b
False
5j in b
False
2 not in b
False
3.14 in b
True
2,3.14 in b
(2, True)
# Bitwise operators
a = 3
b = 9
a&b
1
a = 5
b = 2
a|b
7
>>> a = 11
>>> -(a+1)
-12
>>> ~a
-12
>>> c = -9
>>> -(c+1)
8
>>> a = 5
>>> b = 3
>>> a~b
SyntaxError: invalid syntax
>>> a = 2
>>> b = 3
>>> a^b
1
>>> a = 4
>>> a<<2
16
>>> b = 8
>>> b<<4
128
>>> c = 56
>>> c>>8
0
>>> d = 7
>>> d>>6
0
