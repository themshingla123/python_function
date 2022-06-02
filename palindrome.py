a=["n","i","t","i","n"]
def num(a):  
    i=-1
    b=[]
    while i>=(-len(a)):
        b.append(a[i])
        i-=1
    if a==b:
        print("palindrome")
    else:
        print("not pallindrome")
num(["n","i","t","i","n"])