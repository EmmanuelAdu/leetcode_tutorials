"""
Solution for two sums using classes
"""
from typing import List



class TwoSum:
    def __init__(self, nums:List[int], target:int):
        self.nums = nums
        self.target = target
    
    def two_sums(self) -> List:
        for i in range(len(self.nums) - 1):
            if self.nums[i] + self.nums[i+1] == self.target:
                return [i, i+1]


obj = TwoSum([2, 8, 11, 7], 9)
print(obj.two_sums())