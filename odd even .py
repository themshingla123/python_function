def check_numbers_list(c,d):
    i=0
    while i<len(c):
        a=c[i]+d[i]
        if a%2==0:
            print("both are even")
        elif a%2!=0:
            print("both are odd")
        i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75])


# def my(list1 , list2):
#     i=0
#     while i<len(list1) and i<len(list2):
#         if list1[i]%2==0 and list2[i]%2==0:
#             print(list1[i],list2[i],"even")
#         else:
#             print(list1[i],list2[i],"odd")
#         i=i+1
# (my([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, ])