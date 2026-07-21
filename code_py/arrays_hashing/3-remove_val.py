'''Given an array [5, 10, 15, 20]
Remove 15 from array and print new list
'''
A = [5, 10, 15, 20]

for idx, val in enumerate(A):
    if val == 15:
        del(A[idx])
print(f'New list is [{A}]')

# Simpler version to remove 10
if 10 in A:
    A.remove(10)
print(f'Second list without 10 -> {A}')