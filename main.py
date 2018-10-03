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

from commissions import ALL_COMMISSIONS, PINNACLE_COMMISSIONS, STEVENS_COMMISSIONS
import commissions
import global_config


def main():
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
            cerebro.broker.setcommission(mult=com['mult'],name=com['name'],margin=com['margin'])
    elif global_config.GLOBAL_CONFIG == 'STOCK':
        cerebro.broker.setcommission(leverage=3,stocklike=True,commission=.0001,mult=1,margin=None,interest=.01,interest_long=True)

    cerebro.broker.set_cash(250000)
    cerebro.broker.set_shortcash(False)
    cerebro.addobserver(observers.AcctValue)
    cerebro.addobserver(observers.AcctCash)
    utils.add_data(cerebro)
    for x in range(0,1):
        fast = random.randint(20,60)
        slow = fast * random.randint(3,5)
        #fast = 20
        #slow = 100
        name = str(x)
        print("adding strat with fast {} slow {}".format(fast,slow))
        #cerebro.addstrategy(strategies.SimpleMA.SimpleMA,fast=fast,slow=slow,name=name,plot=False)
    cerebro.addstrategy(strategies.CarverEWMAC.CarverEWMAC, fast=64, slow=256, name="5", plot=False)
    cerebro.addobserver(bt.observers.DrawDown)
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

    main()