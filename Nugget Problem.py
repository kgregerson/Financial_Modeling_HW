# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:31:06 2016

@author: kyle
"""

candidate = 6
in_a_row = 0
largest = 0

def is_nugget_number(candidate):
    for i in range(0,candidate):
        for j in range(0, candidate):
            for k in range(0,candidate):
                if (i*6+j*9+k*20) == candidate:
                    return True
    return False

while in_a_row < 7:
    if is_nugget_number(candidate) == True:
        in_a_row += 1
    if is_nugget_number(candidate) == False:
        largest = candidate
        in_a_row = 0
    candidate += 1
    

print("The largest number is", largest)
    
                   
        