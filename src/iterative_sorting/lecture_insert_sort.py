# Insertion sort


def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i
        while j > 0 and temp < list[j - 1]:
            list[j] = list[j - 1]
            j -= 1
            list[j] = temp
    return list


l = list(range(100))
import random
random.shuffle(l)
print(l)

print()

insertion_sort(l)
print(l)
