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
    BASE_PATH = '/media/forrest/769A17459A170173/Users/mcdof/Documents/'

FOREX_FUTURES = [
    BASE_PATH + 'kibot_data/cont_futures/60min/JY.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/BP.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/CD.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/NE.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/AD.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/SF.txt',
    BASE_PATH + 'kibot_data/cont_futures/60min/PX.txt',
]

CLC_FUTURES_DAILIES = [

'/home/forrest/daily_futures/AD_REV.CSV',
'/home/forrest/daily_futures/AN_REV.CSV',
'/home/forrest/daily_futures/AP_REV.CSV',
'/home/forrest/daily_futures/AX_REV.CSV',

'/home/forrest/daily_futures/BC_REV.CSV',
'/home/forrest/daily_futures/BG_REV.CSV',
'/home/forrest/daily_futures/BN_REV.CSV',
'/home/forrest/daily_futures/BO_REV.CSV',

'/home/forrest/daily_futures/C__REV.CSV',
'/home/forrest/daily_futures/CA_REV.CSV',
'/home/forrest/daily_futures/CB_REV.CSV',
'/home/forrest/daily_futures/CC_REV.CSV',
'/home/forrest/daily_futures/CL_REV.CSV',
'/home/forrest/daily_futures/CN_REV.CSV',
'/home/forrest/daily_futures/CR_REV.CSV',
'/home/forrest/daily_futures/CT_REV.CSV',

#'/home/forrest/daily_futures/DA_REV.CSV',
'/home/forrest/daily_futures/DJ_REV.CSV',
'/home/forrest/daily_futures/DT_REV.CSV',
'/home/forrest/daily_futures/DX_REV.CSV',

'/home/forrest/daily_futures/EC_REV.CSV',
'/home/forrest/daily_futures/ED_REV.CSV',
'/home/forrest/daily_futures/EN_REV.CSV',
'/home/forrest/daily_futures/ER_REV.CSV',
'/home/forrest/daily_futures/ES_REV.CSV',

'/home/forrest/daily_futures/FA_REV.CSV',
'/home/forrest/daily_futures/FB_REV.CSV',
#'/home/forrest/daily_futures/FC_REV.CSV',
'/home/forrest/daily_futures/FF_REV.CSV',

]

STEVENS_FUTURES = [
BASE_PATH + 'stevens_futures2/CME_CL1_FW.csv'

]

STEVENS_FUTURES = [x for x in os.listdir(BASE_PATH + 'stevens_futures2/') if '1_FW' in x and not x.startswith('.')]
STEVENS_CHAIN_TYPE = 'FW'
STEVENS_MONTH_NUM  = '1'

DAILIES_FUTURES = [
    BASE_PATH + 'kibot_data/cont_futures/daily/GC.txt',
    # BASE_PATH + 'kibot_data/cont_futures/daily/PA.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/PL.txt',
      BASE_PATH + 'kibot_data/cont_futures/daily/SI.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/HG.txt',
    # # #BASE_PATH + 'kibot_data/cont_futures/daily/NN.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/NQ.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/NG.txt',
  BASE_PATH + 'kibot_data/cont_futures/daily/CL.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/HO.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/RB.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/TY.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/JY.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/BP.txt',
    #  BASE_PATH + 'kibot_data/cont_futures/daily/CD.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/NE.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/AD.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/SF.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/DX.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/PX.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/GF.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/LE.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/HE.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/S.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/C.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/BO.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/SM.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/W.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/SB.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/KC.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/KW.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/CC.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/OJ.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/RR.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/O.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/daily/LB.txt',

]

