'''Given an Array [6, 10, 12, 15]
Retrieve 12 from the list with its index
'''

A = [6, 12, 3, 15]

for idx, val in enumerate(A):
    if val == 12:
        print(f"The index of {val} is {idx}")
        break
else:
    print("The number you searching for is not available")