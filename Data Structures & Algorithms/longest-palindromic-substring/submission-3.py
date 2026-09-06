class Solution:
    def longestPalindrome(self, s: str) -> str:
        range_index = 0
        length_pal = 0

        for i in range(len(s)):
            #odd
            l, r = i,i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > length_pal:
                    length_pal = r -l + 1
                    range_index = l
                l -= 1
                r += 1

            #even
            l, r = i,i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > length_pal:
                    length_pal = r -l + 1
                    range_index = l
                l -= 1
                r += 1

        return s[range_index : range_index + length_pal]

            
