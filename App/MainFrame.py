from customtkinter import CTk, CTkFont, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkTextbox
from decimal import Decimal
from typing import Any

from Utils import solve


class MainFrame(CTkFrame):
    def __init__(self, master: CTk, elements_font: CTkFont = None) -> None:
        super().__init__(master, fg_color="transparent")

        # Create elements
        self._info_label = CTkLabel(self, text="Enter 3 coefficients", font=elements_font)

        self._input_frame = CTkFrame(self, fg_color="transparent")  # Invisible element for grouping
        self._a_entry = \
            CTkEntry(self._input_frame, width=155, placeholder_text="0", font=elements_font, justify='right')
        self._part1_label = CTkLabel(self._input_frame, text=" x² + ", font=elements_font)
        self._b_entry = \
            CTkEntry(self._input_frame, width=155, placeholder_text="0", font=elements_font, justify='right')
        self._part2_label = CTkLabel(self._input_frame, text=" x + ", font=elements_font)
        self._c_entry = \
            CTkEntry(self._input_frame, width=155, placeholder_text="0", font=elements_font, justify='right')
        self._part3_label = CTkLabel(self._input_frame, text=" = 0", font=elements_font)

        self._output_frame = CTkFrame(self, fg_color="transparent")
        self._x1_label = CTkLabel(self._output_frame, text="X₁ = ", font=elements_font)
        self._x1_textbox = \
            CTkTextbox(self._output_frame, width=570, height=7, font=elements_font, state='disabled')  # readonly
        self._x2_label = CTkLabel(self._output_frame, text="X₂ = ", font=elements_font)
        self._x2_textbox = \
            CTkTextbox(self._output_frame, width=570, height=7, font=elements_font, state='disabled')  # readonly

        self._ok_button = CTkButton(self, text="OK", command=self._ok_button_click, font=elements_font)

        # Configure elements
        self._bind_elements()
        self._display_elements()

    def _bind_elements(self) -> None:
        """
        Bind the keyboard keys to the elements.
        """
        self._a_entry.bind("<Return>", lambda event=None: self._b_entry.focus())
        self._b_entry.bind("<Return>", lambda event=None: self._c_entry.focus())
        self._c_entry.bind("<Return>", lambda event=None: self._ok_button_click())
        # <Return> is Enter on the keyboard
        # lambda generates a function with an event variable as input to avoid an error

    def _display_elements(self) -> None:
        """
        Display all frame elements.
        """
        self._info_label.pack()

        self._input_frame.pack(pady=10)
        for el, column in zip(
                (self._a_entry, self._part1_label, self._b_entry, self._part2_label, self._c_entry, self._part3_label),
                range(0, 6)):
            el.grid(column=column, row=0)

        self._output_frame.pack()
        for el, column, row in zip(
                (self._x1_label, self._x1_textbox, self._x2_label, self._x2_textbox), (0, 1, 0, 1), (0, 0, 1, 1)):
            el.grid(column=column, row=row, pady=5)

        self._ok_button.pack(fill="x", pady=[5, 0])  # upper y-axis padding = 5px

    def _set_output(self, text1: Any, text2: Any) -> None:
        """
        Set the text in the output textboxes.
        :param text1: first textbox text.
        :param text2: second textbox text.
        """
        for text, textbox in zip((text1, text2), (self._x1_textbox, self._x2_textbox)):
            textbox.configure(state="normal")
            textbox.delete(1.0, "end")
            textbox.insert(1.0, str(text))
            textbox.configure(state="disabled")

    def _ok_button_click(self) -> None:
        """
        Put calculation results into the entry.
        """
        a, b, c = Decimal(self._a_entry.get()), Decimal(self._b_entry.get()), Decimal(self._c_entry.get())  # Get input
        result = solve(a, b, c)  # Calculate result
        if result is None:
            self._set_output("No solution!", "No solution!")
        else:
            self._set_output(*result)
