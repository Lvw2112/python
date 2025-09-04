'''
Author: DongWoo Park
Date: 2025-09-04
이 프로그램은 점프 투 파이썬의 02-1~02-2 학습 기록이다
'''
print("="*50)
print("My Program")
print("="*50)

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a=0o117
>>> print(a)
79
>>> a=0o177
>>> print(a)
127
>>> a=ox8ff
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    a=ox8ff
      ^^^^^
NameError: name 'ox8ff' is not defined
>>> a=0x8ff
>>> print(a)
2303
>>> b=0xABC
>>> print(b)
2748
>>> a=3
>>> b=4
>>> a**b
81
>>> 10*18**2+2*11
3262
>>> 7%3
1
>>> 3%7
3
>>> 7/4
1.75
>>> 7//4
1
>>> 14//3
4
>>> 14%3
2
>>> food="Python's favorite food is perl"
>>> food
"Python's favorite food is perl"
>>> food='Python's favorite food is perl'
  File "<python-input-21>", line 1
    food='Python's favorite food is perl'
                                        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> say='"Python is very easy." he says.'
>>> say
'"Python is very easy." he says.'
>>> food='Python\'s favorate food is perl'
>>> food
"Python's favorate food is perl"
>>> say="\"Python is very easy.\" he says."
>>> say
'"Python is very easy." he says.'
>>> multiline="Life is too short\nYou need python"
>>> multiline
'Life is too short\nYou need python'
>>> multiline='''
... Life is too short
... you need python
... '''
>>> multiline
'\nLife is too short\nyou need python\n'
>>> print(multiline)

Life is too short
you need python

>>> head="Python"
>>> tail="is fun!"
>>> head+tail
'Pythonis fun!'
>>> tail=" is fun!"
>>> head+tail
'Python is fun!'
>>> a="Python"
>>> a*2
'PythonPython'
>>> a="Life is too short"
>>> len(a)
17
>>> b="'You need python'
  File "<python-input-42>", line 1
    b="'You need python'
      ^
SyntaxError: unterminated string literal (detected at line 1)
>>> b="'You need python'"
>>> len(b)
17
>>> a="Life is too short, You need Python"
>>> a[3]
'e'
>>> b=a[0]+a[1]+a[2]+a[3]
>>> b
'Life'
>>> a[0:4]
'Life'
>>> a[0"3]
  File "<python-input-50>", line 1
    a[0"3]
       ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a[0:3]
'Lif'
>>> a[19:]
'You need Python'
>>> a[19:-7]
'You need'
>>> a="20230331Rainy"
>>> date=a[:8]
>>> weather=a[8:]
>>> date
'20230331'
>>> weather
'Rainy'
>>> year=a[:4]
>>> day=a[4:8]
>>> weather=a[8:]
>>> year
'2023'
>>> day
'0331'
>>> weather
'Rainy'
>>> a="Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1]+'y'+a[2:]
'Python'
>>> "I eat %d apples." %3
'I eat 3 apples.'
>>> "I eat %s apples." %"five"
'I eat five apples.'
>>> number=3
>>> "I eat %d apples." %number
'I eat 3 apples.'
>>> number=10
>>> day="three"
>>> "I ate %d apples. so I was sick for %s days." %(numver, day)
Traceback (most recent call last):
  File "<python-input-75>", line 1, in <module>
    "I ate %d apples. so I was sick for %s days." %(numver, day)
                                                    ^^^^^^
NameError: name 'numver' is not defined. Did you mean: 'number'?
>>> "I ate %d apples. so I was sick for %s days." %(number, day)
'I ate 10 apples. so I was sick for three days.'
>>> "Error is %d%." %98
Traceback (most recent call last):
  File "<python-input-77>", line 1, in <module>
    "Error is %d%." %98
    ~~~~~~~~~~~~~~~~^~~
ValueError: incomplete format
>>> "Error is %d%." % 98
Traceback (most recent call last):
  File "<python-input-78>", line 1, in <module>
    "Error is %d%." % 98
    ~~~~~~~~~~~~~~~~^~~~
ValueError: incomplete format
>>> "Error is %d%%." % 98
'Error is 98%.'
>>>
>>> "%10s" % "hi"
'        hi'
>>> "%-10sjane." % "hi"
'hi        jane.'
>>> "%0.4f" % 3.42134234
'3.4213'
>>>
>>> "%10.4f" % 3.42134234
'    3.4213'
>>> "I eat {0} apples".format(3)
'I eat 3 apples'
>>> "{0:<10}
  File "<python-input-87>", line 1
    "{0:<10}
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:^10}".format("hi")
'    hi    '
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:10.4f}".format(y)
Traceback (most recent call last):
  File "<python-input-91>", line 1, in <module>
    "{0:10.4f}".format(y)
                       ^
NameError: name 'y' is not defined
>>> y=3.42134234
>>> "{0:10.4f}".format(y)
'    3.4213'
>>> "{{and}}".format()
'{and}'
>>> name='ghdrlfehd'
>>> name='홍길동'
>>> age=30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> ㅁㅎㄷ=30
>>> age=30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
>>> d={'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> f'{!!!python!!!}'
  File "<python-input-104>", line 1
    f'{!!!python!!!}'
       ^
SyntaxError: f-string: valid expression required before '!'
>>> f'{{!!!python!!!}}'
'{!!!python!!!}'
>>> f'{"python":!^12}
  File "<python-input-106>", line 1
    f'{"python":!^12}
    ^
SyntaxError: unterminated f-string literal (detected at line 1)
>>> f'{"python":!^12}'
'!!!python!!!'
>>> a="hobby"
>>> a.count('b')
2
>>> a="Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
>>> a="Life is too short"
>>> a.index('t')
8
>>> ",".join('abcd')
'a,b,c,d'
>>> a="hi"
>>> a.upper()
'HI'
>>> a=" hi "
>>> a.lstrip()
'hi '
>>> a.rstrip()
' hi'
>>> a.strip()
'hi'
>>> a="Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
>>> a=
  File "<python-input-124>", line 1
    a=
      ^
SyntaxError: invalid syntax
>>> a="Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b="a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']
>>> a='hi'
>>> a.upper()
'HI'
>>> a
'hi'
>>> a=a.upper()
>>> a
'HI'
