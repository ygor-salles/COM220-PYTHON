from random import randint
import time
import timeit

#FUNÇÃO BUBBLESORT
def bubbleSort(array2):
    for i in range(len(array2)-1):
        for j in range(len(array2)-1):
            if array2[j]>array2[j+1]:
                array2[j], array2[j+1] = array2[j+1], array2[j]  

#FUNÇÃO QUICKSORT
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]           
        else:
            break
        
    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
                
#FUNÇÃO PRINCIPAL
array = []
for i in range(10000):
    array.append(randint(1, 10000))
inicioQuick = timeit.default_timer()
quick_sort(array, 0, len(array)-1)
fimQuick = timeit.default_timer()
print('\n\nTempo do QuickSort: %f' % (fimQuick - inicioQuick)+' Segundos')

array2 = []
for i in range(10000):
    array2.append(randint(1, 10000))
inicioBubble = timeit.default_timer()
bubbleSort(array2)
fimBubble = timeit.default_timer()
print('Tempo do BubbleSort: %f' % (fimBubble - inicioBubble)+' Segundos\n\n')
