import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import main
import strategies.BaseStrategy

class SimpleMA(strategies.BaseStrategy.BaseStrategy):

    def __init__(self):
        self.brackets = dict()
        self.orders = dict()
        self.indicators = dict()
        for d in self.datas:
            self.orders[d.params.name] = None
            self.indicators[d.params.name] = dict()
            self.add_indicator(d,'fast',bt.ind.EMA,period=32)
            self.add_indicator(d,'slow',bt.ind.EMA,period=128)

    def next(self):
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.get_trading_securities()):
            security_name = d.params.name
            #print(security_name)

            contracts = self.do_sizing_simple(security_name,d)

            fast = self.get_indicator(d,'fast')
            slow = self.get_indicator(d,'slow')
            pos = self.getposition(d).size
            if fast[0] > slow[0]:
                if pos <= 0:
                    if pos < 0:
                        self.close(d)
                    self.buy(d,size=contracts)
            elif fast[0] < slow[0]:
                if pos >= 0:
                    if pos > 0:
                        self.close(d)
                    self.sell(d,size=contracts)
