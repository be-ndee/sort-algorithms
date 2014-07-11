# imports
import math
import copy
from random import randint


def createList(n):
    """
    creates a random list with n integers from 0 to n
    :param n:
    :return:
    """
    list = []
    i = 0
    while (i <= n):
       rand = randint(0, n)
       list.append(rand)
       i = i + 1
    return list


def listToString(list):
    """
    creates a string of the list
    :param list:
    :return:
    """
    str = "["
    for e in list:
        str = str + " %d  " % e
    str = str + "]"
    return str


def printList(list):
    """
    prints list to console
    :param list:
    :return:
    """
    print listToString(list)


def writeToFile(filename, list):
    """
    writes list into given file (appending)
    :param filename:
    :param list:
    :return:
    """
    file = open(filename, "ab")
    file.write(listToString(list))
    file.close()
