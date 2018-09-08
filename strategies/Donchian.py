import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators


import strategies.BaseStrategy

class Donchian(strategies.BaseStrategy.BaseStrategy):

    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'dc20',indicators.DonchianChannel,period=24)
            self.add_indicator(d,'dc10',indicators.DonchianChannel,period=10)
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
            dc20 = self.get_indicator(d,'dc20')
            dc10 = self.get_indicator(d,'dc10')
            if self.getposition(d).size > 0 and dc20.exitshort[0]:
                    self.close(data=d)
            elif self.getposition(d).size > 0 and dc20.exitlong[0]:
                self.close(data=d)
            if dc20.buysig[0]:
                if self.getposition(d).size > 0:
                    continue
                elif self.getposition(d).size < 0:
                    self.close(data=d)

                #self.orders[security_name] = self.sell(data=d,size=contracts)
                o = self.orders[security_name] = self.sell_bracket(data=d, size=contracts,exectype=bt.Order.Market,stopprice=d.close[0]*.99, limitprice=d.close[0]*1.01)
                self.record_bracket(o)
            elif dc20.sellsig[0]:#  and ma[0] < ma[-1]:
                if self.getposition(d).size < 0:
                    continue
                elif self.getposition(d).size > 0:
                    self.close(data=d)
                #self.orders[security_name] = self.buy(data=d,size=contracts)
                o = self.orders[security_name] = self.buy_bracket(data=d,size=contracts, exectype=bt.Order.Market,stopprice=d.close[0]*1.01,limitprice=d.close[0]*.99)
                self.record_bracket(o)