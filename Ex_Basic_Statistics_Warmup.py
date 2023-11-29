"""
You are given an array of N integers separated by spaces, all in one line.

Display the following:

1. Mean (m): The average of all the integers.
2. Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.
3. Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.
4. Standard Deviation (SD)
SD = (  ( (x1-m)^2 + (x2-m)^2 + (x3-m)^2+ ... + (xN-m)^2) ) / N  )^0.5
where xi is the ith element of the array
5. Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space.

Input Format:
    The first line contains the number of integers.
    The second line contains space separated integers for which you need to find the mean, median, mode, standard deviation and confidence interval boundaries.

Constraints:
    10 <= N <= 2500
    0 < xi <= 105

Output Format:
    A total of five lines are required

Note:
    Use the constant 1.96 while computing the confidence interval.

Imput Sample:
    10
    64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
Output Sample:
    43900.6
    44627.5
    4978
    30466.9
    25017.0 62784.2
"""

import math
import numpy as np
from scipy import stats as st

n = int(input())
arr = np.array([int(i) for i in input().split()])
mean = round(np.mean(arr), 1)
print(mean)

median = round(np.median(arr), 1)
print(median)

mod = st.mode(arr)
print(min(mod[0]))

sd = round(np.std(arr), 1)
print(sd)

min_clt = mean - 1.96*sd/math.sqrt(n)
max_clt = mean + 1.96*sd/math.sqrt(n)
print(round(min_clt, 1), round(max_clt, 1))
