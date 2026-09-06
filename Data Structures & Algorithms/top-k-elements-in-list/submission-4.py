class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        temp = []
        for num, cnt  in freq.items():
            temp.append([cnt, num])
        temp.sort()

        ans = []
        while len(ans) < k:
            ans.append(temp.pop()[1])
        return ans