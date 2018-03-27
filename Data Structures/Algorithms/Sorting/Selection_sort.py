#Selection sort is O(n^2) and selects the minimum element index and swaps it.
def selection_sort(arr):
  for i in range(len(arr)):
    min_indx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_indx]:
        min_indx = j
    arr[i], arr[min_indx], = arr[min_indx], arr[i]
    
def main():
    arr = [64, 25, 12, 22 ,11, -1, 4, 9]
    selection_sort(arr)
main()
