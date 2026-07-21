'''Given an array of [5, 10, 15, 20]
Sum but skip the next value until it ends
Applying 3 different approaches
'''

#First Approach using python built-in List slicing
#Syntax [start_idx:stop:step]
A = [5, 10, 15, 20, 3]
total = sum(A[::2])
print(f"The sum is -> {total}")


#Second Approach using range and for loop
#Usage range(start_idx,len,step)

B = [5, 10, 15, 20]
result = 0
for idx in range(0, len(B), 2):
    result += B[idx]
print(f'The result in range is -> {result}')



#Third Approach using enumerate and for loop
#Checks if idx is even
tot = 0
C = [5, 10, 15, 20]
for idx, val in enumerate(C):
    if idx % 2 == 0:
        tot += val
print(f'Total is {tot}')

