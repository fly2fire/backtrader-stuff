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
            self.add_indicator(d,'fast',bt.ind.EMA,period=self.params.fast)
            self.add_indicator(d,'slow',bt.ind.EMA,period=self.params.slow)

    def next(self):
        today = self.datetime.date()
        weekday = today.weekday()

        if weekday not in [0,1]:
            return
        for i,d in enumerate(self.get_trading_securities(today)):
            security_name = d.params.name
            fast = self.get_indicator(d,'fast')
            slow = self.get_indicator(d,'slow')
            pos = self.get_per_strategy_position(security_name)
            if self.is_last_trading_day(security_name,today):
                self.close_out(d,size=pos)
                continue

            if fast[0] > slow[0] and pos <= 0:
                contracts = self.do_sizing_simple(security_name, d)
                if pos < 0 and weekday == 0:
                    o = self.close_out(d,size=pos)
                    #print("trying to close ", pos, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
                if contracts > 0 and self.positions_available() and weekday == 1:
                    o = self.buy_in(d,size=contracts)
                    #print("trying to buy ", contracts, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
            elif fast[0] < slow[0] and pos >= 0:
                if pos > 0 and weekday == 0:
                    o = self.close_out(d,size=pos)
                    #print("trying to close ", pos, "of", security_name, "@", d.close[0], "cash:", self.broker.getcash(),"ref:",o.ref)
