def mid(string):
    if len(string) %2==0:
        return""
    else:
        num=int(len(string)/2)
        return string[num:num+1]
print(mid("abc"))
print(mid("katimla"))