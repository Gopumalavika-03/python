Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Data types
a = 5
type(a)
<class 'int'>
b = 3.6
type(b)
<class 'float'>
name = 'Malavika'
type(name)
<class 'str'>
A = "car"
type(A)
<class 'str'>
B = "Ball"
type(B)
<class 'str'>
c = '''Codegnan'''
type(c)
<class 'str'>
x = 6+7j
type(x)
<class 'complex'>
y = 3j
type(y)
<class 'complex'>
>>> z = 8j+9
>>> type(z)
<class 'complex'>
>>> b = j
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b = j
NameError: name 'j' is not defined
>>> c = "True"
>>> type(c)
<class 'str'>
>>> d = True
>>> type(d)
<class 'bool'>
>>> m = true
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    m = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> x = False
>>> type(x)
<class 'bool'>
>>> y = false
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    y = false
NameError: name 'false' is not defined. Did you mean: 'False'?
