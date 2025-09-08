'''
Author: DongWoo Park
Date: 2025-09-08
이 프로그램은 점프 투 파이썬의 02-4~02-5 학습 기록이다.
'''

>>> t1=(1,2,'a','b')
>>> t1(0)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    t1(0)
    ~~^^^
TypeError: 'tuple' object is not callable
>>> t1[0]
1
>>> t1[3]
'b'
>>> t1[1:]
(2, 'a', 'b')
>>> t2=(3,4)
>>> t3=t1+t2
>>> t3
(1, 2, 'a', 'b', 3, 4)
>>> t3=t2*3
>>> t3
(3, 4, 3, 4, 3, 4)
>>> len(t1)
4
>>> t4=(1,2,3)
>>> t5=(4)
>>> t4+t5
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    t4+t5
    ~~^~~
TypeError: can only concatenate tuple (not "int") to tuple
>>> t6=t4+t5
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    t6=t4+t5
       ~~^~~
TypeError: can only concatenate tuple (not "int") to tuple
>>> t6
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    t6
NameError: name 't6' is not defined. Did you mean: 't1'?
>>> t5(4,)
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    t5(4,)
    ~~^^^^
TypeError: 'int' object is not callable
>>> t5=(4,)
>>> t6
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    t6
NameError: name 't6' is not defined. Did you mean: 't1'?
>>> t6=t4+t5
>>> t6
(1, 2, 3, 4)
>>> a={1:'a'}
>>> a[2]='b'
>>> a
{1: 'a', 2: 'b'}
>>> a['name']='pey'
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}
>>> a[3]=[1,2,3]
>>> a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>> grade={'pey':10,'julliet':99}
>>> grade['pey]
  File "<python-input-31>", line 1
    grade['pey]
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> grade['pey']
10
>>> grade['julliet']
99
>>> a={1"'a',1:'b'}
  File "<python-input-34>", line 1
    a={1"'a',1:'b'}
        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a={1:'a',1:'b'}
>>> a
{1: 'b'}
>>> a={'name':'pey','phone':'010-9999-1234','birth':'1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
>>> for k in a.keys():
...     print(k)
...
name
phone
birth
>>> list(a.keys())
['name', 'phone', 'birth']
>>> a.values()
dict_values(['pey', '010-9999-1234', '1118'])
>>> a.items()
dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
>>> a.clear()
>>> a
{}
>>> a={'name':'pey','phone':'010-9999-1234','birth':'1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'010-9999-1234'
>>> print(a.get('nokey'))
None
>>> print(a['nokey'])
Traceback (most recent call last):
  File "<python-input-49>", line 1, in <module>
    print(a['nokey'])
          ~^^^^^^^^^
KeyError: 'nokey'
>>> a.get('nokey','foo')
'foo'
>>> 'name' in a
True
>>> 'email' in a
False
>>> dix={'name':'홍길동','birth':'1128','age':'30'}
>>> dix['name']
'홍길동'