FOREX_PAIRS = [
    BASE_PATH + 'kibot_data/forex/daily/EURUSD.txt',
    #BASE_PATH + 'kibot_data/forex/daily/EURJPY.txt',
    #BASE_PATH + 'kibot_data/forex/daily/GBPJPY.txt',
    #BASE_PATH + 'kibot_data/forex/daily/USDJPY.txt',
    BASE_PATH + 'kibot_data/forex/daily/EURAUD.txt',
    BASE_PATH + 'kibot_data/forex/daily/GBPUSD.txt',
    BASE_PATH + 'kibot_data/forex/daily/EURCAD.txt',

    BASE_PATH + 'kibot_data/forex/daily/AUDUSD.txt',
    BASE_PATH + 'kibot_data/forex/daily/NZDUSD.txt',
    BASE_PATH + 'kibot_data/forex/daily/GBPCHF.txt',
    BASE_PATH + 'kibot_data/forex/daily/EURGBP.txt',
    BASE_PATH + 'kibot_data/forex/daily/AUDCAD.txt',
    BASE_PATH + 'kibot_data/forex/daily/AUDCHF.txt',
    BASE_PATH + 'kibot_data/forex/daily/USDCHF.txt',
    BASE_PATH + 'kibot_data/forex/daily/AUDNZD.txt',
    BASE_PATH + 'kibot_data/forex/daily/EURCHF.txt',
    BASE_PATH + 'kibot_data/forex/daily/EURNZD.txt',

]

ALL_DATAS = [
    BASE_PATH + 'kibot_data/cont_futures/60min/ES.txt',
    #BASE_PATH + 'kibot_data/cont_futures/60min/GC.txt',

    #BASE_PATH + 'kibot_data/cont_futures/60min/PA.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/PL.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/SI.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/HG.txt',
    # #  BASE_PATH + 'kibot_data/cont_futures/60min/NN.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/NQ.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/NG.txt',
    #   BASE_PATH + 'kibot_data/cont_futures/60min/CL.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/HO.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/RB.txt',
    #  #  BASE_PATH + 'kibot_data/cont_futures/60min/TY.txt',
    #  #  BASE_PATH + 'kibot_data/cont_futures/60min/JY.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/JY.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/BP.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/CD.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/NE.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/AD.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/SF.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/DX.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/PX.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/GF.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/LE.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/HE.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/S.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/C.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/BO.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/SM.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/W.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/SB.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/KC.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/KW.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/CC.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/OJ.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/RR.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/O.txt',
    #    BASE_PATH + 'kibot_data/cont_futures/60min/LB.txt',
]

STOCKS = [

BASE_PATH + 'kibot_data/stocks/daily/SPY.txt',

]

STOCKS_BASE_PATH = BASE_PATH + 'kibot_data/stocks/daily'
FOREX_BASE_PATH = BASE_PATH + 'kibot_data/forex/360min'
CLC_FUTURES_PATH = '/home/forrest/daily_futures/'

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

def get_quandl_data(symbol,exchange='CME',month='1'):
    csv_name = exchange + '_' + symbol.upper() + str(month) + '.csv'
    with tarfile.open('quandl_data.tar.gz','r') as f:
        member = f.getmember(csv_name)
        ret = f.extractfile(member)
        contents = ret.read().decode("utf-8")

        return btfeed.GenericCSVData(dataname=io.StringIO(contents),
                              dtformat='%Y-%m-%d',
                              name=symbol,
                              timeframe=bt.TimeFrame.Ticks,
                              fromdate=datetime.datetime(2009, 1, 1),
                              todate=datetime.datetime(2010, 1, 1),
                              datetime=0,
                              open=1,
                              high=2,
                              low=3,
                              close=4,
                              volume=7,
                              openinterest=8,
                              plot=False
                              )

class MyPandasData(bt.feeds.PandasData):
    lines=('time',)
    params=(('time',1),)

def add_data(cerebro):
    stevens_added_commissions = [x['name'] for x in commissions.STEVENS_COMMISSIONS ]
    print(stevens_added_commissions)
    #stevens_added_commissions = list(set(stevens_added_commissions) - set(commissions.INDICIES) - set(commissions.VOLATILITY))
    #stevens_added_commissions = ['CME_ES']
    print(STEVENS_FUTURES)

    files = get_files_by_file_size(STOCKS_BASE_PATH, reverse=True)
    #files = files[:int(len(files)/2)]
    random.shuffle(files)

    for txt in sorted(STEVENS_FUTURES):

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

    #data has been loaded. let's precompute the number of trading securities
    for begin,end in global_config.GLOBAL_DATAFRAMES_START_END.values():
        delta = end - begin
        for i in range(delta.days + 1):
            d = begin + datetime.timedelta(i)
            global_config.GLOBAL_TRADING_SECURITIES[d] += 1
    for k,v in sorted(global_config.GLOBAL_TRADING_SECURITIES.items()):
        print(k,v)