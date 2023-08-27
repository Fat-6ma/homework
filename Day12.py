#21/8/2023
N=int(input("Enter the N= "))
def partition(Arr):
 
    j = 0
    pivot = 0   
 
    for i in range(len(Arr)):
        if Arr[i] < pivot:
            temp = Arr[i]
            Arr[i] = Arr[j]
            Arr[j] = temp
 
            j = j + 1
 
    return j
 
 
def rearrange(Arr):
 
    p = partition(Arr)
 
    n = 0
    while len(Arr) > p > n:
        temp = Arr[n]
        Arr[n] = Arr[p]
        Arr[p] = temp
 
        p = p + 1
        n = n + 2
 
 
if __name__ == '__main__':
 
    Arr = [9, -3, 5, -2, -8, -6, 1, 3]
 
    rearrange(Arr)
    print(Arr)  