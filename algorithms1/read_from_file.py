from Park import Park


def read_from_file(file):
    with open(file) as f:
        parks_list = []
        for line in f:
            arr = line.split(",")
            parks_list.append(Park(arr[0], arr[1], arr[2]))
        return parks_list
