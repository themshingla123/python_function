def count(a):
    i=0
    upper=0
    lower=0
    while i<len(a):
        if a[i].isupper():
            upper+=1
        else:
            lower+=1
        i+=1
    print("uppercase",upper)
    print("lowercase",lower)
a=input("enter the character")
count(a)