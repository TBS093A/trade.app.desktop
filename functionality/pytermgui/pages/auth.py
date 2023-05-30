import pytermgui as ptg

from .abstract_page import (
    AbstractPage
)


class AuthPage(
    AbstractPage
):

    def __init__(self) -> None:
        pass

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window(
            ptg.Splitter(
                ptg.Window(
                    ptg.DensePixelMatrix(
                        default = "red",
                        width = 30,
                        height = 17,
                    ),
                    height = 25,
                    width = 100,
                    box = "EMPTY",
                ),
                ptg.Window(
                    self.__get_authentication_form()[0],
                    height = 25,
                    width = 100,
                    box = "EMPTY",
                ),
            ),
			box = "EMPTY",
        )

    def __swap_auth_forms(self) -> tuple:
        if self.is_authentication:
            self.__active_form = self.__get_authentication_form()
        else:
            return self.__get_authorization_form()

    def __get_authentication_form(self) -> tuple:
        return ptg.Window(
            ptg.Container(
			    ptg.Window(
                    ptg.InputField(
                     	"",
                    ),
			        title = f"{ self.styles['titles'] }Username",
			        box = "SINGLE",
			    ),
			    ptg.Window(
                    ptg.InputField(
                     	""
                    ),
			        title = f"{ self.styles['titles'] }Password",
			        box = "SINGLE",
			    ),
                ptg.Splitter(
			        ptg.Button(
			         	"Sign In",
			        ),
			        ptg.Button(
			         	"Register",
                        lambda *_: self.set_is_authentication(False),
			        ),
                ),
			    box = "EMPTY"
            ),
            title = f"{ self.styles['titles'] }Authentication",
		 	box = "ROUNDED",
		 	static_width = 60,
		 	static_height = 30,
		),

    def __get_authorization_form(self) -> tuple:
        return ptg.Window(
            ptg.Container(
			    ptg.Window(
                    ptg.InputField(
                     	"",
                    ),
			        title = f"{ self.styles['titles'] }Username",
			        box = "SINGLE",
			    ),
			    ptg.Window(
                    ptg.InputField(
                     	"",
                    ),
			        title = f"{ self.styles['titles'] }E-mail",
			        box = "SINGLE",
			    ),
			    ptg.Window(
                    ptg.InputField(
                     	""
                    ),
			        title = f"{ self.styles['titles'] }Password",
			        box = "SINGLE",
			    ),
                ptg.Splitter(
			        ptg.Button(
			         	"Register",
			        ),
			        ptg.Button(
			         	"Back To Login",
                        lambda *_: self.set_is_authentication(True),
			        ),
                ),
			    box = "EMPTY"
            ).center(),
            title = f"{ self.styles['titles'] }Authorization",
		 	box = "ROUNDED",
		 	static_width = 60,
		 	static_height = 30,
		),

    def set_is_authentication(self, value: bool) -> None:
        self.is_authentication = value

