def bubble_sort2():
  arr = [5,4,1,6,3,2,7]
  for i in range(len(arr)):
      for j in range(0, len(arr)-i-1):
          if arr[j] > arr[j + 1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
  print("This is bubble sort ", arr)
