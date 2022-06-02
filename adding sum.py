l1 = [7,2,4,3]
l2 = [5,6,4]
i=0
s=""
while i<len(l1):
    s=s+str(l1[i])
    i+=1
j=0
s1=""
while j<len(l2):
    s1+=str(l2[j])
    j+=1
sum=int(s)+int(s1)
print(sum)