"""
Two Sum List
Returning the index of two numbers when sum is equal to the target
"""

nums = [3,3]
target = 6

i = 0
while i < len(nums) - 1:
    if nums[i] + nums[i+1] == target:
        print("[",i, i+1, "]")
    i +=1

for i in range(len(nums) - 1):
    if nums[i] + nums[i+1] == target:
        print("[", i," ," ,i+1,"]")