__author__ = 'Lioman dev@lioman.de'
# import list_handling


def bubble_sort(list):
    """
    Sorts a list with the bubble sort algorithm
    :param list:
    :return:
    """
    for i in range(1, len(list) - 1):
        for j in range(len(list) - 1, i-1, -1):
            if list[j - 1] > list[j]:
                x = list[j]
                list[j] = list[j - 1]
                list[j - 1] = x
    return list
