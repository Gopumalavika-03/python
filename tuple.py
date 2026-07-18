Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a = (8,3.5,"apple",3+5j,True,False)
>>> print(a)
(8, 3.5, 'apple', (3+5j), True, False)
>>> type(a)
<class 'tuple'>
>>> b = (7, 5.8,"mango",8+7j,True,False)
>>> b.index(7)
0
>>> b.index(5.8)
1
>>> b.index("mango")
2
>>> b.index(8+7j)
3
>>> b.index(True)
4
>>> len(b)
6
>>> #count()
>>> b.count(8+7j)
1
>>> b.count("kiwi")
0
