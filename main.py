import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import time
import observers
import utils
import math
import random

import strategies.Donchian
import strategies.MACross
import strategies.Turtle
import strategies.BBands
import strategies.SimpleMA
import strategies.UpDownCandles
import strategies.MACross
import strategies.RSI
import strategies.CarverEWMAC
import strategies.FaberTrend

from commissions import STEVENS_COMMISSIONS
import commissions
import global_config


def main(*args, **kwargs):
    start = time.time()
    cerebro = bt.Cerebro(stdstats=False)

    if global_config.GLOBAL_CONFIG == 'FOREX':
        cerebro.broker.setcommission(leverage=50,stocklike=False,commtype=bt.CommInfoBase.COMM_PERC,commission=.0000)
        # Add the new commission scheme
        #comminfo = commissions.forexSpreadCommisionScheme(spread=1.0)
        #cerebro.broker.addcommissioninfo(comminfo)
        pass
    elif global_config.GLOBAL_CONFIG == 'FUTURES':
        for com in STEVENS_COMMISSIONS:
            cerebro.broker.setcommission(mult=com['mult'],name=com['name'],margin=com['margin'],commission=0)
    elif global_config.GLOBAL_CONFIG == 'STOCK':
        cerebro.broker.setcommission(leverage=1,stocklike=True,commission=.0001,mult=1,margin=None,interest=.00,interest_long=True)

    cerebro.broker.set_cash(1000000)
    cerebro.broker.set_shortcash(False)
    cerebro.addobserver(observers.AcctValue)
    cerebro.addobserver(observers.LogAcctValue)
    cerebro.addobserver(observers.AcctCash)
    #cerebro.addobserver(observers.AggregateAssets)
    utils.add_data(cerebro)
    for x in range(0,2):
        fast = random.randint(20,60)
        slow = fast * random.randint(3,5)
        #fast = 20
        #slow = 100
        name = str(x)
        print("adding strat with fast {} slow {}".format(fast,slow))
    cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=64, slow=256, name='trend1', plot=False)
    #cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=32, slow=128, name='trend2', plot=False)
    #cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=16, slow=64, name='trend3', plot=False)
    #cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=8, slow=32, name='trend4', plot=False)
    #cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=4, slow=16, name='trend5', plot=False)
    #cerebro.addstrategy(strategies.FaberTrend.FaberTrend, fast=2, slow=8, name='trend6', plot=False)

    cerebro.addobserver(bt.observers.DrawDown)
    #cerebro.addobserver(bt.observers.Benchmark)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio)
    cerebro.addanalyzer(bt.analyzers.SQN)
    #cerebro.addanalyzer(bt.analyzers.PyFolio)
    #cerebro.addanalyzer(bt.analyzers.Calmar)
    cerebro.addanalyzer(bt.analyzers.TimeDrawDown)
    cerebro.addanalyzer(bt.analyzers.GrossLeverage)
    cerebro.addanalyzer(bt.analyzers.PeriodStats)
    #cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio_A)
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)
    cerebro.addanalyzer(bt.analyzers.TimeReturn, timeframe=bt.TimeFrame.Years)

    ret = cerebro.run()
    for thing in ret[0].analyzers._items:
        name = type(thing).__name__
        if name in ['GrossLeverage','Calmar']:
            calmar_vals = [x for x in thing.get_analysis().values() if not math.isnan(x)]
            average = sum(calmar_vals) / len(calmar_vals)
            print(name,average)
        else:
            print(name)
            for k,v in thing.get_analysis().items():
                print('\t',k,v)
        #print(thing.get_analysis())
    strat = ret[0]
    end = time.time()
    print("simulation took",end-start,"seconds")
    #cerebro wants to plot a different plot for each strategy even if they share the same broker
    #for our purposes that isn't really necessary, so here let's just kick out everything but the 1st
    #strategy so we only plot one
    new_runstrats = []
    for s in cerebro.runstrats:
        new_runstrats.append([s[0]])
    cerebro.runstrats = new_runstrats
    cerebro.plot()


if __name__ == '__main__':
    import multiprocessing
    #with multiprocessing.Pool(2) as p:
    #    p.map(main,[1,2])
    main()