import math as m

def my_function(x,z):
    if 0 <= z <= 1:
        return z
    else:
        return 1 / m.abs(x) + m.exp(-z)

print("result=", my_function(1,2))

/////////////////////

def countup(x,y):
    print(x)
    if(x==y):
        return 0
    else:
        countup(x-1,y)
countup(10,0)
