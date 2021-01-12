class Solution:
    def rotate(self, matrix):
        for idx, col in enumerate(zip(*matrix)):
            matrix[idx] = list(reversed(col))
        print(matrix)
    
solution = Solution()
solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
arr = [1, 2, 3]
for i in range(len(arr) - 1):
    arr[i + 1] = 0
    print(arr[i])