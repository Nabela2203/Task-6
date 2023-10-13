# 1. You have been given a python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two list one which have
# all the even numbers and another list which will have all the ODD numbers in it?

l = [10, 501, 22, 37, 100, 999, 87, 351]
l1 =[]
l2 =[]

for num in l:
    if (num % 2 == 0):
        l1.append(num)
    else:
        l2.append(num)
print("Even number is: ", l1)
print("Odd number is: ", l2)