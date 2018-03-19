def bubbleSort(unordered_list):
    iteration_number = len(unordered_list)-1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
    return unordered_list
   
