
import time

print("chai is here")

username= "ayan"
print("username")

'''
>>> f = open('file.py')
>>> f.readline()
'\n'
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'\n'
>>> f.readline()
'username= "ayan"\n'
>>> f.readline()
'print("username")\n'
>>> f.readline()
''

for line in open('file.py'):
     print(line)

     

'''



'''


>>> l =[1,2,3,4,5]
>>> ls =iter(l)
>>> ls
<list_iterator object at 0x0000017F8295FBE0>
>>> l.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    l.__next__()
    ^^^^^^^^^^
AttributeError: 'list' object has no attribute '__next__'. Did you mean: '__ne__'?
>>> ls.__next__()
1
>>> ls
<list_iterator object at 0x0000017F8295FBE0>
>>> ls.__next__()
2
>>> ls.__next__()
3
>>> ls.__next__()
4
>>> ls.__next__()
5
>>> ls.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    ls.__next__()
    ~~~~~~~~~~~^^
StopIteration
>>> 
>>> f = open('chai.py'
... iter(f) is f      
  File "<stdin>", line 1
    f = open('chai.py'
             ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> f = open('chai.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f = open('chai.py')
FileNotFoundError: [Errno 2] No such file or directory: 'chai.py'
>>> f = open('file.py')
>>> iter(f) is f       
True
>>> iter(f) is f.__iter__()
True
>>> l1=[1,2,3]
>>> iter(l1) is l1
False
>>> d ={'a':'1','b':'2'}
>>> for key in D.keys():
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for key in D.keys():
...     print(key)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for key in D.keys():
               ^
NameError: name 'D' is not defined
>>> for key in d.keys():
...     print(key)      
... 
a
b
>>> i= iter(d)
>>> i
<dict_keyiterator object at 0x0000017F82968C20>
>>> next(i)
'a'
>>> 
>>> range (5)
range(0, 5)
>>> r =range(5)
>>> r
range(0, 5)
>>> i =itet(r)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    i =itet(r)
       ^^^^
NameError: name 'itet' is not defined. Did you mean: 'iter'?
>>> i =iter(r)
>>> i
<range_iterator object at 0x0000017F826E7B70>
>>> 


'''