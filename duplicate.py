def num(a):
    i=0
    b=[]
    b1=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        else:
            b1.append(a[i])
        i=i+1
    print(b1)
num([1,2,3,3,3,3,4,5])