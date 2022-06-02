# a="this is a cup"
# i=0
# b=[]
# s=""
# while i<len(a):
#     if a[i]==" ":
#         b.append(s)
#         s=""
#     else:
#         s+=a[i]
#     i=i+1
# if s:
#     b.append(s)
# print(b)

def fun(a):
    b=a.split()
    print(b)
fun("my name")
