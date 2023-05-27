import pytermgui as ptg


class Section:

    assign: str = ""

    height: float = 0
    width: float = 0

    def __init__(self):
        pass

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window()

    def get_assign(self) -> str:
        return self.assign

    def get_height(self) -> float:
        return self.height

    def get_width(self) -> float:
        return self.width


class Header(
    Section
):

    assign: str = "header"

    height: float = 0.03
    width: float = None

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window(
            "trade app desktop",
            box = "EMPTY",
            is_persistant = True,
        )


class Body(
    Section
):

    assign: str = "body"

    height: float = 0.97
    width: float = None

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window(
            "Body",
            box = "ROUNDED",
            title = "Body"
        )


class Footer(
    Section
):

    assign: str = "footer"

    height: float = 0.03
    width: float = None
    
    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window(
            ptg.Button("Quit", lambda *_: self.__confirm_quit(manager = manager)),
            box = "EMPTY"
        )

    def __confirm_quit(self, manager: ptg.WindowManager) -> None:
        
        modal = ptg.Window(
            "Are you sure you want to quit?",
            "",
            ptg.Container(
                ptg.Splitter(
                    ptg.Button("Yes", lambda *_: manager.stop()),
                    ptg.Button("No", lambda *_: modal.close()),
                ),
            ),
        ).center()

        modal.select(1)
        manager.add(modal)

