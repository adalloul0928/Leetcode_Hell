# simple binary search implementation

def binarySearch(A, L, R, S):
    if R >= L:
        mid = (L + R) // 2
        if A[mid] == S:
            return True
        if A[mid] > S:
            return binarySearch(A, L, mid-1, S)
        else:
            return binarySearch(A, mid+1, R, S)
    return False

array = [1,3,5,7,9,10,11]
L = 0
R = len(array) - 1
S = 1
print(binarySearch(array, L, R, S))