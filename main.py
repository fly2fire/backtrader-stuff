import datetime
import backtrader as bt
import backtrader.feeds as btfeed

class EVWAP(bt.Indicator):

    lines = ('evwap',)
    params = (('period',10),)

    def __init__(self):
        self.addminperiod(self.params.period)
        self.time_ma = bt.ind.EMA(period=self.params.period)

    def next(self):
        volume_price_sum = 0
        volume_sum = sum(self.data.volume.get(size=self.params.period))
        for i,(v,p) in enumerate(zip(self.data.volume.get(size=self.params.period),self.data.close.get(size=self.params.period))):
            volume_price_sum += v * p
        average_price = volume_price_sum / volume_sum
        #print(average_price)
        self.lines.evwap[0] = (average_price + self.time_ma[0])/2
        #print(volume_sum)


class maCross(bt.Strategy):

    def __init__(self):
        self.fast_ma = bt.ind.SMA(period=2)
        self.slow_ma = bt.ind.SMA(period=20)

        self.atr = bt.ind.ATR(period=30)

        # Cross of macd.macd and macd.signal
        self.cross = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)
        self.orders = dict()
        for d in self.datas:
            self.orders[d._dataname] = None

    def stop(self):
        for d in self.datas:
            self.close(data=d)


    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        #print(self.orders)

        lot_dollars = self.broker.getvalue() / len(self.datas)*.9

        for i,d in enumerate(self.datas):
            security_name = d._dataname

            # we only allow one outstanding backet order per security. if this is not none, that means we have
            # a pending buy / stop loss / profit, so we continue
            if self.orders[security_name] is not None:
                continue

            pos = self.getposition(d).size
            lot_size = int(lot_dollars / d.close[0])
            assert(not pos)
            if self.fast_ma[0] > self.slow_ma[0]:
                print("buying",lot_size)
                buy_order = self.buy(data=d,size=lot_size,transmit=False)
                trail_stop = self.sell(data=d,size=lot_size,parent=buy_order,trailpercent=.01,exectype=bt.Order.StopTrail)
                self.orders[security_name] = [buy_order,trail_stop]
            elif self.fast_ma[0] < self.slow_ma[0]:

                print("selling",lot_size)
                sell_order = self.sell(data=d,size=lot_size,transmit=False)
                trail_stop = self.buy(data=d,size=lot_size,parent=sell_order,trailpercent=.01,exectype=bt.Order.StopTrail)
                self.orders[security_name] = [sell_order,trail_stop]



    def notify_order(self, order):

        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        security_name = order.params.data._dataname
        if order.status in [order.Completed]:
            if order.isbuy():
                pass
                self.log('BUY EXECUTED, %.6f' % order.executed.price)
            elif order.issell():
                pass
                self.log('SELL EXECUTED, %.6f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled]:
            self.log('Order Canceled')
        elif order.status in [order.Margin]:
            self.log('Order Margin')
        elif order.status in [order.Rejected]:
            self.log('Order Rejected')

        for k,v in self.orders.items():
            if v is None:
                continue
            for o in v:
                if not o.status in [o.Canceled,o.Margin,o.Rejected,o.Completed,]:
                    break
            else:
                self.orders[k] = None

class AcctValue(bt.Observer):
    alias = ('Value',)
    lines = ('value',)

    plotinfo = {"plot": True, "subplot": True}

    def next(self):
        self.lines.value[0] = self._owner.broker.getvalue() # Get today's account value (cash + stocks)

def add_data(cerebro):
    for txt in ['USDCAD.txt']:
        data = btfeed.GenericCSVData(dataname=txt,
                                     dtformat='%m/%d/%Y',
                                     tmformat='%H:%M',

                                     fromdate=datetime.datetime(1990, 1, 1),
                                     todate=datetime.datetime(2019, 6, 1),

                                     #  nullvalue=0.0,

                                     datetime=0,
                                     time=1,
                                     open=2,
                                     high=3,
                                     low=4,
                                     close=5,
                                     volume=6,
                                     openinterest=-6)
        cerebro.adddata(data)

cerebro = bt.Cerebro(stdstats=False)

cerebro.broker.set_cash(1000000) # Set our starting cash to $1,000,000
cerebro.addobserver(AcctValue)
add_data(cerebro)
cerebro.addstrategy(maCross)
cerebro.addobserver(bt.observers.DrawDown)

cerebro.run()
cerebro.plot()