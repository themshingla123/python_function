i=0
b=[]
while i<=13:
    count=0
    j=2
    while j<=i//2:
        if i%j==0:
            count=count+1
            j+=1
    if count==0 and i!=1:
        if i>11:
            x=i%10
            y=i//10
            z=str(x)+str(y)
            r=[i,int(z)]
            b.append(r)
    i=i+1
print(b)