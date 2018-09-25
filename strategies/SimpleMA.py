import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import main
import strategies.BaseStrategy

class SimpleMA(strategies.BaseStrategy.BaseStrategy):
    params = (('fast', 5),('slow',20),('name','asdf'))

    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'fast',bt.ind.EMA,period=self.params.fast)
            self.add_indicator(d,'slow',bt.ind.EMA,period=self.params.slow)
            self.add_indicator(d,'really_slow',bt.ind.EMA,period=100)

    def next(self):
        #print(self.params.name)
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.get_trading_securities()):
            security_name = d.params.name
            #print(security_name)

            contracts = self.do_sizing_simple(security_name,d)

            fast = self.get_indicator(d,'fast')
            slow = self.get_indicator(d,'slow')
            really_slow = self.get_indicator(d,'really_slow')
            pos = self.get_per_strategy_position(security_name)
            if fast[0] > slow[0] and fast[-1] < slow[-1]:
                if pos <= 0:
                    if pos < 0:
                        print("should be closing", self.get_per_strategy_position(security_name))
                        self.close(d,size=pos)
                    self.buy(d,size=contracts)
            elif fast[0] < slow[0] and fast[-1] > slow[-1]:
                if pos >= 0:
                    if pos > 0:
                        print("should be closing",self.get_per_strategy_position(security_name))
                        self.close(d,size=pos)
                    #self.sell(d,size=contracts)
