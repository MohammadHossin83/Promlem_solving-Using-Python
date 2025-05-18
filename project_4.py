def reverse(text):
    result = ""  
    for i in text: 
        result = i + result
    return result 
reverse("mamad") 

///////////////////////

def cul(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return cul(x-1) + cul(x-2)
cul(8)
