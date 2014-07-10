# imports
import list_handling

# this function sorts the list with bubblesort
def bubble_sort(list):
   for i in range(1, len(list)):
      rangeDown = range(i, len(list))
      for j in rangeDown.reverse():
         if (list[j-1] > list[j]):
            list[j], list[j-1] = list[j-1], list[j]
   return list
