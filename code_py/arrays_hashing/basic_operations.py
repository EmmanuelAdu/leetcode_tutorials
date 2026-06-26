"""Data structures in python

Arrays Deep Dive with Big O Annotation
"""

#Printing an array of A
A = [1, 2, 4, 5]
print("A -> {}".format(A))

#Append an element at the end
A.append(7)
print(f"7 appended in array A -> {A}")

#Pop or Delete last element without index
A.pop()
print(f"Last element deleted A -> {A}")

#Pop or delete given an index
A.pop(1)
print(f"Index one deleted using pop with index A -> {A}")