import pandas as pd
import numpy as np


def group_no_overlap(square, DEV_MODE=False):

    num_in_group = pd.DataFrame()
    
    #square_num = int(np.sqrt(len(square)))
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
                
                if (not 1 in mems[col].values and num_in_group.at[int(col),'num']<square_num):
                #if persons in group have not been in a group with person at col    
                #AND person at col is not already in full group
                    
                    group.append(int(col))
                    num_in_group.loc[num_in_group.index.isin(group),'num'] = len(group)
                        
                
                if num_in_group.at[i,'num'] < square_num:
                    pass
                else:
                    groups.append(group)
                    square.loc[square.index.isin(group),list(map(str,group))] = 1
                    break

    print(square)
        
    
    print(num_in_group)
    print(groups)

    return 0
                













"""
for i in list(df.index):
    group = [str(i)]
    line = df[df.index == i]
    cols = [col for col in list(line.columns[1:]) if(col != f'{i}' and '_' not in col)]
    for col in cols:
        if df.at[i,f'{i}_num_in_group'] < square:
            if df.at[i,col] == 0:
                group.append(col)
                for j in group:
                    mems = [mem for mem in group if mem != j]
                    df.loc[df.index == int(j), mems] = 1
                    df.loc[j+'_num_in_group'] = len(group)
"""                

