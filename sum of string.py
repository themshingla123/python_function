def num(a):
    l=list(a)
    i=0
    b=0
    while i<len(a):
        b=b+int(a[i])
        i=i+1
    print("'",b,"'")
num(a=("4","5"))