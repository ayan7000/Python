x=2
y=3
z=4
print((x+y)*z)
print(40+2.23)

print('chai'+'code')
print(x,y,z)
print(x+1,y*2)



'''

>>> 12+24
36
>>> 2.5*5
12.5
>>> 2 **4
16
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.randon()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    random.randon()
    ^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'randon'. Did you mean: 'random'?
>>> random.random()
0.5422287786543151
>>> username="ayansingh"
>>> len(username)
9
>>> username[0]
'a'
>>> username[0]='s'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    username[0]='s'
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
>>> list=[1,2,4]
>>> list[0]
1
>>> dic ={'1':'mango','2':'grapes'}
>>> dic
{'1': 'mango', '2': 'grapes'}
>>> dic['comic']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    dic['comic']
    ~~~^^^^^^^^^
KeyError: 'comic'
>>> tuple = (1,2,4)
>>> tuple
(1, 2, 4)
>>> import sys
>>> sys.getrefcount(24601)
3
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]
>>> h1=[1,2,3]
>>> h3=h1[:]
>>> h1[0]=55
>>> h1
[55, 2, 3]
>>> h2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    h2
NameError: name 'h2' is not defined
>>> h3
[1, 2, 3]
>>> m-[1,2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    m-[1,2,3]
    ^
NameError: name 'm' is not defined
>>> m=[1,2,3]
>>> m=n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    m=n
      ^
NameError: name 'n' is not defined
>>> n=m
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3]
>>> m==n
True
>>> m is n
False
>>> 2*100
200
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> repr(chai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    repr(chai)
         ^^^^
NameError: name 'chai' is not defined
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print(chai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(chai)
          ^^^^
NameError: name 'chai' is not defined
>>> print('chai')
chai
>>> 2<6
True
>>> 5.0==5.0
True
>>> 4.0!=5.0
True
>>> x=2
>>> y=3
>>> z=5
>>> x,y,z
(2, 3, 5)
>>> x<y<z
True
>>> 1==2<3
False
>>> import math
>>> math.floor(3.6)
3
>>> math.floor(-3.5)
-4
>>> math.trunc(2.9)
2
>>> math.trunc(-2.9)
-2
>>> 9999999999999999999 * 2.1
2.1e+19
>>> 2 + 1j
(2+1j)
>>> (2+1j)*3
(6+3j)
>>> 0o23
19
>>> 0xff
255
>>> 0b1000
8
>>> 0020
  File "<stdin>", line 1
    0020
    ^^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 0o20
16
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> int(64.99)
64
>>> int('54',8)
44
>>> x=1
>>> x<<2
4
>>> x|2
3
>>> import random
>>> random.random()
0.43019332957712453
>>> random.randomint(1,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    random.randomint(1,10)
    ^^^^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'randomint'. Did you mean: 'randint'?
>>> random.randint(1,10)  
4
>>> 
>>> 
>>> random.randint(1,10)
5
>>> random.randint(1,10)
4
>>> random.randint(1,10)
2
>>> l1=['lemo',2,'apple']
>>> random.choice(l1)
'apple'
>>> random.choice(l1)
'apple'
>>> random.choice(l1)
'lemo'
>>> random.shuffle(l1)
>>> l1
['apple', 'lemo', 2]
>>> 0.1+0.1).4
  File "<stdin>", line 1
    0.1+0.1).4
           ^
SyntaxError: unmatched ')'
>>> 0.1+0.1+0.4
0.6000000000000001
>>> 0.1+0.1+0.1
0.30000000000000004
>>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.3')+Decimal('0.2')
Decimal('0.6')
>>> Decimal('0.1')+Decimal('0.3')+Decimal('0.2')-Decimal('0.3')
Decimal('0.3')
>>>  

'''