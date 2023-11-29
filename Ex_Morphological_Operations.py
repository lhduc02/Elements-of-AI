"""
You are provided the following image B
    0000000000
    0111111100
    0000111100
    0000111100
    0001111100
    0000111100
    0001100000
    0000000000
    0000000000
The structuring element S is given below, and its' origin is the middle pixel.
    111
    111
    111
1. What is the total number of pixels marked 1 in the image obtained after B is opened with the structuring element S?
2. What is the total number of pixels marked 1 in the image obtained after B is closed with the structuring element S?
3. After B is dilated with the structuring element S, what is the number of pixels marked 1 obtained in the image?
4. What is the number of pixels marked 1 in the image obtained after B is eroded with the structuring element S?
"""

import numpy as np
from skimage.morphology import erosion, dilation, closing, opening

a = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
])

s = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]])
# 1
unique, freq = np.unique(opening(a,s), return_counts=True)
print("opening", freq[1])

# 2
"""
unique, freq = np.unique(closing(a,s), return_counts=True)
print("closing", freq[1])
"""

#3
unique, freq = np.unique(dilation(a,s), return_counts=True)
print("dilation", freq[1])

#4
unique, freq = np.unique(erosion(a,s), return_counts=True)
print("erosion", freq[1])
