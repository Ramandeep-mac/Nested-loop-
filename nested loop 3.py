Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> # NESTED LOOP

  

>>> rows=5
>>> for i in range(0,rows+1):
...     for j in range(i):
...         print(i,end="")
...     print()
... 
...     

1
22
333
4444
55555


 
>>> rows=5
>>> for i in range(1,rows+1):
...     for j in range(i):
...         print(j+i,end=" ")
...     print()
... 
...     
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
