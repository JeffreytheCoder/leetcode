def oldDuplicateZeros(arr):
    i = 0
    while i < len(arr):
        if (arr[i] == 0):
            j = len(arr) - 1
            while j != i:
                arr[j] = arr[j - 1]
                j -= 1
            i += 1
        i += 1
        
def duplicateZeros(arr):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0

arr = [1,0,2,3,0,4,5,0]
print(arr)
duplicateZeros(arr)
print(arr)
arr = [0,0,0,0,0,0,0]
print(arr)
duplicateZeros(arr)
print(arr)