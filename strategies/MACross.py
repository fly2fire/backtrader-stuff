import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import strategies.BaseStrategy

class MACross(strategies.BaseStrategy.BaseStrategy):

    def __init__(self):
        super().__init__()
        self.orders = dict()
        self.indicators = dict()
        for d in self.datas:
            self.orders[d.params.name] = None
            self.indicators[d.params.name] = dict()
            ema_fast = bt.ind.SMA(d,period=4)
            ema_slow = bt.ind.SMA(d, period=32)
            self.add_indicator(d,'ema_real_slow',bt.ind.SMA, period=200)

            self.add_indicator(d,'cross',bt.ind.CrossOver,ema_fast,ema_slow)
            self.add_indicator(d,'atr',bt.ind.ATR,period=60)

    def next(self):
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.datas):
            security_name = d.params.name

            #if self.orders[security_name]:
            #    continue

            contracts = self.do_sizing_simple(security_name,d)
            atr = self.get_indicator(d,'atr')*10
            #print(atr)
            ema_real_slow = self.get_indicator(d,'ema_slow')
            if self.get_indicator(d, 'cross')[0] == 1:
                if self.getposition(d).size > 0:
                    continue
                elif self.getposition(d).size < 0:
                    self.close(data=d)
                #self.orders[security_name] = self.buy_bracket(data=d, size=contracts, exectype=bt.Order.Market,stopprice=d.close[0]*.98, limitprice=d.close[0]*1.02)
                if ema_real_slow[0] > ema_real_slow[-1]:
                    self.buy(data=d,size=contracts)

            elif self.get_indicator(d, 'cross')[0] == -1:
                if self.getposition(d).size < 0:
                    continue
                elif self.getposition(d).size > 0:
                    self.close(data=d)
                #self.orders[security_name] = self.sell_bracket(data=d,size=contracts, exectype=bt.Order.Market,stopprice=d.close[0]*1.02,limitprice=d.close[0]*.98)
                #if ema_real_slow[0] < ema_real_slow[-1]:
                #    self.sell(data=d,size=contracts)
