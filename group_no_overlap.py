import pandas as pd
import numpy as np


def group_no_overlap(square, square_num=None, skip_num=0):

    num_in_group = pd.DataFrame()
    
    if square_num == None:
        square_num = int(np.sqrt(len(square)))
    
    #square['numbers'] = np.arange(int(square_num**2))
    num_in_group['num'] = np.zeros(len(square))
    
    #for i in list(square.index):
    #    square[f'{i}'] = np.zeros(len(square))
    
    groups = []
    
    for i in list(square.index):
        if num_in_group.at[i,'num'] < square_num: 
            #if true, person at index i needs more group members
    
            group = [i]
            #start new group for person at index i
    
            cols = [col for col in list(square.columns[1:]) if col != str(i)]
            #get cols to check excluding index i self col
    
            for col in cols:
    
                mems = square[square.index.isin(group)]                
                
                is_good_group = True
                if skip_num > 0:
                    is_good_group = False
                    skip_num -= 1

                
                if (not 1 in mems[col].values and num_in_group.at[int(col),'num']<square_num and is_good_group):
                #if persons in group have not been in a group with person at col    
                #AND person at col is not already in full group
                    print(f'i: {i}, col: {col}') 
                    group.append(int(col))
                    num_in_group.loc[num_in_group.index.isin(group),'num'] = len(group)
                        
                
                if num_in_group.at[i,'num'] < square_num:
                    pass
                else:
                    groups.append(group)
                    square.loc[square.index.isin(group),list(map(str,group))] = 1
                    break

    full_solution = num_in_group['num'].values == square_num

    if False in full_solution:
        print(square)
        return 1

    print(square)

    return 0

