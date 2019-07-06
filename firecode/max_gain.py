'''
Given an list of integers, write a method - max_gain - that returns the maximum gain. 
Maximum Gain is defined as the maximum difference between 2 elements in a list,
such that the larger element appears after the smaller element.
If no gain is possible, return 0.

Example:
max_gain([100,40,20,10]) ==> 0
max_gain([0,50,10,100,30]) ==> 100
'''

def max_gain(input_list):
    max_so_far, minimum = 0, input_list[0]
    for num in input_list:
        minimum, max_so_far = num if num < minimum else minimum, num - minimum if num - minimum > max_so_far else max_so_far
    return max_so_far