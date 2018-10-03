import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import main
import strategies.BaseStrategy

import global_config

class SimpleMA(strategies.BaseStrategy.BaseStrategy):
    params = (('fast', 5),('slow',20),('name','asdf'))

    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'fast',bt.ind.EMA,period=self.params.fast)
            self.add_indicator(d,'slow',bt.ind.EMA,period=self.params.slow)
            self.add_indicator(d,'really_slow',bt.ind.EMA,period=200)

    def next(self):
        if global_config.GLOBAL_CONFIG == 'FUTURES':
            self.update_margins()
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        weekday = self.datetime.date().weekday()

        for i,d in enumerate(self.get_trading_securities()):

            security_name = d.params.name
            contracts = self.do_sizing_simple(security_name,d)

            fast = self.get_indicator(d,'fast')
            slow = self.get_indicator(d,'slow')
            really_slow = self.get_indicator(d,'really_slow')
            pos = self.get_per_strategy_position(security_name)
            if fast[0] > slow[0] and pos <= 0:
                if pos < 0:
                    self.close(d,size=pos)
                if contracts > 0:
                    o = self.buy(d,size=contracts)
                    print("trying to buy ", contracts, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
            elif fast[0] < slow[0] and pos >= 0:
                if pos > 0:
                    self.close(d,size=pos)
                if contracts > 0:
                    o = self.sell(d,size=contracts)
                #if really_slow[0] < really_slow[-50]:
                #    o = self.sell(data=d,size=contracts)
                #    print("trying to short ", contracts, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)

