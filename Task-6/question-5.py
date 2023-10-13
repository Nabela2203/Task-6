# 5. You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable
# number of Mangoes. There are M students in a Guvi class, your task is to distribute the Mangoes in such a way that
# each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with
# minimum Mangoes given to the student is minimum ?

def min_mango_difference (mangoes, students) :
    mangoes.sort() # Sort the list of mangoes in ascending order
    min_difference = 9999 # Initialize minimum difference to a large value

    for i in range(len(mangoes) - students + 1): #4-2+1 = 3
        current_difference = mangoes[i + students - 1] - mangoes[i]
        if current_difference < min_difference:
            min_difference = current_difference
    return min_difference
N = int (input("Enter the number of bags:" ))
M = int(input("Enter the number of students: "))
mangoes = []
for i in range(N):
    mangoes.append(int(input(f"Enter the number of mangoes in bag {i + 1}: ")))
print(mangoes)
if N < M:
     print("Number of bags cannot be less than the number of students.")
else:
    result = min_mango_difference(mangoes, M)
    print("Minimum difference in mangoes:", result)