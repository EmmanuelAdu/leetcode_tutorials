"""
Two Sum List
Returning the index of two numbers when sum is equal to the target
"""

nums = [2, 5, 8, 7, 4, 1]
target = 9
"""
i = 0
while i < len(nums) - 1:
    if nums[i] + nums[i+1] == target:
        print("[",i, i+1, "]")
    i +=1

for i in range(len(nums) - 1):
    if nums[i] + nums[i+1] == target:
        print("[", i," ," ,i+1,"]")

"""

i = 0
new_item = {}
while i < len(nums) - 1:
    j = i + 1
    while j < len(nums):
        if nums[i] + nums[j] == target:
            new_item[i] = j
        j += 1
    i += 1
    print(new_item)