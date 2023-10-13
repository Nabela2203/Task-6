#7. Write a python program to find the first non - repeating elements in a given list of integer.

l1 = [4,4,8,5,5,6]
l2 = []

for ele in l1:
    if l1.count(ele) == 1: # count(ele) == 1 => 8,6 - count() - Returns the number of elements with the specified value
        l2.append(ele)
print(l2)
print("first non - repeating elements:", l2[0])