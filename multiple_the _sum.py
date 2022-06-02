def my(n,n1):
    if n>0 and n1>0:
        i=0
        s=0
        while i<=n1:
            m=i*n
            if m==n1 or m<n1:
                s=s+m
            i=i+1
        print(s)
    else:
        print("invalid")
n=int(input("enter the number"))
n1=int(input("enter the number"))
my(n,n1)