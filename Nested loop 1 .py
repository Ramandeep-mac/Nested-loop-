Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> print("Day 5")
Day 5
>>> print("Today's topic is Nested looping")
Today's topic is Nested looping
>>> 
>>> for i in range(1,4):
...     for j in range(1,4):
...         print(i*j,end=" ")
...         print()
... 
...         
1 
2 
3 
2 
4 
6 
3 
6 
9 
>>> for i in range(1,4):
...     for j in range(1,4):
...         print(i*j,end=" ")
...      print()
...      
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
