#! /usr/bin/env python
# -*- coding: ASCII -*-

import numpy as np
count = 0
data = []
with open("/Users/vladimirskobcov/Desktop/lab/lab_parallel_prog/lab_1/parallel/parallel/input_f.txt") as f:
    for line in f:
        if(count != 0):
            data.append([int(x) for x in line.split()])
        count = count + 1

data = np.array(data)

data1 = []
count1 = 0
with open("/Users/vladimirskobcov/Desktop/lab/lab_parallel_prog/lab_1/parallel/parallel/input_s.txt") as f1:
    for line1 in f1:
        if(count1 != 0):
            data1.append([int(x) for x in line1.split()])
        count1 = count1 + 1

data1 = np.array(data1)

total = data.dot(data1)
print(total)
