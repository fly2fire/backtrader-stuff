import backtrader as bt

import global_config

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

    def get_trading_securities(self):
        for d in self.datas:
            if d.datetime.date() == self.datetime.date():
                yield d

    def get_per_strategy_position(self,security_name):
        return self.per_strategy_positions.get(security_name,0)

    def set_per_strategy_position(self,security_name, size):
        self.per_strategy_positions[security_name] = size


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

    def get_indicator(self,data,name):
        return self.indicators[data.params.name][name]

    def do_sizing_simple(self,security_name, data):
        broker = self.broker
        num_strats = len(self.cerebro.runningstrats)
        if global_config.GLOBAL_CONFIG in ['STOCK']:
            leverage = self.broker.comminfo[None].params.leverage
            #return 100
            try:
                #print("num trading securities",len([self.get_trading_securities()]))
                stocks = int(self.broker.getvalue() / (len([self.get_trading_securities()])) / data.close[0] * .9 * leverage * 1 / num_strats)
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
            margin = comminfo.margin
            mult = comminfo.params.mult
            try:
                max_contracts = int((self.broker.getvalue() / margin / len([self.get_trading_securities()]) / num_strats)**(1.0 / 2.0))
            except:
                max_contracts = 1
            if max_contracts == 0:
                max_contracts = 1
            return max_contracts

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
                self.log('{} BUY EXECUTED, {} @ {}. comm {}'.format(security_name, order.executed.size, order.executed.price,order.executed.comm))
            elif order.issell():
                pass
                self.log('{} SELL EXECUTED, {} @ {}. comm {}'.format(security_name, order.executed.size, order.executed.price,order.executed.comm))
            self.set_per_strategy_position(security_name,self.get_per_strategy_position(security_name)+order.executed.size)
            self.bar_executed = len(self)

        elif order.status in [order.Canceled]:
            self.log('Order Canceled')
        elif order.status in [order.Margin]:
            self.log('Order Margin')
        elif order.status in [order.Rejected]:
            self.log('Order Rejected')

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