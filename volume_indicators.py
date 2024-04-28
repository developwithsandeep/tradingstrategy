import pandas_ta as ta
from trading_indicator import TradingIndicator


class VolumeIndicators(TradingIndicator):
    def __init__(self,data):
        super().__init__(self,data)

    def obv(self):
        self.data['OBV'] = ta.obv(close=self.data.Close,volume=self.volume)
        return self.data

    def cmf(self):
        self.data['CMF'] = ta.cmf(high=self.data.High, low=self.data.Low, close=self.data.Close, volume=self.data.Volume)
        return self.data

