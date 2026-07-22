'''Given an array [5, 10, 12, 15]
Sum except first value
'''

A = [5, 10, 12, 15]

tot = sum(A[1:])
print(tot)

# Using index and range
result = 0
for idx in range(1, len(A)):
    result += A[idx]
print(result)