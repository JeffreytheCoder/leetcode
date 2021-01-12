class Solution:
    def plusOne(self, digits):
        print("now digits is: " + str(digits))
        if (digits[len(digits) - 1] == 9):
            if (len(digits) == 1):
                return [1, 0]
            digits = self.plusOne(digits[:len(digits) - 1]) + [0]
        else:
            digits[len(digits) - 1] = digits[len(digits) - 1] + 1
        return digits
      
solution = Solution()
print(solution.plusOne([9, 9, 9]))