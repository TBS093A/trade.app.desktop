from datetime import date, timedelta 
from enum import Enum

from pandas import DataFrame


class Period(Enum):

    1D = 1
    5D = 5
    
    1W = 7
    2W = 7 * 2
    3W = 7 * 3
    
    1M = 30
    2M = 30 * 2
    3M = 30 * 3

    YTD = None

    1Y = 365
    2Y = 365 * 2
    3Y = 365 * 3

    MAX = None


class AbstractOrdinaryStockExchangeStrategy:

    def __init__(self, period: Period) -> None:
        
        self.start = self.__calculate_start_date(
            period = period
        )

        if end == None:
            self.end = f"{ date.today() }"

    def __calculate_start_date(self, period: Period) -> str:
        if period == Period.YTD:
            return f"{ date(date.today().year, 1, 1) }"
        if period == Period.MAX:
            return None
        return f"{ date.today() - timedelta(days = period.value) }"

    def get_index_list(self) -> list[str]:
        return

    def get_index_info(self, index: str) -> dict:
        return

    def get_index_news(self, index: str) -> dict:
        return

    def get_index_stock_exchange_chart(self, index: str) -> DataFrame:
        return

    def get_index_actions_info(self, index: str) -> dict[str, DataFrame]:
        return

    def get_index_holders_info(self, index: str) -> dict[str, DataFrame]:
        return

    def get_index_earnings_info(self, index: str) -> dict[str, DataFrame]:
        return
