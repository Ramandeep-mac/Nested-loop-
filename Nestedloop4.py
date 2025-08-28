Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> rows=5
>>> for i in range(rows+1,1,-1):
...     for j in range(i):
...         print(" ",end="*")
...     print()
... 
...     
 * * * * * *
 * * * * *
 * * * *
 * * *
 * *


>>> 
>>> rows=5
>>> for i in range(rows):
...     for j in range(rows-i-1):
...         print(" ",end=" ")
...     for j in range(1*i+1):
...         print(" ",end="*")
...     print()
... 
    
         *
       * *
     * * *
   * * * *
 * * * * *
