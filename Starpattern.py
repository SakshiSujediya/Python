#simple star patter(5)
num=8
for i in range(0,num) :
    for j in range(0,i+1) :
       print("* ",end="")

    print("\r")


for i in range(0,num) :
    for j in range(0,num-i):
        print("* ",end="") 

    print("\r")    
        