from customtkinter import CTk, CTkFont

from MainFrame import MainFrame


class App(CTk):
    def __init__(self) -> None:
        super().__init__()

        # Config
        title = "Quadratic Equation Solver"
        icon_path = __file__ + "/../res/calc.ico"
        geometry = (660, 300)
        resizable = (False, False)
        global_font = CTkFont("Roboto", 30)

        # Configure the window
        self.title(title)
        self.wm_iconbitmap(icon_path)
        self.geometry("{}x{}".format(*geometry))
        self.minsize(*geometry)
        self.resizable(*resizable)

        # Create elements
        self._main_frame = MainFrame(self, global_font)

        self._display_elements()

    def _display_elements(self) -> None:
        """
        Display all window elements.
        """
        self._main_frame.pack(padx=10, pady=10, fill="both")

    def run(self) -> None:
        """
        Run the application.
        """
        self.mainloop()


if __name__ == '__main__':
    App().run()
