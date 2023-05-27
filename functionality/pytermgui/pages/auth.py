import pytermgui as ptg

from .abstract_page import (
    AbstractPage
)


class AuthPage(
    AbstractPage
):

    def get_window(self, manager: ptg.WindowManager) -> ptg.Window:
        return ptg.Window(
			ptg.Window(
            	ptg.Container(
					ptg.Window(
            	    	ptg.InputField(
            	        	"",
            	    	),
						title = "[210 bold]Username",
						box = "SINGLE",
					),
					ptg.Window(
            	    	ptg.InputField(
            	        	""
            	    	),
						title = "[210 bold]Password",
						box = "SINGLE",
					),
					ptg.Button(
						"Sign In"
					),
					ptg.Button(
						"Register"
					),
					box = "EMPTY"
            	),
            	title = "[210 bold]Authentication",
		 		box = "ROUNDED",
		 		static_width = 60,
		 		static_height = 30,
			).center(),
			box = "EMPTY",
        )
