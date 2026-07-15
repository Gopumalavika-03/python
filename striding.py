Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> #positive striding
>>> a = "Machine Learning"
>>> a[::4]
'MiLn'
>>> a[::7]
'M n'
>>> a[;;2]
SyntaxError: invalid syntax
>>> a[::2]
'McieLann'
>>> a[2:8]
'chine '
>>> a[:9]
'Machine L'
>>> b = "cloud computing"
>>> b[4:14:4]
'dmi'
>>> b[6:10:1]
'comp'
>>> a[2:13:5]
'c n'
>>> b[2:13:5]
'ooi'
>>> #Negative striding
>>> a = "cloud computing"
>>> a[-4:-14:-4]
'tou'
a[-6:-10-1]
''
a[-6:-10:-1]
'pmoc'
a[-2:-13:-5]
'nmu'
a[-7:-4:-2]
''
