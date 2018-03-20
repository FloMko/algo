def bubbleSort(unordered_list):
    iteration_number = len(unordered_list)-1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
    return unordered_list


def insertionSort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index -1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
            unsorted_list[search_index] = insert_value
    return unsorted_list


def selectionSort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
    return unsorted_list


def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and \
        greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and \
        less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] =  \
            unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index

def quickSort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quickSort(unsorted_array, first, partition_point-1)
        quickSort(unsorted_array, partition_point+1, last)
    print(unsorted_array)
