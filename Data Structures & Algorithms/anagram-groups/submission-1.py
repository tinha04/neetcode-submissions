class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            #Turns into a list which is mutabel so by doing ''.join it turns it into an immutable string used for dictionary key
            sorted_s = ''.join(sorted(s))
            result[sorted_s].append(s)

        return list(result.values())
