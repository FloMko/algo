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
