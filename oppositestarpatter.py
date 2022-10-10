for i in range(0,4):
    for j in range (0,4-i):
        print(" ",end=" ")
       
    for k in range(0,i+1):
        print("*", end=" ")
    print("\r")      

#right side Triangle
for i in range (0,5):
    for j in range(0,5-i):
         print(" ",end=" ")

    for k in range(0,i+1):
        print("* ",end="")

    print("\r")    