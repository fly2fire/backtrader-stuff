import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import os
import math



class AcctCash(bt.Observer):
    alias = ('Value',)
    lines = ('value',)

    plotinfo = {"plot": True, "subplot": True}

    def next(self):
        self.lines.value[0] = self._owner.broker.getcash() / self._owner.broker.getvalue() # Get today's account value (cash + stocks)


class AcctValue(bt.Observer):
    alias = ('Value',)
    lines = ('value',)

    plotinfo = {"plot": True, "subplot": True}

    def next(self):
        self.lines.value[0] = self._owner.broker.getvalue() # Get today's account value (cash + stocks)

class LogAcctValue(bt.Observer):
    alias = ('Value',)
    lines = ('value',)

    plotinfo = {"plot": True, "subplot": True}

    def __init__(self):
        self.initial_value = self._owner.broker.getvalue()

    def next(self):
        try:
            self.lines.value[0] = math.log(self._owner.broker.getvalue(),2) # Get today's account value (cash + stocks)
        except:
            self.lines.value[0] = 0


class AggregateAssets(bt.Observer):
    alias = ('Value',)
    lines = ('value',)

    plotinfo = {"plot": True, "subplot": True}

    def next(self):
        self.lines.value[0] = sum(self._owner.datas) / len(self._owner.datas)  # Get today's account value (cash + stocks)

class RollingSharpe(bt.Observer):
    alias=('Value',)
    lines=('Value',)

    plotinfo = {"plot": True, "subplot": True}

    def next(self):
        self.lines.value[0] =0
