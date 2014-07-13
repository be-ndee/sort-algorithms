__author__ = 'Lioman dev@lioman.de'


def divide(r_int, l_int, list):
    i = l_int
    j = r_int - 1
    p = list[r_int]
    print "Pivot: ", p
    while i < j:
        while list[i] <= p and i < r_int:
            i += 1
        while list[j] >= p and j > l_int:
            j -= 1
        if i < j:
            t = list[i]
            list[i] = list[j]
            list[j] = t

        if list[i] > p:
            t = list[i]
            list[i] = list[r_int]
            list[r_int] = t
    return i


def quick_sort(l_int, r_int, list):
    """
    Sorts a list with quick_sort algorithm
    :param l_int:
    :param r_int:
    :param list:
    :return:
    """
    if r_int > l_int:
        print(list)
        d_int = divide(r_int, l_int, list)
        quick_sort(l_int, d_int - 1, list)
        quick_sort(d_int + 1, r_int, list)
        t_int = list[l_int]
        list[l_int] = list[r_int]
        list[r_int] = list[t_int]