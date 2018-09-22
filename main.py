import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import time
import observers
import utils
import math


import strategies.Donchian
import strategies.MACross
import strategies.Turtle
import strategies.BBands
import strategies.SimpleMA
import strategies.UpDownCandles
import strategies.MACross
import strategies.RSI

from commissions import ALL_COMMISSIONS
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
        for com in ALL_COMMISSIONS:
            cerebro.broker.setcommission(**com)
    elif global_config.GLOBAL_CONFIG == 'STOCK':
        cerebro.broker.setcommission(leverage=1,stocklike=True,commission=.0001,mult=1,margin=None,interest=.00,interest_long=True)

    cerebro.broker.set_cash(2500000)
    cerebro.addobserver(observers.AcctValue)
    cerebro.addobserver(observers.AcctCash)
    utils.add_data(cerebro)
    cerebro.addstrategy(strategies.SimpleMA.SimpleMA)
    cerebro.addobserver(bt.observers.DrawDown)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio)
    cerebro.addanalyzer(bt.analyzers.SQN)
    #cerebro.addanalyzer(bt.analyzers.PyFolio)
    #cerebro.addanalyzer(bt.analyzers.Calmar)
    cerebro.addanalyzer(bt.analyzers.TimeDrawDown)
    cerebro.addanalyzer(bt.analyzers.GrossLeverage)
    cerebro.addanalyzer(bt.analyzers.PeriodStats)
    cerebro.addanalyzer(bt.analyzers.Returns)
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
    cerebro.plot()


if __name__ == '__main__':

    main()