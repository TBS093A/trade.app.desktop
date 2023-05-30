import plotext

from pandas import DataFrame

from .ordinary import (
    AbstractOrdinaryChart
)

from ..indicators import (
    IndicatorRSI,
    IndicatorMACD,
)


class AbstractCandlestickChart:

    __colors: list[int] = [39, 124]

    def __init__(
        self, 
        data_frame: DataFrame,
        title: str = "unknown",
        theme: str = "matrix",
        indicators_class: list[AbstractOrdinaryChart]
    ):
        """
            data_frame: DataFrame - data for candlestick chart - it must looks like example below:
                             Open        High        Low         Close       Adj Close  Volume
                Date                                                                            
                2020-01-02   67.077499   68.406998   67.077499   68.368500   68.368500  28132000
                2020-01-03   67.392998   68.625000   67.277199   68.032997   68.032997  23728000
                2020-01-06   67.500000   69.824997   67.500000   69.710503   69.710503  34646000
                2020-01-07   69.897003   70.149498   69.518997   69.667000   69.667000  30054000
                2020-01-08   69.603996   70.579002   69.542000   70.216003   70.216003  30560000
                ...                ...         ...         ...         ...         ...       ...
                2023-05-22  123.510002  127.050003  123.449997  125.870003  125.870003  29760200
                2023-05-23  124.930000  125.419998  123.050003  123.290001  123.290001  24477900
                2023-05-24  121.879997  122.750000  120.750000  121.639999  121.639999  23087900
                2023-05-25  125.209999  125.980003  122.900002  124.349998  124.349998  33812700
                2023-05-26  124.065002  126.000000  123.290001  125.430000  125.430000  25154700

            title: str - it's a title of defined chart
                
            theme: str - it's a theme for define style of chart (see plotext docs)

            indicators_class: AbstractOrdinaryChart - indicators who will be use with candlestick chart, example:

                [
                    IndicatorRSI,
                    IndicatorMACD,
                ]
        """
        self.__title = title
        self.__theme = theme

        self.__data = data_frame
        self.__dates = plotext.datetimes_to_string(self.__data.index)

        self.__indicators_class: list[AbstractOrdinaryChart] = indicators_class

    def __prepare_plot(self):
        plotext.theme(
            self.__theme
        )
        plotext.candlestick(
            self.__dates,
            self.__data,
            colors = self.__colors,
            label = f'{ self.__title } price',
        )
        plotext.title(
            self.__title
        )

    def show_plot_ordinary(self):
        self.__prepare_plot()
        plotext.show()

    def show_plot_with_indicators(self):
        plotext.clf()
        plotext.subplots(0, 1)
        plotext.subplot(0, 1).subplots(2, 1)
        plotext.subplot(0, 1).subplots(3, 1)

        plotext.subplot(0, 1).subplot(1, 1)
        self.__prepare_plot()

        subplot_index: int = 0
        for indicator_class in self.__indicators_class:
            subplot_index += 0

            plotext.subplot(0, 1).subplot(subplot_index, 1)
            plotext.subplot(0, 1).subplot(subplot_index, 1).plotsize(plotext.tw(), 15)

            indicator = indicator_class(
                data_frame = self.__data
            )
            indicator.prepare_plot()

        plotext.show()
