import pytermgui as ptg

from .layout import (
    sections
)

from .pages import (
    auth,
    chart,
    tickers,
)

from .styles.general import (
    STYLES
)


class IndexPage:

    layout: dict = {
        sections.Header(): True,
        sections.Body(): True,
        sections.Footer(): True,
    }

    pages: dict = {
		# auth.AuthPage(): True,
        tickers.TickersPage(): True,
    }

    def __init__(self):
        self.__load_windows()

    def __load_windows(self):
        with ptg.WindowManager() as manager:

            manager.layout = self.____define_layout()

            self.____load_styles()

            for section, is_visible in self.layout.items():
                if is_visible:
                    manager.add(
                        section.get_window(
                            manager = manager
                        ),
                        assign = section.get_assign()
                    )

            for page, is_visible in self.pages.items():
                if is_visible:
                    manager.add(
                        page.get_window(
                            manager = manager
                        ),
                        assign = page.get_assign()
                    )
                    page.update()

    def ____define_layout(self) -> ptg.Layout:
        layout = ptg.Layout()

        for section, is_visible in self.layout.items():

            layout.add_slot(
                section.get_assign(), 
                height = section.get_height(),
                width = section.get_width()
            ) 
            layout.add_break()

        return layout

    def ____load_styles(self) -> None:
        with ptg.YamlLoader() as loader:
            loader.load(STYLES)
