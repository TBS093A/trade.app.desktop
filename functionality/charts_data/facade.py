from .strategies import (
    abstract_strategy,
    yahoo,
)


class ChartsDataFacade:

    def get_period_enum(self) -> abstract_strategy.Period:
        return abstract_strategy.Period()

    def get_yahoo_data_getter(self, period: int = abstract_strategy.Period.2W) -> yahoo.YahooStartegy:
        return yahoo.YahooStrategy(
            period = period
        )
