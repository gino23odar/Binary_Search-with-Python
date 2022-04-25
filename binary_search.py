import random
import time


# Implementation of a Binary Search algorithm with Python!

def binary_search(list, target_val, lowest=None, highest=None):

    if lowest is None:
        lowest = 0
    if highest is None:
        highest = len(list) - 1

    if highest < lowest:
        return -1

    center_value = (lowest + highest) // 2

    if list[center_value] == target_val:
        return center_value
    elif target_val < list[center_value]:
        return binary_search(list, target_val, lowest, center_value-1)
    else:
        return binary_search(list, target_val, center_value+1, highest)


if __name__ == '__main__':
    # list1 = [2, 5, 6, 7, 12, 16, 23, 31]
    # target_val = 12
    # print(binary_search(list1, target_val))

    # make a new list with a length of 2000, pre-sorted, in the range of -6000 and 6000
    sample_length = 2000
    sorted_list = set()
    while len(sorted_list) < sample_length:
        sorted_list.add(random.randint(-3 * sample_length, 3 * sample_length))
    sorted_list = sorted(list(sorted_list))
    print(sorted_list)

    # get the time needed to find the target
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    time_needed = end - start
    time_needed_per_iteration = time_needed / sample_length
    print("The search time is: ", time_needed, "seconds in total")
    print("The search time per iteration is: ", time_needed_per_iteration, "seconds")
