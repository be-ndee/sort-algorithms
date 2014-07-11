# imports
import list_handling


def insert_sort(list):
    """
    sorts a list with insert sort algorithm
    :param list:
    :return:
    """
    for i in range(1, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x
    return list
