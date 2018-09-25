import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import tarfile
import io
import sys
import random

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
    files = get_files_by_file_size(STOCKS_BASE_PATH,reverse=True)
    files = files[:int(len(files)/8)]
    print(files[0])
    random.shuffle(files)
    for txt in  ['./SPY.txt','./IWM.txt','EFA.txt','LQD.txt','VEA.txt','AGG.txt',]:
        print("adding",txt)
        if 'CL' in txt:
            data = btfeed.GenericCSVData(dataname=txt,
                                         dtformat='%m/%d/%Y',
                                         # tmformat='%H:%M',
                                         name=os.path.splitext(os.path.basename(txt))[0],
                                         timeframe=bt.TimeFrame.Days,
                                         fromdate=datetime.datetime(1900, 1, 1),
                                         todate=datetime.datetime(2018, 12, 1),
                                         datetime=0,
                                         time=-1,
                                         open=1,
                                         high=2,
                                         low=3,
                                         close=4,
                                         volume=5,
                                         openinterest=6,
                                         plot=False,
                                         preload=True,
                                         runonce=True
                                         )
        elif True:# 'daily' in txt:
            data = btfeed.GenericCSVData(dataname=txt,
                                     dtformat='%m/%d/%Y',
                                     #tmformat='%H:%M',
                                     name = os.path.splitext(os.path.basename(txt))[0],
                                     timeframe=bt.TimeFrame.Days,
                                     fromdate=datetime.datetime(1900, 1, 1),
                                     todate=datetime.datetime(2018, 12, 1),
                                     datetime=0,
                                     time=-1,
                                     open=1,
                                     high=2,
                                     low=3,
                                     close=4,
                                     volume=5,
                                     openinterest=-6,
                                     plot=False,
                                     preload=True,
                                     runonce=True
                                     )
        else:

            data = btfeed.GenericCSVData(dataname=txt,
                                     dtformat='%m/%d/%Y',
                                     tmformat='%H:%M',
                                     name = os.path.splitext(os.path.basename(txt))[0],
                                     timeframe=bt.TimeFrame.Minutes,
                                     fromdate=datetime.datetime(2000, 1, 1),
                                     todate=datetime.datetime(2018, 12, 1),
                                     datetime=0,
                                     time=1,
                                     open=2,
                                     high=3,
                                     low=4,
                                     close=5,
                                     volume=6,
                                     openinterest=-6,
                                    # plot=False,
                                     preload=True,
                                     runonce=True
                                     )


        #data = MyChartData(dataname=txt,name=os.path.splitext(os.path.basename(txt))[0])
        cerebro.adddata(data)
        #if global_config.GLOBAL_CONFIG == 'FOREX':

            #comminfo = commissions.forexSpreadCommisionScheme(spread=0.0,JPY_pair='JPY' in txt)
            #cerebro.broker.addcommissioninfo(comminfo,name=os.path.basename(txt).split('.')[0])