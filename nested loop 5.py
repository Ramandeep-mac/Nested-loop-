Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
rows=5
num=1
for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
    print()

    
1 
1 1 
1 1 1 
1 1 1 1 
1 1 1 1 1 
for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

    
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 



 
