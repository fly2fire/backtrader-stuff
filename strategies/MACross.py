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
        for i,d in enumerate(self.get_trading_securities()):
            security_name = d.params.name
            print(security_name)

            #if self.orders[security_name]:
            #    continue

            contracts = self.do_sizing_simple(security_name,d)
            atr = self.get_indicator(d,'atr')*10
            #print(atr)
            ema_real_slow = self.get_indicator(d,'ema_slow')
            if self.get_indicator(d, 'cross')[0] == 1:
                self.order_target_percent(d,.99)

            elif self.get_indicator(d, 'cross')[0] == -1:
                self.order_target_percent(d, 0)
