#8. Write a python program to find the minimum element in a rated and sorted list?

l1 = [4,4,8,5,5,6]

l2 = sorted(l1) # alphabet order
print(l2)
print(min(l2))
#or
l1.sort(reverse=False)
print(l1)
print(min(l1))