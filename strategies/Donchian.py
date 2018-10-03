import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators


import strategies.BaseStrategy

class Donchian(strategies.BaseStrategy.BaseStrategy):
    params = (('entry', 5),('exit',20),('name','asdf'))


    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'entry',indicators.DonchianChannel,period=self.params.entry)
            self.add_indicator(d,'exit',indicators.DonchianChannel,period=self.params.exit)
            #self.add_indicator(d,'ma',bt.ind.SMA,period=40)
            self.add_indicator(d,'atr',bt.ind.ATR,period=100)

    def next(self):
        #if not (datetime.time(14,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.datas):
            security_name = d.params.name

            if self.orders[security_name]:
                continue

            #date = self.data.datetime.date()
            #valid_til = datetime.datetime(year=date.year,month=date.month,day=date.day,hour=23,minute=45)
            contracts = self.do_sizing_simple(security_name, d)
            entry = self.get_indicator(d,'entry')
            exit = self.get_indicator(d,'exit')
            pos = self.getposition(d).size
            if pos > 0 and exit.sellsig[0]:
                self.close(data=d)
            if entry.buysig[0]:
                if pos > 0:
                    continue
                elif pos < 0:
                    self.close(data=d)
                self.buy(data=d,size=contracts)
