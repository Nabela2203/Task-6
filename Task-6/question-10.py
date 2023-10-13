#10. Given a list [4,2,-3,1,6] Write a python program to find if there is sub-list with sum equal to zero?
#l1 = [4,2,-3,1,6]
#sum = 0
def sub_list(l1, n): # no. of values in list
    for i in range(n - 1):
        print("i", i)
        sum = l1[i]
        print("i-sum",sum)
        for j in range(i + 1, n):
            print("j",j)
            sum += l1[j]
            print("Sum", sum)
            if sum == 0:
                return True
    return False

print(sub_list([4, 2, -3, 1, 6], 5))