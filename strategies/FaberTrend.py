import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import main
import strategies.BaseStrategy

import global_config

class FaberTrend(strategies.BaseStrategy.BaseStrategy):
    params = (('fast', 32),('slow',256),('name','asdf'))

    def __init__(self):
        super().__init__()
        for d in self.datas:
            security_name = d.params.name
            self.add_indicator(d.close,security_name, 'fast',bt.ind.EMA,period=self.params.fast)
            self.add_indicator(d.close,security_name, 'slow',bt.ind.EMA,period=self.params.slow)
            self.add_indicator(d.close,security_name, 'momentum',indicators.Momentum,period=self.params.slow)
            self.add_indicator(d.close,security_name, 'greendays',indicators.GreenDaysPercent,period=self.params.slow)
            self.add_indicator(d.volume,security_name, 'avgvolume',bt.ind.EMA,period=20)

    def next(self):
        today = self.datetime.date()
        weekday = today.weekday()
        if weekday not in [0,1]:
            return
        trading_securities = list(self.get_trading_securities(today))
        l = len(trading_securities)
        trading_securities = list(sorted(trading_securities,key=lambda d: self.get_indicator(d,'avgvolume'), reverse=True))
        trading_securities = trading_securities[:int(l/2)]
        trading_securities = sorted(trading_securities,key=lambda d: d.volume[0])
        trading_securities = sorted(trading_securities, key=lambda d: self.get_indicator(d,'momentum') * self.get_indicator(d,'greendays'), reverse=True)
        for i,d in enumerate(trading_securities):
            volume = d.close[0]*d.volume[0]
            #if volume < 1000000:
            #    continue
            security_name = d.params.name
            fast = self.get_indicator(d,'fast')
            slow = self.get_indicator(d,'slow')
            pos = self.get_per_strategy_position(security_name)
            if self.is_last_trading_day(security_name,today):
                self.close_out(d,size=pos)
                continue

            if fast[0] > slow[0] and pos <= 0:
                if pos < 0 and weekday == 0:
                    o = self.close_out(d,size=pos)
                    #print("trying to close ", pos, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
                contracts = self.do_sizing_simple(security_name, d, today)
                if contracts > 0 and self.positions_available() and weekday == 1:
                    o = self.buy_in(d,size=contracts)
                    #print("trying to buy ", contracts, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
            elif fast[0] < slow[0] and pos >= 0:
                if pos > 0 and weekday == 0:
                    o = self.close_out(d,size=pos)
                    #print("trying to close ", pos, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
