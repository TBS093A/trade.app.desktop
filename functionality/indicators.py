import plotext
import pandas_ta


class AbstractIndicatorChart:

    indicator_name: str = ""

    colors: list[int] = []

    def __init__(self, data, theme: str = "matrix"):
        self.data = self.prepare_indicator(
            data = data
        )
        self.dates = plotext.datetimes_to_string(self.data.index)
        self.theme = theme
        
    def prepare_indicator(self):
        pass

    def prepare_plot(self):
        plotext.theme(
            self.theme
        )
        color_index = 0
        for data_set_key in self.data.keys():
            plotext.plot(
                self.dates,
                self.data[data_set_key],
                label = data_set_key,
                color = self.colors[color_index]
            )
            color_index += 1
        plotext.title(
            self.indicator_name
        )


class IndicatorRSI(
    AbstractIndicatorChart
):
   
    indicator_name: str = "RSI"

    colors: list[int] = [33]

    def prepare_indicator(self, data):
        return pandas_ta.rsi(
            data['Close']
        )

    def prepare_plot(self):
        plotext.theme(
            self.theme
        )
        plotext.date_form('d/m/Y')
        plotext.plot(
            self.dates,
            list(self.data),
            color = self.colors[0]
        )
        plotext.title(
            self.indicator_name
        )

class IndicatorMACD(
    AbstractIndicatorChart
):

    indicator_name: str = "MACD"

    colors: list[int] = [135, 165, 207]

    def prepare_indicator(self, data):
       return pandas_ta.macd(
           data['Close']
       )
