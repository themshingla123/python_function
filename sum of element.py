numbers = [1, 2, 3, 4, 5]
def my(numbers):
    i=0
    sum=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i=i+1
    return(sum)
print(my([1, 2, 3, 4, 5]))