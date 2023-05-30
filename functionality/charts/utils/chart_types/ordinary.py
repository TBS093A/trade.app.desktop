from plotext
from pandas import DataFrame


class AbstractOrdinaryChart:

    chart_name: str = ""

    colors: list[int] = []

    def __init__(self, data_frame: DataFrame, theme: str = "matrix"):
        self.data = self.prepare_data(
            data_frame = data_frame
        )
        self.dates = plotext.datetimes_to_string(self.data_frame.index)
        self.theme = theme
        
    def prepare_data(self, data_frame: DataFrame):
        pass

    def prepare_plot(self):
        plotext.theme(
            self.theme
        )
        color_index = 0
        for data_set_key in self.data_frame.keys():
            plotext.plot(
                self.dates,
                self.data_frame[data_set_key],
                label = data_set_key,
                color = self.colors[color_index],
                marker = 'braille'
            )
            color_index += 1
        plotext.title(
            self.chart_name
        )
