# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:46:03 2021

@author: user

"""


def  perform_swap(arr,idx1,idx2):
                temp=arr[idx2]
                arr[idx2]=arr[idx1]
                arr[idx1]=temp




def quick_sort(array):
    # base  case:
    if(len(array)<=1):
        return array

    pivot_idx=len(array)-1
    
    pivot=array[pivot_idx]
    #print(pivot_idx,pivot)
    idx=0
    while(idx<pivot_idx):
        if(array[idx]>pivot):
            perform_swap(array, idx, pivot_idx-1)
            perform_swap(array,pivot_idx,pivot_idx-1)
            pivot_idx-=1
            if(array[idx]>pivot): # swap ettiğin eleman  küçükse??? 
                idx-=1

            
        idx+=1
    
    # here pivot element is in the right place
    # apply the same proc before  pivot
    left=quick_sort(array[:pivot_idx])
    #print(left)
    right=quick_sort(array[pivot_idx+1:])
    #print(right)
    return left+[pivot]+right
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test=[ 10, 7, 8, 9, 1, 5 ]
print(quick_sort(test))



########:Geek  for geeeks   solution

def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort 
def quick_sort(start, end, array):
      
    if (start < end):
          
        # p is partitioning index, array[p] 
        # is at right place
        p = partition(start, end, array)
          
        # Sort elements before partition 
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
          
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)
  
print(f'Sorted array: {array}')
      
# This code is contributed by Adnan Aliakbar




