n=4
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    
n=6
for i in range(n):
    for j in range(i):
        print(i, end="")
    print()

n=6
val=65
for i in range(n):
    for j in range(i+1):
        print(chr(val), end="")
    val+=1
    print() 

n=7
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*", end="")
    print()

n=6
for i in range(n,0,-1):
    for j in range(0,i):
        print(i, end="")
    print()

n=5
for i in range(n,0,-1):
    for j in range(0,i):
        print(n, end="")
    print()

n=8
for i in range(1,n):
    for j in range(1,i+1):
        print(j, end="")
    print()

n=6
for i in range(n,0,-1):
    for j in range(0,i+1):
        print(j, end="")
    print()
