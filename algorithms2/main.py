import numpy as np

new_array = []


def count_zeros(array):
    zero_count = 0
    for i in range(len(array)):
        if array[i] == 0:
            zero_count += 1
    return zero_count


def remove_zeros(array):
    for i in range(len(array)):
        if array[i] != 0:
            new_array.append(array[i])
    return new_array


def longest_sequence(array):
    array = sorted(array)
    zero_quantity = count_zeros(array)
    array = remove_zeros(array)

    counter = 1
    max_length = 0
    missed = 0

    for i in range(len(array)):
        if array[i] - array[i-1] == 1:
            counter += 1
        if array[i] - array[i - 1] > 1:
            if zero_quantity >= array[i] - array[i - 1] - 1:
                zero_quantity -= array[i] - array[i - 1] - 1
                counter += array[i] - array[i - 1]
                if missed == 0:
                    missed = i
            else:
                counter += zero_quantity
                zero_quantity = count_zeros(array)
                if counter >= max_length:
                    max_length = counter
                if missed != 0:
                    i = missed
                missed = 0
                counter = 1

    if zero_quantity != 0:
        counter += zero_quantity
    if counter > max_length:
        max_length = counter

    return max_length


data = np.genfromtxt('lngpok.in', delimiter=' ')
print(data)

print(longest_sequence(data))
