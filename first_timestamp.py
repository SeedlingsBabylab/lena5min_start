import sys

import os
from pathlib import Path
import pandas as pd
import re
import csv

def find_timestamp(f):
    """extract the first item of 'Timestamp'"""
    with open(f) as csvDataFile:
        csvReader = csv.reader(csvDataFile,quotechar='"')
        rownum = 0    
        for row in csvReader:
            if rownum == 0:
                col_ind = row.index('Timestamp')
            elif rownum == 1:
                res = row[col_ind]  # only the first row
            rownum+=1
    return(res)


def first_timestamp(rootdir,savedir):
    """Given a directory, extract all files' names, and their first "Timestamp" values, and save as a csv file"""
    
    # all files' addresses
    rootdir1 = Path(rootdir)
    file_list = [f for f in rootdir1.glob('**/*') if f.is_file()]
    
    # all files' names
    name = re.compile(r'.*\/(.+)?\.csv')
    df_all = []
    
    # Extract file name, and the first value in the "Timestamp" column
    for path in file_list:
        f = str(path)
        x = name.findall(f)
        x.append(find_timestamp(f))
        df_all.append(x)
        
    df_all1 = pd.DataFrame(df_all)
    df_all1.columns = ['file', 'Timestamp']
    
    # save as csv
    df_all1.to_csv(savedir +"/Timestamp.csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        first_timestamp(sys.argv[1],sys.argv[2])
    else:
        print("usage: first_timestamp(rootdir,savedir)")