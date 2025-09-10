'''
Author: DongWoo Park
Date: 2025-09-10
이 프로그램은 점프 투 파이썬의 02-6~02-8 학습 기록이다.
'''

>>> s1=set([1,2,3])
>>> s1
{1, 2, 3}
>>> s2=set("Hello")
>>> s2
{'o', 'e', 'H', 'l'}
>>> l1=list(s1)
>>> l1
[1, 2, 3]
>>> l1[0]
1
>>> t1=tuple(s1)
>>> t1
(1, 2, 3)
>>> t1[0]
1
>>> s1=set([1,2,3,4,5,6])
>>> s2=set([4,5,6,7,8,9])
>>> s1&s2
{4, 5, 6}
>>> s1.intersection(s2)
{4, 5, 6}
>>> s1:s2
>>> s1|s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1-s2
{1, 2, 3}
>>> s2-s1
{8, 9, 7}
>>> s1.difference(s2)
{1, 2, 3}
>>> s2.difference(s1)
{8, 9, 7}
>>> s1=set([1,2,3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}
>>> s1=set([1,2,3])
>>> s1.update([4,5,6])
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1=set([1,2,3])
>>> s1.remove(2)
>>> s1
{1, 3}
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> 1==1
True
>>> 2>1
True
>>> 2<1
False
>>> a=[1,2,3,4]
>>> while a:
...     print(a.pop())
...
4
3
2
1
>>> if[1,2,3]:
...     print('참')
... else:
...     print('거짓')
...
참
>>> bool('python')
True
>>> bool('')
False
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool(0)
False
>>> bool(3)
True
>>> a=[1,2,3]
>>> id(a)
2110949564992
>>> a=[1,2,3]
>>> b=a
>>> id(a)
2110949564672
>>> id(b)
2110949564672
>>> a is b
True
>>> a[1]=4
>>> a
[1, 4, 3]
>>> b
[1, 4, 3]
>>> a=[1,2,3]
>>> b=a[:]
>>> a[1]
2
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> a[1]4
  File "<python-input-61>", line 1
    a[1]4
        ^
SyntaxError: invalid syntax
>>> a[1]=4
>>> a
[1, 4, 3]
>>> b
[1, 2, 3]
>>> from copy import copy
>>> a=[1,2,3]
>>> b=copy(a)
>>> b is a
False
>>> a=[1,2,3]
>>> b=a.copy()
>>> b is a
False
>>> a,b=('python', 'life')
>>> a=3
>>> b=5
>>> a,b=b,a
>>> a
5
>>> b
3
>>> a=[1,2,3]
>>> b=[1,2,3]
>>> a is b
False
>>> id(a)
2110949560192
>>> id(b)
2110949557056
