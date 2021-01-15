class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for s_val in s:
            if d1.get(s_val) == None:
                d1[s_val] = 1
            else:
                d1[s_val] += 1
        for t_val in t:
            if d2.get(t_val) == None:
                d2[t_val] = 1
            else:
                d2[t_val] += 1
        return d1 == d2