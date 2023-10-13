# 2. Given a python list [10, 501, 22, 37, 100, 999, 87, 351] your task is to count all the prime numbers and create a new
# Python list which will contain all the Prime numbers in it?

l1 = [10, 501, 22, 37, 100, 999, 87, 351]
prime_num = []
not_prime_num = set()

for num in l1:
    count = 0
    for i in range(1, 10): #1,2,3,4,5,6,7,8,9
        if num%i == 0:
            count+=1
            if count>1:
                not_prime_num.add(num)
    if count == 1:
        prime_num.append(num)

print(not_prime_num, "is not a prime number")
print(prime_num, "is a prime number")
print("Count:",len(prime_num))