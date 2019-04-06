import math

import backtrader as bt

import global_config
from collections import defaultdict
import commissions

class BaseStrategy(bt.Strategy):
    params = (('name','asdf'),)

    def __init__(self):
        self.orders = dict()
        self.indicators = dict()
        self.brackets = dict()
        self.per_strategy_positions = dict()
        for d in self.datas:
            self.orders[d.params.name] = None
            self.indicators[d.params.name] = dict()
        self.num_positions_on = 0

    def close_out(self, *args, **kwargs):
        self.num_positions_on -= 1
        return self.close(*args, **kwargs)

    def buy_in(self, *args, **kwargs):
        self.num_positions_on += 1
        return self.buy(*args, **kwargs)

    def short_sell(self, *args, **kwargs):
        self.num_positions_on += 1
        return self.sell(*args, **kwargs)

    def positions_available(self):
        return self.num_positions_on < self.get_total_possible_positions() / 4

    def get_trading_securities(self, td=None):
        today = td if td else self.datetime.date()
        for d in self.datas:
            security_name = d.params.name
            start_dt,end_dt = global_config.GLOBAL_DATAFRAMES_START_END[security_name]
            if start_dt < today < end_dt:
                yield d

    def is_last_trading_day(self, security_name, td=None):
        _,end_dt = global_config.GLOBAL_DATAFRAMES_START_END[security_name]
        today = td if td else self.datetime.date()
        return end_dt == today

    def get_per_strategy_num_positions(self):
        return len([x for x in self.per_strategy_positions.values() if x != 0])

    def get_total_num_positions(self):
        return sum([s.get_per_strategy_num_positions() for s in self.cerebro.runningstrats])

    def get_total_possible_positions(self):
        positions = global_config.GLOBAL_TRADING_SECURITIES[self.datetime.date()] * len(self.cerebro.runningstrats)
        return max(positions,1)

    def get_per_strategy_position(self,security_name):
        return self.per_strategy_positions.get(security_name,0)

    def set_per_strategy_position(self,security_name, size):
        self.per_strategy_positions[security_name] = size

    def get_per_strategy_value(self, security_name):
        return self.get_per_strategy_position(security_name) * self.get_data_from_name(security_name).close[0]

    def get_data_from_name(self,security_name):
        for d in self.datas:
            if d.params.name == security_name:
                return d

    def prenext(self):
        self.next()

    def stop(self):
        for d in self.datas:
            self.close(data=d)

    def log(self, txt, dt=None):
        dt = dt or self.datetime.date()
        t  = self.datetime.time()
        print('%s %s %s, %s' % (self.params.name, dt.isoformat(), t, txt))

    def add_indicator(self,data,name,ind,*args,**kwargs):
        self.indicators[data.params.name][name] = ind(data,*args,**kwargs)

    def update_margins(self):
        for data in self.get_trading_securities():
            security_name = data.params.name
            comminfo = self.broker.comminfo[security_name]
            ratio = commissions.STEVENS_MARGIN_RATIOS[security_name]
            comminfo.params.margin = data.close[0] * comminfo.params.mult * ratio
#            comminfo.margin = data.close[0] * comminfo.params.mult * ratio

    def get_indicator(self,data,name):
        return self.indicators[data.params.name][name]

    def do_sizing_simple(self,security_name, data):
        broker = self.broker
        num_strats = len(self.cerebro.runningstrats)
        if global_config.GLOBAL_CONFIG in ['STOCK']:
            leverage = self.broker.comminfo[None].params.leverage
            #return 100
            try:
                stocks = self.broker.getvalue() / self.get_total_possible_positions() * 3
                stocks /= data.close[0]
                stocks *= .9 #leave some cushion for when stock are (de)listed
                stocks *= leverage
                stocks = int(stocks)
            except:
                stocks = 1
            if stocks == 0:
                print("num stocks is zero!")
                stocks = 1
            return stocks
        elif global_config.GLOBAL_CONFIG in ['FOREX']:
            comminfo = self.broker.comminfo
            if security_name in self.broker.comminfo:
                leverage = self.broker.comminfo[security_name].params.leverage
            else:
                leverage = self.broker.comminfo[None].params.leverage
            #return 1
            stocks = int(self.broker.getvalue() / len([self.get_trading_securities()]) / data.close[0] * .19 * leverage * 1/ num_strats)
            if stocks == 0:
                stocks = 1
            return stocks

        elif global_config.GLOBAL_CONFIG in ['FUTURES']:
            #return 1
            comminfo = self.broker.comminfo[security_name]
            #backtrader doesnt allow us to have changing margins, which kinda sucks. instead, we emulate it here
            #by assuming a fairly safe margin of 10%
            mult = comminfo.params.mult
            margin = comminfo.params.margin
            try:
                max_contracts = int((self.broker.getvalue() / margin / (self.get_total_possible_positions()))**(1.0/2.0))
            except:
                max_contracts = 0
            return int(math.fabs(max_contracts))

    def close_open_orders(self, data):
        orders = self.orders[data.params.name]
        if orders is None:
            return
        for o in orders:
            self.cancel(o)
            self.log('Order cancelled')

    def record_parent_stop(self,parent,stop):
        self.brackets[parent.ref] = [stop]

    def record_bracket(self,bracket):
        # for brackets
        parent,stop,limit = bracket
        self.brackets[parent.ref] = [stop,limit]


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        security_name = order.params.data.params.name
        if order.status in [order.Completed]:
            if order.isbuy():
                pass
                self.log('{} BUY EXECUTED, {} @ {}. comm {} ref: {}'.format(security_name, order.executed.size, order.executed.price,order.executed.comm,order.ref))
            elif order.issell():
                pass
                self.log('{} SELL EXECUTED, {} @ {}. comm {} ref: {}'.format(security_name, order.executed.size, order.executed.price,order.executed.comm,order.ref))
            self.set_per_strategy_position(security_name,self.get_per_strategy_position(security_name)+order.executed.size)
            self.bar_executed = len(self)


        elif order.status in [order.Canceled]:
            self.log('Order Canceled ref: {}'.format(order.ref))
        elif order.status in [order.Margin]:
            self.log('Order Margin ref: {}'.format(order.ref))
        elif order.status in [order.Rejected]:
            self.log('Order Rejected ref: {}'.format(order.ref))

        if order.ref in self.brackets:
            #did we cancel the parent? if so we need to cancel the children
            if order.status in [order.Canceled, order.Margin, order.Rejected,order.Expired]:
                for o in self.brackets[order.ref]:
                    self.cancel(o)
                del self.brackets[order.ref]



        for k,v in self.orders.items():
            if v is None:
                continue
            if isinstance(v,list):
                for o in v:
                    if o.status not in [o.Canceled, o.Margin, o.Rejected, o.Completed, o.Expired]:
                        break
                else:
                    self.orders[k] = None
            elif v.status in [v.Canceled, v.Margin, v.Rejected, v.Completed, v.Expired]:
                self.orders[k] = None