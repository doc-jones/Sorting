# TO-DO: Complete the selection_sort() function below


def findSmallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:  # compare next value to smallest value
            smallest = arr[i]  # value
            smallest_index = i  # index
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Find smallest element in arr
        new_arr.append(arr.pop(smallest))  # and add to new_arr
        new_arr = arr
    return arr


# print(selection_sort([5, 3, 6, 2, 10]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
