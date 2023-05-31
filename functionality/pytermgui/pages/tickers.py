import pytermgui as ptg

from .abstract_page import (
    AbstractPage
)

from ..assets.ports.charts_data import (
    ChartsDataPort
)


class TickersPage(
    AbstractPage
):

    __charts_data_port: ChartsDataPort = ChartsDataPort()

    __pagination: dict[str, int] = {
        "elements": 10,
    }

    def __init__(self) -> None:
        self.__tickers_list: list[ptg.Label] = []
        
        self.__index_info_list = None

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return self.__get_tickers_labels_list()

    def __get_tickers_labels_list(self) -> ptg.Window:

        labels_tuple: tuple[ptg.Label] = ()

        for elements in range(self.__pagination["elements"]):
            
            single_label = ptg.Label(
                "",
                width = 100,
            )

            self.__tickers_list.append(
                single_label
            )

            labels_tuple += (
                ptg.Window(
                    single_label,
                    box = "EMPTY_VERTICAL"
                ),
            )

        return ptg.Window(
            labels_tuple,
            title = f"{ self.styles['titles'] }Stock Exchange Tickers",
		 	box = "ROUNDED",
		)

    def update(self):

#        if self.__index_info_list == None:
#
#            yahoo_client = self.__charts_data_port.get_yahoo_data_getter()
#
#            self.__index_info_list: dict[str, dict] = {}
#
#            for index in yahoo_client.get_index_list():
#                index_info_dict = {
#                    index_info_dict,
#                    **{
#                        index: yaho_client.get_index_info(
#                            index = index
#                        )
#                    }
#                }

        i = 0
        for ticker_label in self.__tickers_list:
            i += 1
            ticker_label.value += f"[210 bold]INDEX [60 bold]up [230 bold] down { i }"
            
