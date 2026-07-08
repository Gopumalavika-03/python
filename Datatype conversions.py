Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Datatype conversions
#int
int(3)
3
int(5.6)
5
int("code")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
int(5+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
# float
float(6)
6.0
float(3.6)
3.6
float("codegnan")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("codegnan")
ValueError: could not convert string to float: 'codegnan'
float(5+7j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
# str
str(6)
'6'
str(8.0)
'8.0'
str("Python")
'Python'
str(4+9j)
'(4+9j)'
str('True')
'True'
str('False')
'False'
# complex
complex(11)
(11+0j)
complex(65.0)
(65+0j)
>>> complex(65.3)
(65.3+0j)
>>> complex(5.6)
(5.6+0j)
>>> complex("apple")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("apple")
ValueError: complex() arg is a malformed string
>>> complex("5+6j")
(5+6j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> # bool
>>> bool(6)
True
>>> bool(9.5)
True
>>> bool("malu")
True
>>> bool("8+6j")
True
>>> bool(True)
True
>>> bool(False)
False
