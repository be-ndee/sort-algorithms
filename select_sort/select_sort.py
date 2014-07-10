# imports
import list_handling

# sorts the list with selection
def select_sort(list):
   for i in range(0, len(list)-1):
      writeToFile("select_sort.txt", list)
      k = i
      for j in range(i+1, len(list)):
         if (list[j] < list[k]):
            k = j
      list[i], list[k] = list[k], list[i]
   return list
