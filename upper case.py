def my(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]<="Z":
            b.append(a[i])
        i=i+1
    return b
print(my("HaRrIs"))