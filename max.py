def my(number):
    i=0
    max=0
    while i<len(number):
        if number[i]> max:
            max=number[i]
        i=i+1
    return max
print(my([3, 5, 7, 34, 2, 89, 2, 5]))