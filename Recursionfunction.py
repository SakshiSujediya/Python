from ast import Num


def factroial(x) :

    if x ==1 :
       return 1
    else :
       return (x * factroial(x-1))

Num=10
print("The factroial of", Num ,"=" ,factroial(Num))