from random import randint
import time


def binary_search(element, array, start, end):
    """
    Search element within array using binary search (if the element is found return index otherwise -1)
    :param element:
    :param array:
    :param start:
    :param end:
    :return:
    """
    if start <= end:
        middle = int((start + end) / 2)
        if array[middle] == element:
            return middle
        else:
            if element < array[middle]:
                return binary_search(element, array, start, middle - 1)
            else:
                return binary_search(element, array, middle + 1, end)
    else:
        return -1


def binary_search_randomized(element, array, start, end):
    """
    Search element within array using randomized binary search (if the element is found return index otherwise -1)
    :param element:
    :param array:
    :param start:
    :param end:
    :return:
    """
    if start <= end:
        middle = randint(start, end)
        if array[middle] == element:
            return middle
        else:
            if element < array[middle]:
                return binary_search_randomized(element, array, start, middle - 1)
            else:
                return binary_search_randomized(element, array, middle + 1, end)
    else:
        return -1


def create_arrays(size, minimum, members_limit, non_members_limit):
    """
    Generate array and elements to search (members and non members)
    :param size:
    :param minimum:
    :param members_limit:
    :param non_members_limit:
    :return:
    """
    array_local = []
    members_local = []
    non_members_local = []

    array_count = 0
    members_count = 0
    non_members_count = 0

    number = minimum

    member_step = int(size / 700)

    while array_count < size:
        if randint(0, 1):
            array_local.append(number)
            if members_count < members_limit and array_count % member_step == 0:
                members_local.append(number)
                members_count += 1
            array_count += 1
        else:
            non_members_local.append(number)
            non_members_count += 1
        number += 1

    if non_members_count < non_members_limit:
        while non_members_local < non_members_limit:
            if randint(0, 1):
                non_members_local.append(number)
                non_members_count += 1
            number += 1
    else:
        non_members_local = non_members_local[0:non_members_limit]

    return array_local, members_local, non_members_local


for k in [5, 6, 7]:

    array_size = 10 ** k

    print("Test for element size: 10^" + str(k))

    array, members, non_members = create_arrays(array_size, 1, 700, 300)

    start_time = time.time()

    for e in members:
        binary_search(e, array, 0, array_size - 1)

    for e in non_members:
        binary_search(e, array, 0, array_size - 1)

    end_time = time.time()

    print("Time elapsed (Binary Search): " + str(int(1000 * (end_time - start_time))) + " microseconds")

    start_time = time.time()

    for e in members:
        binary_search_randomized(e, array, 0, array_size - 1)

    for e in non_members:
        binary_search_randomized(e, array, 0, array_size - 1)

    end_time = time.time()

    print("Time elapsed (Binary Search Randomized): " + str(int(1000 * (end_time - start_time))) + " microseconds\n")
