# imports
import math
import copy
from random import randint

# creates a random list with n integers from 0 to n
def createList(n):
   list = []
   i = 0
   while (i <= n):
      rand = randint(0, n)
      list.append(rand)
      i = i + 1
   return list

# creates a string of the list
def listToString(list):
   str = "["
   for e in list:
      str = str + " %d  " % e
   str = str + "]"
   return str

# prints list to console
def printList(list):
   print listToString(list)

# writes list into given file (appending)
def writeToFile(filename, list):
   file = open(filename, "ab")
   file.write(listToString(list))
   file.close()
