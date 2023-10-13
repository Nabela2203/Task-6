#3. Given a python list [10, 501, 22, 37, 100, 999, 87, 351]. Find out how many numbers are there in the given Python list
# which are Happy numbers? - positive integer - 68 => 6**2(6*6) + 8**2(8*8) = 100 => 1**2 +0**2 +0**2 = 1 -(result  - 1) not a happy number result = 4
# magic number - sum of digits =1 - 172 -  1+7+2 = 10 and again 1+0 = 1

l1 = [10, 501, 22, 37, 100, 999, 87, 351]

for n in l1: # convert list to integer
    #print(n, end=" ")
    x = n
    #print(x)
    #print(type(x))
    while x!=1 and x!=4: # outer condition - result - 1 (happy no.), 4 (not happy no.)
        sum = 0
        while x>0: # Initial condition
            rem = x%10
            sum = sum +(rem**2)
            x=x//10 # // - floor division - removes decimal point - x==1 - come out of the loop
        #print("Sum: ", sum)
        x=sum
    if x==1:
        print(n, "is a happy number")