#22/8/2023
def subsetSums(arr, l, r, sum=0):

    if l > r:
        print(sum, end=" ")
        return

    subsetSums(arr, l + 1, r, sum + arr[l])
 
    subsetSums(arr, l + 1, r, sum)
 
arr = [5,4,3]
n = len(arr)
subsetSums(arr, 0, n - 1)