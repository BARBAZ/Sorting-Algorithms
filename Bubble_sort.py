
# Optimisation tests

# Data sets and array are defined  before chrono start 
# to only mesure computational time

# Modules

import time
import random

# Arrays

Dataset = []
Sorted_Array = []

# function definitions

def fill_list(items_numbers):
    for i in range(items_numbers):
        Dataset.append(random.randrange(0, 999999999))

# Variables 

loop = 1

fill_list(12000)
start = time.time() # Chrono start
comp_count = 0

## Algo ##

while(loop):
    index = -1
    Min = 10000000000
    Min_index = 0
    for i in range(len(Dataset)):
        index += 1
        Var = Dataset[i]
        comp_count += 1
        if(Var < Min):
            Min = Var
            Min_index = index
    Sorted_Array.append(Min)
    Dataset.pop(Min_index)
    if(len(Dataset) == 0):
        loop = 0

end = time.time() # Chrono stop

string = "Elapsed time :"
time = end - start
time = str(time)
tuple = (string, time)
log_time = "".join(tuple)
print log_time 
print comp_count
print "Comparisons"