#4. Write a python program to find the sum of the first and last digit of the integer?

num = int(input("Enter number: ")) #100
last = num%10 #0
while num!=0: # outer condition
    first = num%10 # initial loop start #1.0 , 2.1
    num = num//10 #1.1, 2.0.1
sum = last+first #2.0+1
print("sum of the first and last digit is: ", sum)