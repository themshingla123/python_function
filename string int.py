def num(a):
    i=0
    count=0
    while i<len(a):
        if a[i][0]==a[i][-1]:
            count+=1
        i=i+1
    print(count)
num(["abc","xyz","aba","1221"])