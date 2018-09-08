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
            ma_fast = bt.ind.EMA(d,period=10)
            ma_slow = bt.ind.EMA(d,period=200)
            self.add_indicator(d,'cross',bt.ind.CrossOver,ma_fast,ma_slow)

    def next(self):
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.datas):
            security_name = d.params.name

            contracts = self.do_sizing_simple(security_name,d)

            if self.get_indicator(d,'cross')[0] == 1:
                if self.getposition(d).size > 0:
                    continue
                elif self.getposition(d).size < 0:
                    self.close(data=d)
                self.buy(data=d,size=contracts)

            elif self.get_indicator(d,'cross')[0] == -1:
                if self.getposition(d).size < 0:
                    continue
                elif self.getposition(d).size > 0:
                    self.close(data=d)
                self.sell(data=d,size=contracts)
