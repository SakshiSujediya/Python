
n=7
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print("\r")

for i in range (n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        print("* ",end="")
    print("\r")6