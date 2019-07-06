'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
'''

from math import log
def reverse(x):
    pos = True
    if x < 0:
        pos = False
    x = abs(x)
    places = int(log(x,10))
    tot = 0
    for i in range(places, -1, -1):
        tot += (x % 10) * 10 ** i
        x = x // 10
    return tot if pos else -tot

print(reverse(0))