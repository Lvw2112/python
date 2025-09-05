'''
Author: DongWoo Park
Date: 2025-09-05
이 프로그램은 점프 투 파이썬의 02-3 학습 기록이다.
'''

>>> odd=[1,3,5,7,9]
>>>  a=[1,2,3]
  File "<python-input-1>", line 1
    a=[1,2,3]
IndentationError: unexpected indent
>>> a
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[1,2,3]
>>> a[0]
1
>>> a[0]+a[2]
4
>>> a=[1,2,3,['a','b','c']]
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
>>> a[-1][0]
'a'
>>> a=[1,2,['a','b',['Life','is']]]
>>> a[2][2][0]
'Life'
>>> a=[1,2,3,4,5]
>>> a[0:2]
[1, 2]
>>> a="12345"
>>> a[0:2]
'12'
>>> a[1,2,3,4,5]
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    a[1,2,3,4,5]
    ~^^^^^^^^^^^
TypeError: string indices must be integers, not 'tuple'
>>> a=[1,2,3,4,5]
>>> a[1:3]
[2, 3]
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> len(a)
3
>>> str(a[2])+"hi"
'3hi'
>>> a[2]=4
>>> a
[1, 2, 4]
>>> del a[1]
>>> a
[1, 4]
>>> a=[1,2,3,4,5]
>>> del a[2:]
>>> a
[1, 2]
>>> a=[1,2,3]
>>> a.append([5,6])
>>> a
[1, 2, 3, [5, 6]]
>>> a=[1,4,3,2]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a=['a','c','b']
>>> a.reverse()
>>> a
['b', 'c', 'a']
>>> a=[1,2,3,4]
>>> a.index(3)
2
>>> a.index(1)
0
>>> a=[1,2,3]
>>> a.insert(0,4)
>>> a
[4, 1, 2, 3]
>>> a=[1,2,3,1,2,3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]
>>> a=[1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
>>> a=[1,2,3]
>>> a.extend([4,5])
>>> a
[1, 2, 3, 4, 5]
>>> b=[6,7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]


