def num(a,b):
    i=0
    c=[]
    while i<len(a):
        j=0
        while j<len(b):
            c.append(str(a[i])+str(b[j]))
            j=j+1
        i=i+1
    print(c)
num(a=[1,2,3],b=[3,4,5])


# def num(a):
#     i=0
#     b=[]
#     while i<len(a):
#         j=0
#         while j<len(a):
#             c=str(a[i])+str(a[j])
#             b.append(c)
#             j=j+1
#         i=i+1
#     print(b)
# num([2,3,4])


def num(a):
    i=0
    b=[]
    while i<len(a)-1:
        c=a[i]+a[i+1]
        b.append(c)
        i=i+1
    print(b)
    j=0
    max=0
    while j<len(b):
        if b[j]>max:
            max=b[j]
        j=j+1
    print(max)
num([4,23,2,8])


# a=[1,2,3]
# b=[4,5,3]
# i=0
# c=[]
# while i<len(a) and i<len(b):
#     d=a[i],b[i]
#     c.extend(d)
#     i=i+1
# print(c)