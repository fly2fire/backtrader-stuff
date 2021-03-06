import numpy as np
import pandas as pd
import tempfile
import datetime
import os

COLUMNS = ["Date","Time","Open","High","Low","Close","Volume"]

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def resample_dataframe(df, period):
    ret = []
    #prev_date = datetime.datetime(0,0,0,0,0,0,0)
    for chunk in chunks(df,period):
        ret.append([chunk.iloc[0]["Date"],
               chunk.iloc[0]["Time"],
               chunk.iloc[0]["Open"],
               max(chunk["High"]),
               min(chunk["Low"]),
               chunk.iloc[-1]["Close"],
               sum(chunk['Volume'])])

    ret = pd.DataFrame(ret,columns=COLUMNS)
    return ret

def resample_dataframe2(df,period):
    ret = []
    cur_line = ["01/01/0000","00:00",0.0,0.0,0.0,0.0,0]
    prev_line = ["01/01/0000","00:00",0.0,0.0,0.0,0.0,0]
    for thing in df.iterrows():
        d = thing[1].Date
        t = thing[1].Time
        o = thing[1].Open
        h = thing[1].High
        l = thing[1].Low
        c = thing[1].Close
        v = thing[1].Volume

        print(d,t,o,h,l,c,v)

base_path = "/media/forrest/769A17459A170173/Users/mcdof/Documents/kibot_data/forex/"
for csv in os.listdir(os.path.join(base_path,'120min')):
    print("processing",csv)
    csv_path = os.path.join(base_path,'120min',csv)
    df = pd.read_csv(csv_path,dtype={"Date":np.str,"Time":np.str},engine='c')
    resampled = resample_dataframe(df,2)
    resampled.to_csv(os.path.join(base_path,'240min',csv), index=False,)
