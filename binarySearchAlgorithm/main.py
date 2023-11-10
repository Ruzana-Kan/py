#binary searh algorithm for posiive value
def binary_search(arr, target):
  low, high = 0, len(arr) - 1

  while low <= high:
      mid = (low + high) // 2
      mid_value = arr[mid]
     
    # Found the target, return its index
      if mid_value == target:
          return mid 
    # Search the right half
      elif mid_value < target:
          low = mid + 1  
    # Search the left half
      else:
          high = mid - 1  
  # Target not found in the array
  return -1  


my_list = [70,22,44,87,91,71,35,76]
target_value = 22

result = binary_search(my_list, target_value)



if result != -1:
  print(f"Element {target_value} is present at index {result}.")
else:
  print(f"Element {target_value} is not present in the array.")
