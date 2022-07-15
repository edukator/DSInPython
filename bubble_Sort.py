# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:21:45 2021

@author: user
"""
def buble_sort(array):
    N=len(array)
    for upper_idx in range(N-1,0,-1):  #  alt ve süt sınırlara  dikkat
        
        for idx in range(upper_idx):
            
            if(array[idx] > array[idx+1] ):
                temp=array[idx+1]
                array[idx+1]=array[idx]
                array[idx]=temp
        print("it :", N-upper_idx)
        print("possibly unordered   ", array[:upper_idx],end="--")
        print("surely ordered   ",array[upper_idx:])
def main():
    
    array=[21,4,6,3,9,20,25,6,21,14,1]
    buble_sort(array)
    print(array)
    
main()

        
        
        