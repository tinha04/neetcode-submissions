class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_store = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in values_store:
                return [values_store[complement], i]

            values_store[n] = i
