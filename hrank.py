import math
import os
import random
import re
import sys


"""n = input("enter the  number: ")
n = int(n)

if n % 2 != 0:
	print("Weird")
else:
	if n > 2 and n < 5:
		print("Not Weird")
	elif n > 6 and n < 20:
		print("Weird")
	elif n > 20:
		print("Not Weird")"""

n = input("enter the number: ")
n = int(n)
for i in range(1,n+1):
    print(i, end = "")