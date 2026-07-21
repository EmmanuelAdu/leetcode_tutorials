'''Given an array [5, 10, 12, 15]
Sum all except 12
'''
A = [5, 10, 12, 15]
result = 0
for val in A:
    if not val == 10:
        result += val
print(result)