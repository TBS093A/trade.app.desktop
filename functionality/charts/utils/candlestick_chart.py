import plotext
import yfinance

from .indicators import (
    IndicatorRSI,
    IndicatorMACD,
)


class AbstractCandlestickChart:

    __indicators_class: list = [IndicatorRSI, IndicatorMACD]

    __colors: list[int] = [40, 124]

    def __init__(
        self, 
        data_frame,
        title: str = "unknown",
        theme: str = "matrix",
    ):
        self.__title = title
        self.__theme = theme

        self.__data = data_frame
        self.__dates = plotext.datetimes_to_string(self.__data.index)

    def __prepare_plot(self):
        plotext.theme(
            self.__theme
        )
        plotext.candlestick(
            self.__dates,
            self.__data,
            colors = self.__colors,
            label = f'{ self.title } price',
        )
        plotext.title(
            self.__title
        )

    def show_plot_ordinary(self):
        self.__prepare_plot()
        plotext.show()

    def show_plot_with_indicators(self):
        plotext.clf()
        plotext.subplots(1, 1)
        plotext.subplot(1, 1).subplots(2, 1)
        plotext.subplot(1, 1).subplots(3, 1)

        plotext.subplot(1, 1).subplot(1, 1)
        self.__prepare_plot()

        subplot_index: int = 1
        for indicator_class in self.__indicators_class:
            subplot_index += 1

            plotext.subplot(1, 1).subplot(subplot_index, 1)
            plotext.subplot(1, 1).subplot(subplot_index, 1).plotsize(plotext.tw(), 15)

            indicator = indicator_class(
                data = self.__data
            )
            indicator.prepare_plot()

        plotext.show()
