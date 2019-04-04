import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import tarfile
import io
import sys
import random
import pandas as pd

import commissions
import global_config

PANDAS_HEADER=['datetime','open','high','low','close','volume']

if sys.platform.startswith('win'):
    BASE_PATH = 'C:/Users/mcdof/Documents/'
else:
    if os.path.exists('/home/forrest/stock_data_drive'):
        BASE_PATH = '/home/forrest/stock_data_drive/otherdata/'
    else:
        BASE_PATH = '/media/forrest/769A17459A170173/Users/mcdof/Documents/'

if os.path.exists('/mnt/c/Users'):
    BASE_PATH='/mnt/c/Users/mcdof/Documents/otherdata/'



#STEVENS_FUTURES = [x for x in os.listdir(BASE_PATH + 'stevens_futures2/') if '1_FW' in x and not x.startswith('.')]
STEVENS_CHAIN_TYPE = 'FW'
STEVENS_MONTH_NUM  = '1'


STOCKS_BASE_PATH = BASE_PATH + 'kibot_data/stocks/daily'
FOREX_BASE_PATH = BASE_PATH + 'kibot_data/forex/360min'

def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in range(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in range(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths



def add_data(cerebro):
    #stevens_added_commissions = [x['name'] for x in commissions.STEVENS_COMMISSIONS ]
    #print(stevens_added_commissions)
    #stevens_added_commissions = list(set(stevens_added_commissions) - set(commissions.INDICIES) - set(commissions.VOLATILITY))
    #stevens_added_commissions = ['CME_ES']
    #print(STEVENS_FUTURES)

    files = get_files_by_file_size(STOCKS_BASE_PATH, reverse=True)
    files = files[:int(len(files)/2)]
    random.shuffle(files)
    files = files[:100]

    for txt in sorted(files):

        txt = os.path.join(BASE_PATH,'stevens_futures2',txt)
        df = pd.read_csv(txt)
        if 'steven' in txt:
            name = os.path.splitext(os.path.basename(txt))[0]
            name = name.replace(STEVENS_MONTH_NUM + '_' + STEVENS_CHAIN_TYPE,'')
            if name not in stevens_added_commissions:
                continue
            kwargs = {
                'name': name,
                'dtformat' : '%Y-%m-%d',
                'datetime':5,
                'open':6,
                'high':7,
                'low':8,
                'close':9,
                'volume':10,
                'openinterest':11,
            }

        elif 'daily' in txt and 'kibot' in txt:
            kwargs = {
                'dtformat' : '%m/%d/%Y',
                'name' : os.path.splitext(os.path.basename(txt))[0],
                'datetime' : 0,
                'time' : -1,
                'open' : 1,
                'high' : 2,
                'low' : 3,
                'close' : 4,
                'volume' : 5,
                'openinterest' : -6,
            }
        else:
            kwargs = {
                'dtformat' : '%m/%d/%Y',
                'tmformat' : '%H:%M',
                'name' : os.path.splitext(os.path.basename(txt))[0],
                'datetime' : 0,
                'time' : -1,
                'open' : 1,
                'high' : 2,
                'low' : 3,
                'close' : 4,
                'volume' : 5,
                'openinterest' : -6,
            }

        try:
            #this throws an error for some securities, so... skip!
            begin = df[df.columns[kwargs['datetime']]].iloc[0]
            end = df[df.columns[kwargs['datetime']]].iloc[-1]
        except:
            continue

        start_dt = datetime.datetime.strptime(begin,kwargs['dtformat'])
        end_dt = datetime.datetime.strptime(end,kwargs['dtformat'])
        delta = end_dt - start_dt
        #we're only allowing stocks that have been trading for > 2 years, plus a few days for fudge factor
        if delta.days < 750:
            print("skipping",kwargs['name'],"due to not enough trading date")
            continue
        print("adding", kwargs['name'])
        start_dt += datetime.timedelta(days=740)
        global_config.GLOBAL_DATAFRAMES_START_END[kwargs['name']] = (start_dt.date(), end_dt.date())

        #we still load all data since we want correct values say, 200 day MA, rather than only
        #1 day of it
        data = btfeed.GenericCSVData(
            dataname=txt,
            **kwargs,
            timeframe=bt.TimeFrame.Days,
            fromdate=datetime.datetime(1900, 1, 1),
            todate=datetime.datetime(2018, 12, 1),
            plot=False,
            preload=True,
            runonce=True,
            separator=',',
        )
        cerebro.adddata(data)
    print("dont loading data")
    #data has been loaded. let's precompute the number of trading securities
    for begin,end in global_config.GLOBAL_DATAFRAMES_START_END.values():
        delta = end - begin
        for i in range(delta.days + 1):
            d = begin + datetime.timedelta(i)
            global_config.GLOBAL_TRADING_SECURITIES[d] += 1
    for k,v in sorted(global_config.GLOBAL_TRADING_SECURITIES.items()):
        print(k,v)