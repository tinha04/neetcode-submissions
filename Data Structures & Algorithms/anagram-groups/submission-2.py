class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            temp = ''.join(sorted(s))
            ans[temp].append(s)

        return list(ans.values())