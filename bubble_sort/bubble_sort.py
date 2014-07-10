__author__ = 'Lioman dev@lioman.de'
# import list_handling

# bubble sort algorithm
listi = [4, 5, 6, 2, 1, 89, 88, 3, 5635, 44, 2, 2, 44, 546, 454]


def bubble_sort(list):
    for i in range(1, len(list) - 1):
        for j in range(len(list) - 1, i-1, -1):
            if list[j - 1] > list[j]:
                x = list[j]
                list[j] = list[j - 1]
                list[j - 1] = x
    return list
