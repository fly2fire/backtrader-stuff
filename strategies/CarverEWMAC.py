import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import main
import strategies.BaseStrategy

import global_config

class CarverEWMAC(strategies.BaseStrategy.BaseStrategy):
    params = (('fast', 5),('slow',20),('name','asdf'))

    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'ewmac',indicators.EWMACfull)

    def next(self):
        if global_config.GLOBAL_CONFIG == 'FUTURES':
            self.update_margins()
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        weekday = self.datetime.date().weekday()
        if weekday != 0:
            return
        for i,d in enumerate(self.get_trading_securities()):

            security_name = d.params.name
            contracts = self.do_sizing_simple(security_name,d)

            ewmac = self.get_indicator(d,'ewmac')
            pos = self.get_per_strategy_position(security_name)

            comminfo = self.broker.comminfo[security_name]
            mult = comminfo.params.mult
            contract_val = mult * d.close[0]
            max_contracts = self.broker.getvalue() / self.get_total_possible_positions() / contract_val
            print("max",security_name,"contracts",max_contracts)
            contracts = (12.5/ewmac.yearly_returns[0]) * ewmac[0] * max_contracts
            if math.isnan(contracts):
                contracts = pos
            else:
                contracts = int(contracts)
            diff = int(math.fabs(contracts - pos))
            if contracts > pos:
                self.buy(data=d,size=diff)
            elif contracts < pos:
                self.sell(data=d, size=diff)


