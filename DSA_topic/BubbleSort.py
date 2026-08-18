def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 2, 4, 1]
bubble_sort(arr)
print(arr)

# Insertion Sort (Good for Small Lists)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

arr = [5, 3, 2, 4, 1]
insertion_sort(arr)
print(arr)