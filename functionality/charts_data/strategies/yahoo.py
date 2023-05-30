import yfinance

from pandas import DataFrame

from .abstract_strategy import (
    AbstractStrategy
)


class YahooStrategy(
    AbstractStrategy
):

    def get_index_list(self) -> list[str]:
        return [
            "NVDA",
            "TSLA",
            "PLTR",
            "AMD",
            "AI",
            "AMZN",
            "SOFI",
            "META",
            "SOXL",
            "MSFT",
            "INTC",
            "GOOG",
            "AAPL",
        ]

    def get_index_info(self, index: str):
        return yfinance.Ticker(index).info

    def get_index_stock_exchange_chart(self, index) -> DataFrame:
        return yfinance.download(
            index,
            self.start,
            self.end,
        )

    def get_index_actions_info(self, index: str) -> dict[str, DataFrame]:
        ticker = yfinance.Ticker(index)
        return {
            "actions": ticker.actions,
            "dividends": ticker.dividends,
            "splits": ticker.splits,
            "capital_gains" ticker.capital_gains,
        }

    def get_index_holders_info(self, index: str) -> dict[str, DataFrame]:
        ticker = yfinance.Ticker(index)
        return {
            "major": ticker.major_holders,
            "institutional": ticker.institutional_holders,
            "mutualfund": ticker.mutualfund_holders,
        }

    def get_index_earnings_info(self, index: str) -> dict[str, DataFrame]:
        """
            Show future and historic earnings dates,
            returns at most next 4 quarters and last 8 quarters by default.
        """
        ticker = yfinance.Ticker(index)
        return {
            "earnings_dates": ticker.earnings_dates
        }
