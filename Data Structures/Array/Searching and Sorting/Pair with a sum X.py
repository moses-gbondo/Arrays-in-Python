# Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a C program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S 
# whose sum is exactly x.
# Method 1 using sorting
def two_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == target:
            return arr[left], arr[right]
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

# Method 2 using double loops

def two_sum_loops(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == target:
                    print(arr[i], arr[j])
                    return (arr[i],arr[j])

def two_sum_setHashing(arr, target):
    s = set()
    for i in range(len(arr)):
        if target - arr[i] in s:
            return True
        else:
            s.add(arr[i])

def main():
    arr = [1, 4, 45, 6, 10, -8]
    target = 16
    print(two_sum(arr, target))
    two_sum_loops(arr, target)
    print(two_sum_setHashing(arr, target))

main()
