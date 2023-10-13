#9. You have been given a python list [10,20,30,9] and value of 59. write a python progrma to find the triplet in the list
# whose sum is equal to the given value? Triplet - which three elements can join to give a certain sum -59

def triplet_sum(l1, x, n): # n= no. of values in list,x-sum,l1-list
    l1.sort() #9,10,20,30
    for i in range(n): # i = 0 (constant), l and k - changes
        l = i+1 #1.l=1,k=3, 2.l=2,k=3
        k = n-1
        while(l<k):
            sum = l1[i]+l1[l]+l1[k] #2nd - 9+20+30
            if sum==x:
                return True
            if sum<x:
                l+=1
            else:
                k-=1
    return False
print(triplet_sum([10,20,30,9],59,4))