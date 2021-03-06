#!/usr/bin/python

"""
Python Core object Types
"""

import numpy as np


#### arr: 		the input array
#### nRow: 		the # of row in the reformed array
#### nCol: 		the # of column in the reformed array
#### new_arr:	the new reformed array as the output
#### reform the array to a new array with size(nRow,nCol)
def reform_array_dimension_col_wise(arr, nRow, nCol):
	new_arr = np.reshape(arr,(nRow, nCol)) # write your code here
	return new_arr


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### stack the column summation below the bottom of the array
def append_sum_of_array(arr):
	new_arr = np.vstack((arr, np.sum(arr,axis=0))) # write your code here
	return new_arr 


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### delete the top row and ending column from the array
def remove_topRow_endCol_from_array(arr):
	new_arr = np.delete(np.delete(arr,0,axis=0),-1,axis=1)# write your code here
	return new_arr

#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### calculate the product of each row and append to the array, use row_product to save the product value and add to the new array
def add_row_product_to_array(arr):
	row_product = np.prod(arr,axis=1)# write your code here
	new_arr = np.hstack((arr,row_product.reshape(3,1)))# write your code here
	return new_arr









