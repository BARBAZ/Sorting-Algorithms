
# Optimisation tests

# Data sets and array are defined  before chrono start 
# to mesure only computational time

# Modules

import time
import random

# Arrays

Dataset = []
Sorted_Array = []

# function definitions

def fill_list(items_numbers):
    for i in range(items_numbers):
        Dataset.append(random.randrange(0, 999999999)) # picks random values included between 0 - 999999999 and append it to an array

def Chrono_print(comp_cnt):
    string = "Elapsed time :"
    unit = ".s"
    string2 = " Comparisons"
    time = end - start
    time = str(time)
    comp_cnt = str(comp_cnt)
    tuple0 = (string, time, unit)
    tuple1 = (comp_cnt, string2)
    log_time = "".join(tuple0)
    log_comp = "".join(tuple1)
    print log_time 
    print log_comp
    

# Variables 

loop = 1
fill_list(7500) # sets the amount of randomally generated numbers here 7500 # we recommand values < 10000 #  be careful N^2 sorting times are exponenential !
comp_count = 0


start = time.time() # Chrono start

while(loop):
    index = -1
    Min = 1000000000 # Re init Var each cycle
    Min_index = 0 # Re init Var each cycle
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

Chrono_print(comp_count)