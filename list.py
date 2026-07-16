Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list()
a = [2,3,56,7,8,4,9]
print(a)
[2, 3, 56, 7, 8, 4, 9]
type(a)
<class 'list'>
b = [11,5.6,"apple",3+9j,True,False]
print(b)
[11, 5.6, 'apple', (3+9j), True, False]
type(b)
<class 'list'>
#append()
c = [2,6,7,8,4,9,10]
c.append(36)
c
[2, 6, 7, 8, 4, 9, 10, 36]
d = [90,3.6,"mango",True,False]
d.append(9+4j)
d
[90, 3.6, 'mango', True, False, (9+4j)]
e = [999,40.5,"python",True]
e.append(5+6j,False)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    e.append(5+6j,False)
TypeError: list.append() takes exactly one argument (2 given)
e.append([5+6j,False])
e
[999, 40.5, 'python', True, [(5+6j), False]]
# extend()
x = ["html","css","js"]
x.extend(["python","java"])
print(x)
['html', 'css', 'js', 'python', 'java']
y = [2,7.9,"codegnan",3+3j]
y.extend(True)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    y.extend(True)
TypeError: 'bool' object is not iterable
y.extend(1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    y.extend(1)
TypeError: 'int' object is not iterable
y.extend("apple",5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    y.extend("apple",5)
TypeError: list.extend() takes exactly one argument (2 given)
#insert()
A = ["vijayawada",2,4.5,3+6j,True,False]
A.insert(36+56j)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    A.insert(36+56j)
TypeError: insert expected 2 arguments, got 1
A.insert("36+56j")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    A.insert("36+56j")
TypeError: insert expected 2 arguments, got 1
A.insert(3,36+56j)
A
['vijayawada', 2, 4.5, (36+56j), (3+6j), True, False]
#index()
a = ["apple","banana","grapes","kiwi"]
a.index("kiwi")
3
a.index("apple")
0
# sort()
b = ["kiwi","orange","apple",3+4j,8,True,False]
b.sort()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'complex' and 'str'
b = ["kiwi","orange","apple",True,False]
b.sort()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'bool' and 'str'
b = ["kiwi","orange","apple",2,6.8]
b.sort()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
b = ["kiwi","orange","apple","dragonfruit"]
b.sort()
b
['apple', 'dragonfruit', 'kiwi', 'orange']
c = [2,1,8,7,9,41,0]
c.sort()
c
[0, 1, 2, 7, 8, 9, 41]
d = [5.6,0.0,7.8,1.1,2.9]
d.sort()
d
[0.0, 1.1, 2.9, 5.6, 7.8]
e = [3+9j,8+7j,11+4j]
e.sort()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    e.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
f = [True,False]
f.sort()
f
[False, True]
#pop()
list1 = [2,6,8,"apple","banana",3+6j,True,False]
list1.pop()
False
list1
[2, 6, 8, 'apple', 'banana', (3+6j), True]
#copy()
list2 = [2,3,9+4j,"kiwi",8.0,True,False]
list3 = list2.copy()
print(list3)
[2, 3, (9+4j), 'kiwi', 8.0, True, False]
#clear()
list3.clear()
print(list3)
[]
#remove()
>>> x = [5,3.3,"lily",True,False,9+7j]
>>> x.remove("lily")
>>> x
[5, 3.3, True, False, (9+7j)]
>>> #count()

>>> x.count()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> x.count(5)
1
>>> y = ["mango","kiwi","apple","grapes"]
>>> y.count("mango")
1
>>> z= ["mango","kiwi","mango","apple","grapes","mango"]
>>> z.count("mango")
3
>>> #reverse()
>>> a = [4,5,9,7,11,56]
>>> a.reverse()
>>> a
[56, 11, 7, 9, 5, 4]
>>> b = ["kiwi","grapes","orange","apple","papaya","mango"]
>>> b.reverse()
>>> b
['mango', 'papaya', 'apple', 'orange', 'grapes', 'kiwi']
