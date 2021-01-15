class Solution:
    def moveZeroes(self, nums):
        insertIdx = 0
        for idx, val in enumerate(nums):
            if (val != 0):
                nums[insertIdx] = val
                insertIdx += 1
        while (insertIdx < len(nums)):
            nums[insertIdx] = 0
            insertIdx += 1
        print(nums)

solution = Solution()
solution.moveZeroes([0, 0, 1])