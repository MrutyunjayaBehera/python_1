#TASK

Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

#CODE

import math
import os
import random
import re
import sys


n = input("enter the number: ")
n = int(n)
for i in range(1,n+1):
    print(i, end = "")
