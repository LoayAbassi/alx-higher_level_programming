#!/usr/bin/python3
"""a peak finding algorithm"""
def find_peak(list_of_integers=[]):
    """finds a peak in a list of unsorted integers using a binary search """
    if not list_of_integers:
        return None  

    if len(list_of_integers) == 1:
        return list_of_integers[0]  

    if len(list_of_integers) == 2:
        return max(list_of_integers)  

    
    mid = len(list_of_integers) // 2
    left_peak = find_peak(list_of_integers[:mid]) 
    right_peak = find_peak(list_of_integers[mid:])  
    return max(left_peak, right_peak) 
