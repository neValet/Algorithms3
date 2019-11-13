import sorting
import read_from_file
import time

parks_list = read_from_file.read_from_file("info.txt")

startTime = time.time()
print("Bubble sort:")
sorting.bubble_sort(parks_list)
print("Time: ", time.time() - startTime, "\nResult: ")
for i in parks_list:
    print(i, "\n")

sorting.check_sorted(parks_list)

startTime = time.time()
print("Quick sort:")
if not sorting.check_sorted(parks_list):
    sorting.quick_sort(parks_list)
print("Time: ", time.time() - startTime, "\nResult: ")
for i in parks_list:
    print(i, "\n")
