import pytermgui as ptg


class AbstractPage:

    assign: str = "body"

    styles: dict[str, str] = {
        "titles": "[210 bold]"
    }

    def __init__(self) -> None:
        pass

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window()

    def get_assign(self) -> str:
        return self.assign

