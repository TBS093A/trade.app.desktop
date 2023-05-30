from pandas import DataFrame

from .utils.chart_types import (
    candlestick,
    ordinary,
)

from .utils.indicators import (
    IndicatorRSI,
    IndicatorMACD,
)


class ChartsFacade:

    def get_available_indicators_class_list(self) -> list[ordinary.AbstractOrdinaryChart]:
        return [
            IndicatorRSI,
            IndicatorMACD,
        ]

    def get_candlestick_chart(
        self, 
        data_frame: DataFrame, 
        title: str, 
        indicators_class: list[ordinary.AbstractOrdinaryChart]
    ) -> candlestick.AbstractCandlestickChart:
        return candlestick.AbstractCandlestickChart(
            data_frame = data_frame,
            title = title,
            indicators_class = indicators_class
        )
