import pandas as pd
import numpy as np
import group_no_overlap as group

square = pd.DataFrame()

square['numbers'] = np.arange(16)

for i in square.index:
    square[f'{i}'] = np.zeros(len(square))

while(True):
    answer = input("Run? y or n")

    if answer == 'y':
        group.group_no_overlap(square)
    elif answer == 'yd':
        group.group_no_overlap(square,DEV_MODE = True)

    else:
        break

