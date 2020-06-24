import pandas as pd
import numpy as np

square = pd.DataFrame()
num_in_group = pd.DataFrame()

square_num = 4

square['numbers'] = np.arange(int(square_num**2))
num_in_group['num'] = np.zeros(len(square))

for i in list(square.index):
    square[f'{i}'] = np.zeros(len(square))


groups = []


for i in list(square.index):
    if num_in_group.at[i,'num'] < square_num: 
        #if true, person at index i needs more group members
        print(f'{i} num_in_group: {num_in_group.at[i,"num"]}')
        #if true, num in group should always be 0. I think...

        group = [i]
        #start new group for person at index i

        cols = [col for col in list(square.columns[1:]) if col != str(i)]
        #get cols to check excluding index i self col

        for col in cols:
            if num_in_group.at[i,'num'] < square_num: 
                if square.at[i,col] == 0:
                #if person at index i has not been in a group with person at col    
                #NOT JUST PERSON AT INDEX I, NEED TO CHECK FOR ALL PERSONS IN GROUP
                    
                    group.append(int(col))
                    num_in_group.loc[num_in_group.index.isin(group),'num'] = len(group)

print(num_in_group)
                













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

