#17/8/2023
def check_elements_in_range(arr, n, A, B):
    if A > B:
        return False  
    for i in range(A, B+1):
        found = False
        for j in range(n):
            if arr[j] == i:
                found = True
                break
        if not found:
            return False  
    return True  
 
 
arr = [1, 4, 5, 2, 7, 8, 3]
n = len(arr)
A, B = 2, 5
if check_elements_in_range(arr, n, A, B):
    print("Yes")
else:
    print("No")