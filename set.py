Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # set{}
>>> a = {4,6.7,8+6j,"Python",True,False}
>>> print(a)
{False, True, 4, 6.7, (8+6j), 'Python'}
>>> type(a)
<class 'set'>
>>> # add()
>>> b = {2,3,8,9,7,4,6,1}
>>> b.add(5)
>>> print(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> b.add(10)
>>> print(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> #issubset
>>> a = {3,4,5,6,7,8}
>>> b = {6,7,8,9,10}
>>> b.issubset(a)
False
>>> c = {1,2,3}
>>> d = {4,5,6,1,2,3}
>>> c.issubset(d)
True
>>> #superset()
>>> e = {5,6,7,8,9,10,11}
>>> f = {7,8,9,10}
>>> e.issuperset(f)
True
f.issuperset(e)
False
# union()
a = {3,3,4,5,9,7,8}
b = {1,6,2,10,12,11}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#intersection()
c = {3,36,8,7,56,11}
d = {2,5,7,11,36,56,45}
c.intersection(d)
{56, 11, 36, 7}
d.intersection(c)
{56, 11, 36, 7}
#difference()
e = {7,8,9,10,11,12,13}
f = {8,9,10,11,12,13,14,15}
e.difference(f)
{7}
f.difference(e)
{14, 15}
# update()
m = {2,3,4,5,6}
n = {1,4,5,6,7,8,9}
m.update(n)
m
{1, 2, 3, 4, 5, 6, 7, 8, 9}
n.update(m)
n
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#symmetric difference()
a = {2,3,4,5,6,7,8}
b = {1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}
b.symmetric_difference(a)
{1, 2, 3, 5, 7, 9, 10, 11}
#difference_update()
x = {1,3,4,2}
y = {4,5,3,5,6,7}
x.difference_update(y)
x
{1, 2}
y.difference_update(x)
y
{3, 4, 5, 6, 7}
#intersection_update()
a = {3,4,5,6,7,8}
b = {5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
a
{8, 5, 6, 7}
#symmetric_difference_update()
c = {11,12,13,14,15,16}
d = {13,14,15,16,17,18}
c.symmetric_difference_update(d)
c
{17, 18, 11, 12}
d.symmetric_difference_update(c)
d
{16, 11, 12, 13, 14, 15}
#copy()
e = {1,3,4,3,5,6,7}
f =v.copy()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    f =v.copy()
NameError: name 'v' is not defined
f = e.copy()
f
{1, 3, 4, 5, 6, 7}
f
{1, 3, 4, 5, 6, 7}
e
{1, 3, 4, 5, 6, 7}
#discard()
num={1,2,3,4,3}
num.discard(4)
num
{1, 2, 3}
#remove()
letters = {"a","b","c"}
letters.remove("c")
letters
{'a', 'b'}
#isdisjoint()
set1 = {1,2,3}
set2 = {4,5,6}
set3 = {3,7,8}
print(set1.isdisjoint(set2))
True
print(set1.isdisjoint(set3))
False
#pop()
a = {3,4,5,67,8}
a.pop()
67
a
{3, 4, 5, 8}
a.pop(8)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.pop(8)
TypeError: set.pop() takes no arguments (1 given)
#clear()
x ={3,4,5,6,7,8}
x.clear()
x
set()
y = {18,12,25,30,95}
y.clear()
y
set()
