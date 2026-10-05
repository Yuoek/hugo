import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# 本地测试
if __name__ == "__main__":
    obj = Solution([1,2,3])
    print(obj.shuffle())
    print(obj.reset())
    print(obj.shuffle())
