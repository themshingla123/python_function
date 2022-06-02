def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number"))
res=factorial(n)
print(res)

def my(b):
    if b==1 or b==2:
        return 1
    
    else:
        return(my(b-1)+(my(b-2)))
print(my(8))


def my():
    print("bts")
    my()
my()

def fun(num):
    a=num*num
    return a
def fun2(num):
    b=num*num*num
    return b
def main():
    c=fun(num)+fun2(num)
    return c
num=int(input("enter the number"))