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
        "elements": 50,
    }

    __single_index_labels_count: int = 5

    def __init__(self) -> None:
        self.__tickers_list: list[list[ptg.Label]] = []
        
        self.__index_info_list = None

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return self.__get_tickers_labels_list()

    def __get_tickers_labels_list(self) -> ptg.Window:

        tickers_window: ptg.Window = ptg.Window(
            title = f"{ self.styles['titles'] }Stock Exchange Tickers",
		 	box = "ROUNDED",
            overflow = ptg.Overflow.SCROLL,
		)

        for label in self.____generate_tickers_labels():
            
            tickers_window.lazy_add(
                label
            )

        return tickers_window

    def ____generate_tickers_labels(self) -> ptg.Container:

        for _ in range(self.__pagination['elements']):
            
            single_index_container: ptg.Splitter = ptg.Splitter()

            index_labels = []


            for label_id in range(self.__single_index_labels_count):                

                single_label = ptg.Label(
                    "",
                    width = int(100 / self.__single_index_labels_count),
                    parent_align = ptg.HorizontalAlignment.LEFT,
                )

                index_labels.append(
                    single_label
                ) 
    
                single_index_container.lazy_add(
                    single_label
                )
            
            self.__tickers_list.append(
                index_labels
            )

            yield ptg.Container(
                single_index_container,
                box = "EMPTY_VERTICAL",
            )


    def update(self):

        if True:
 
            yahoo_client = self.__charts_data_port.get_yahoo_data_getter()
 
            self.__index_info_dict: dict[str, dict] = {}
 
            for index in yahoo_client.get_index_list():
                self.__index_info_dict = {
                    **self.__index_info_dict,
                    **{
                        index: yahoo_client.get_index_info(
                            index = index
                        )
                    }
                }

        for ticker_container in self.__tickers_list:

            for index, info in self.__index_info_dict.items():

                data_map = [
                    f"[white bold]{ index }",
                    f"[gray bold]{ info['shortName'] }",
                    f"[red bold]\ { info['dayLow'] }",
                    f"[green bold]/ { info['dayHigh'] }",
                    f"[gray bold]V { info['volume'] }",
                ]

                data_map.reverse()

                for ticker_label in ticker_container:
                
                    ticker_label.value = data_map.pop()

                del data_map

                del self.__index_info_dict[index]

                break 
            
