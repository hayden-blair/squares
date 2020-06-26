import pandas as pd
import numpy as np
import group_no_overlap as group

square = pd.DataFrame()

square['numbers'] = np.arange(25)

for i in square.index:
    square[f'{i}'] = np.zeros(len(square))

prev_bad_groups = False
skip_num = 0

while(True):

    prev_state_square = square.copy()

    if prev_bad_groups:
        result = group.group_no_overlap(square,skip_num = skip_num)
    else:
        result = group.group_no_overlap(square)

    if result == 0:
        prev_bad_groups = False
        skip_num = 0
    else:
        prev_bad_groups = True
        skip_num += 1
        square = prev_state_square
        print(f'skip_num: {skip_num}')
    
    if 0 not in square[square.columns[1:]].values:
        print('Did it!')
        break
    elif skip_num == len(square):
        print("Couldn't do it...")
        break

"""
while(True):
    answer = input("Run? y or n")

    if answer == 'y':
        if prev_bad_groups:
            result = group.group_no_overlap(square,skip_num = skip_num)
        else:
            result = group.group_no_overlap(square)

        if result == 0:
            prev_bad_groups = False
            skip_num = 0
        else:
            prev_bad_groups = True
            skip_num += 1

    elif answer == 'p':
        print(skip_num)

    else:
        break
"""
