a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(a):
    k=a[i],a[i+1]
    b.append(k)
    i=i+2
print(b)