class Solution:
  def rotate(self, nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
      nums.insert(0, nums[len(nums) - 1])
      nums.pop(len(nums) - 1)
        