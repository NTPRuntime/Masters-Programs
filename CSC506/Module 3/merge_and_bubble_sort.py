import time
import random

class Sorting_Algorithms:
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Sorting_Algorithms.merge_sort(L)
            Sorting_Algorithms.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


unsorted_array = []
for _ in range(1000):
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(1990, 2025)
    birthday = f"{year}{month :02d}{day :02d}"
    unsorted_array.append(int(birthday))
sorted_array_merge = unsorted_array.copy()
sorted_array_bubble = unsorted_array.copy()
# print("Unsorted array:", unsorted_array)

start_time = time.time()
Sorting_Algorithms.merge_sort(sorted_array_merge)
end_time = time.time()
print(f"Sorted array using Merge Sort: {sorted_array_merge} in {end_time - start_time:.6f} seconds\n")

start_time = time.time()
Sorting_Algorithms.bubble_sort(sorted_array_bubble)
end_time = time.time()
print(f"Sorted array using Bubble Sort: {sorted_array_bubble} in {end_time - start_time:.6f} seconds\n")