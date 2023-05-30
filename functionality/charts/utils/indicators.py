import plotext
import pandas_ta

from .chart_types.ordinary import (
    AbstractOrdinaryChart
)

class IndicatorRSI(
    AbstractOrdinaryChart
):
   
    chart_name: str = "RSI"

    colors: list[int] = [33]

    def prepare_data(self, data_frame: DataFrame):
        return pandas_ta.rsi(
            data_frame['Close']
        )

    def prepare_plot(self):
        plotext.theme(
            self.theme
        )
        plotext.date_form('d/m/Y')
        plotext.plot(
            self.dates,
            list(self.data_frame),
            color = self.colors[0],
            marker = 'braille'
        )
        plotext.title(
            self.chart_name
        )

class IndicatorMACD(
    AbstractOrdinaryChart
):

    chart_name: str = "MACD"

    colors: list[int] = [135, 165, 207]

    def prepare_data(self, data_frame: DataFrame):
       return pandas_ta.macd(
           data_frame['Close']
       )
