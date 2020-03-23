def binSearch(A, l, r, target):
    mid = (l + r) // 2
    if l <= r:
        if target == A[mid]:
            return mid
        if target <= A[mid]:
            return binSearch(A, l, mid-1, target)
        else:
            return binSearch(A, mid+1, r, target)
    return -1

def binSearchIterative(A, l, r, target):
    while l <= r:
        mid = l + (r-l)//2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def mergeSort()

A = [1,5,9,10,11,14,15,19,20]
target = 20
# print(binSearch(A,0,len(A)-1, target))
print(binSearchIterative(A, 0, len(A)-1, target))