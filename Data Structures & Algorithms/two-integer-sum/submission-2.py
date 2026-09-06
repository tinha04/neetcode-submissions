class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in tempMap:
                return [tempMap[complement], i]
            tempMap[num] = i

        return []