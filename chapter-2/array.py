from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
floats2 = array('d')

with open('floats.bin', 'wb') as file:
    floats.tofile(file)

with open('floats.bin', 'r') as file:
    floats2.fromfile(file, 10**7)
