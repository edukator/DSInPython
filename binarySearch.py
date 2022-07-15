# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:14:37 2021

@author: user
"""
def binary_search(input_array, value):
    lower=0
    upper=len(input_array)-1
    while(lower<=upper):
        mid=(lower+upper)//2
        
        
        if(input_array[mid]<value):
            lower=mid+1
            
        elif(input_array[mid]>value):
            upper=mid-1
        else:
            
            return mid
    return -1



test_list = [1,3,9,11,15,19,20,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list,29 ))

