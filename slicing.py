Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Slicing
# Positive Slicing
a = "work until you succeed"
a[0:4]
'work'
a[5:10]
'until'
a[11:14]
'you'
a[15:22]
'succeed'
b = "time is very precious"
b[13:20]
'preciou'
b[13:21]
'precious'
b[0:4]
'time'
b[5:7]
'is'
b[8:12]
'very'
c = "simple is better than complex"
c[0:6]
'simple'
>>> # Negative Indexing
>>> x = "simple is better than complex"
>>> 
>>> x[-19:-13]
'better'
>>> x[-29:23]
'simple is better than c'
>>> x[-29:-23]
'simple'
>>> x[-7:]
'complex'
>>> y = "codegnan it solutions"
>>> y[-9:-1]
'solution'
>>> y[-21:-13]
'codegnan'
>>> y[-9:]
'solutions'
>>> y[-9:0]
''
>>> d[-1:-9]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[-1:-9]
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> y[-1:-9]
''
