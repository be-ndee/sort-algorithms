# imports
import ../list_handling

# insert sort algorithm
def insert_sort(list):
   for i in range(1, len(list)):
      x = list[i]
      j = i
      while (j > 0 and list[j-1] > x):
         list[j] = list[j-1]
         j = j - 1
      list[j] = x
   return list
