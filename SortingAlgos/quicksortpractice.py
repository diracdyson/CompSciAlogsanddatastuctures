import numpy as np
  2 def partition(array,low,high):
  3     pivot = array[high]
  4     i = low - 1
  5     for j in range(low, high):
  6         if array[j] <= pivot:
  7 
  8             i = i + 1
  9 
 10             array[i], array[j] = array[j], array[i]
 11 
 12     array[i+1], array[high] = array[high], array[i+1]
 13 
 14     return i + 1
 15 #simple recursion based quicksort
 16 
 17 def quickSort(array,low,high):
 18     if low < high:
 19 
 20         pi = partition(array, low, high)
 21 
 22         quickSort(array, low, pi - 1)
 23 
 24         quickSort(array, pi + 1, high)
 25 da= [5,6,10,19,7,8,9]
 26 size = len(da)
 27 quickSort(da,0,size -1)
