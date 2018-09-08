import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math

import indicators


import strategies.BaseStrategy

class RSI(strategies.BaseStrategy.BaseStrategy):

    def __init__(self):
        super().__init__()
        for d in self.datas:
            self.add_indicator(d,'rsi',bt.ind.RSI,period=3,safediv=True)
            #self.add_indicator(d,'atr',bt.ind.ATR,period=14)

    def next(self):
        #if not (datetime.time(10,00) <= self.data.datetime.time() <= datetime.time(16, 00)):
        #    return
        for i,d in enumerate(self.datas):
            security_name = d.params.name

            #if self.orders[security_name]:
            #    continue
            date = self.data.datetime.date()
            contracts = self.do_sizing_simple(security_name,d)
            valid_til = datetime.datetime(year=date.year,month=date.month,day=date.day,hour=23,minute=45)

            rsi = self.get_indicator(d,'rsi')
            #atr = self.get_indicator(d,'atr')
            if self.getposition(d).size > 0 and rsi[0] > 30:
                self.close(data=d)
                self.close_open_orders(d)
            elif self.getposition(d).size < 0 and rsi[0] < 70:
                self.close(data=d)
                self.close_open_orders(d)
            elif rsi[0] > 90:
                if self.getposition(d).size > 0:
                    continue
                elif self.getposition(d).size < 0:
                    self.close(data=d)

                #self.sell(data=d,size=contracts)
                #buy_order = self.buy(data=d, size=contracts, transmit=False)
                #sell_order = self.sell(data=d, size=contracts, transmit=False,exectype=bt.Order.Stop, price=d.close[0] - atr[0],parent=buy_order)
                #self.record_parent_stop(buy_order,sell_order)
                #o = self.orders[security_name] = self.buy_bracket(data=d, size=contracts,exectype=bt.Order.Market,stopprice=d.close[0]-atr[0], limitprice=d.close[0]+atr[0])
                #self.record_bracket(o)
            elif rsi[0] < 10:
                if self.getposition(d).size < 0:
                    continue
                elif self.getposition(d).size > 0:
                    self.close(data=d)

                self.buy(data=d,size=contracts)

                #sell_order = self.sell(data=d, size=contracts, transmit=False)
                #buy_order = self.buy(data=d, size=contracts, transmit=False,exectype=bt.Order.Stop, price=d.close[0] + atr[0],parent=sell_order)
                #self.record_parent_stop(sell_order,buy_order)
                #o = self.orders[security_name] = self.sell_bracket(data=d,size=contracts, exectype=bt.Order.Market,stopprice=d.close[0]+atr[0],limitprice=d.close[0]-atr[0])
                #self.record_bracket(o)