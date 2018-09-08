import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators
import strategies.BaseStrategy

class WeekylHigh52(strategies.BaseStrategy.BaseStrategy):

    def __init__(self):

        self.orders = dict()
        self.indicators = dict()
        for d in self.datas:
            self.orders[d.params.name] = None
            self.indicators[d.params.name] = dict()
            self.add_indicator(d, 'dc20', indicators.DonchianChannel, period=240)


    def next(self):
        for i, d in enumerate(self.datas):
            security_name = d.params.name

            if self.orders[security_name]:
                continue

            contracts = int(self.broker.getvalue() / len(self.datas) / d.close[0] * .95)
            # atr = self.get_indicator(d,'atr')

            if self.get_indicator(d, 'dc20').buysig[0]:
                # if self.get_indicator(d,'rsi')[0]  > 50:
                if self.getposition(d).size > 0:
                    continue
                elif self.getposition(d).size < 0:
                    self.close(data=d)
                self.orders[security_name] = self.buy_bracket(data=d, size=contracts, exectype=bt.Order.Market,
                                                              stopprice=d.close[0] * .80, limitprice=d.close[0] * 2)

            elif self.get_indicator(d, 'dc20').sellsig[0]:
                # elif self.get_indicator(d,'rsi')[0] < 50:
                if self.getposition(d).size < 0:
                    continue
                elif self.getposition(d).size > 0:
                    self.close(data=d)
                #self.orders[security_name] = self.sell_bracket(data=d, size=contracts, exectype=bt.Order.Market,
                #                                               stopprice=d.close[0] * 1.1, limitprice=d.close[0] * .9)
