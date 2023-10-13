#6. You have been given three lists. Your task is to find the dupliactes in the three lists. Write a python program for
# the same. You can use your own python lists?

l1 = [2,2,2,4,4,8,5,9,6,3,3,3]
l2 = [4,4,8,5,5,6]
l3 = [1,2,2,3,3,4,5]
l = l1+l2+l3
#print(len(l))
#print(l)
uni = [] # unique char.
dup = [] # duplicates

for ele in l:
    if ele not in uni:
        uni.append(ele)
    elif ele not in dup:
        dup.append(ele)

print("Duplicates: ",dup)
print("Unique: ", uni)