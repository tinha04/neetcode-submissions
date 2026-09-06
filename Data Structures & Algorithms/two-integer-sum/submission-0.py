class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in tempMap:
                return [tempMap[complement], i]
            tempMap[n] = i