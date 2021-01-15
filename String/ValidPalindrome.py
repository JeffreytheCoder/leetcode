class Solution:
    def isPalindrome(self, s):
        s = ''.join(char for char in s.lower() if char.isalnum())
        for s_idx in range(len(s) // 2):
            print("first %s last %s" % (s[s_idx], s[len(s) - s_idx - 1]))
            if (s[s_idx] != s[len(s) - s_idx - 1]):
                return False
        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print("test wakatime")