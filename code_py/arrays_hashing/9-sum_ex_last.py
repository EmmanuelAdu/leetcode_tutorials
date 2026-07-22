'''Given an array of [5, 10, 15, 20]
Sum except last value
'''

A = [5, 10, 15, 20, 9]
tot = sum(A[:-1:])
print(tot)

# Using range
total = 0
for idx in range(len(A) - 1):
    total += A[idx]
print(total)