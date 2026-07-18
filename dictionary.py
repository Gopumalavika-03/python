Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a = {"name":"kushi","city":"vijayawada"}
print(a)
{'name': 'kushi', 'city': 'vijayawada'}
type(a)
<class 'dict'>
# methods
# keys()
a = {"name":"kushi","city":"vijayawada","month":"july"}
a.keys()
dict_keys(['name', 'city', 'month'])
a = {"name":"kushi","city":"vijayawada","month":"july","year" : 2026}
a.keys()
dict_keys(['name', 'city', 'month', 'year'])
#values()
b = {"name":"kushi","city":"vijayawada","month":"july","rollno" :11}
b.values()
dict_values(['kushi', 'vijayawada', 'july', 11])
# items()
b = {"name":"kushi","city":"vijayawada","month":"july","rollno" :11,"age" : 16}
b.items()
dict_items([('name', 'kushi'), ('city', 'vijayawada'), ('month', 'july'), ('rollno', 11), ('age', 16)])
#update()
x =  {"name":"kushi","city":"vijayawada","month":"july","rollno" :11}
x.update({"year" : 2026})
x
{'name': 'kushi', 'city': 'vijayawada', 'month': 'july', 'rollno': 11, 'year': 2026}
y = {"name":"kanth","city":"mantada"}
y.update({"month" : 4},{"age" , 18})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    y.update({"month" : 4},{"age" , 18})
TypeError: update expected at most 1 argument, got 2
y = {"name":"kanth","city":"mantada"}
y.update({"month" : 4,"age" , 18})
SyntaxError: ':' expected after dictionary key
y.update({"month" : 4,"age":18})
y
{'name': 'kanth', 'city': 'mantada', 'month': 4, 'age': 18}
# setdefault()
z = {"name" : "malu","branch" : "CSE-DS","year":2026}
z.setdefault("mail" :"malu123@gmail.com")
SyntaxError: invalid syntax
z.setdefault("mail","malu123@gmail.com")
'malu123@gmail.com'
z
{'name': 'malu', 'branch': 'CSE-DS', 'year': 2026, 'mail': 'malu123@gmail.com'}
#pop()
z = {"name" : "malu","branch" : "CSE-DS","year":2026}
z.pop()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    z.pop()
TypeError: pop expected at least 1 argument, got 0
A={"name" : "malu","branch" : "CSE-DS","year":2026}
A.pop("year")
2026
A
{'name': 'malu', 'branch': 'CSE-DS'}
#popitem()
A.popitem()
('branch', 'CSE-DS')
A.popitem()
('name', 'malu')
A
{}
# copy()
s ={"name" : "malu","branch" : "CSE-DS","year":2026}
a = s.copy()
a
{'name': 'malu', 'branch': 'CSE-DS', 'year': 2026}
>>> len(a)
3
>>> #dictionary doesn't allow duplicates
>>> M = {"name" : "malu","branch" : "CSE-DS","year":2026,"name": "malu"}
>>> print(M)
{'name': 'malu', 'branch': 'CSE-DS', 'year': 2026}
>>> R= {"name1" : "malu","branch" : "CSE-DS","year":2026,"name2": "malu"}
>>> print(R)
{'name1': 'malu', 'branch': 'CSE-DS', 'year': 2026, 'name2': 'malu'}
>>> R.count()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    R.count()
AttributeError: 'dict' object has no attribute 'count'
>>> R.index("branch")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    R.index("branch")
AttributeError: 'dict' object has no attribute 'index'
>>> #clear()
>>> V={"name1" : "malu","branch" : "CSE-DS","year":2026,"name2": "malu"}
>>> V.clear()
>>> V
{}
>>> V.update({"name" : "malu"})
>>> V
{'name': 'malu'}
