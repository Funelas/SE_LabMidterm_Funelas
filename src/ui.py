import customtkinter as ctk
from calculator import Calculator

DISPLAY_PADDING = 16

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self._calc = Calculator()
        self._error_timer = None
        self._build_display()
        self._build_dial()

    def _build_display(self):
        # Sunken bevel effect via a darker outer frame + inner entry
        outer = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=6)
        outer.pack(padx=20, pady=(20, 8), fill="x")

        self.display = ctk.CTkEntry(
            outer,
            justify="right",
            font=ctk.CTkFont(size=28),
            fg_color="#2b2b2b",
            border_color="#111111",
            border_width=3,
            corner_radius=4,
            state="readonly",
        )
        self.display.pack(padx=DISPLAY_PADDING, pady=DISPLAY_PADDING, fill="x")

    def _set_display(self, value: str):
        if self._error_timer:
            self.after_cancel(self._error_timer)
            self._error_timer = None
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.insert(0, value)
        self.display.xview_moveto(1)
        self.display.configure(state="readonly")
        if value == "Error":
            self._error_timer = self.after(2000, lambda: self._set_display(self._calc.clear()))

    def _make_btn(self, parent, text, command, width=72, height=72, fg="#1D263B", hover="#5C6784"):
        return ctk.CTkButton(
            parent, text=text, width=width, height=height, command= command,
            font=ctk.CTkFont(size=20), fg_color=fg, hover_color=hover,
        )

    def _build_dial(self):
        dial = ctk.CTkFrame(self, fg_color="transparent")
        dial.pack(padx=20, pady=(8, 20))

        PAD = {"padx": 6, "pady": 6}
        OP  = {"fg": "#3B3355", "hover": "#6C5F8A"}
        AC  = {"fg": "#5C1A1A", "hover": "#8B2E2E"}

        def num(val):
            return lambda: self._set_display(self._calc.press_number(val))

        def op(val):
            return lambda: self._set_display(self._calc.press_operator(val))

        # Row 0: AC, DEL, *, /
        self._make_btn(dial, "AC",  **AC, command=lambda: self._set_display(self._calc.clear())).grid(row=0, column=0, **PAD)
        self._make_btn(dial, "DEL", **AC, command=lambda: self._set_display(self._calc.delete())).grid(row=0, column=1, **PAD)
        self._make_btn(dial, "*",  **OP, command=op("*")).grid(row=0, column=2, **PAD)
        self._make_btn(dial, "/",  **OP, command=op("/")).grid(row=0, column=3, **PAD)

        # Row 1: 7, 8, 9, +
        self._make_btn(dial, "7", command=num("7")).grid(row=1, column=0, **PAD)
        self._make_btn(dial, "8", command=num("8")).grid(row=1, column=1, **PAD)
        self._make_btn(dial, "9", command=num("9")).grid(row=1, column=2, **PAD)
        self._make_btn(dial, "+", **OP, command=op("+")).grid(row=1, column=3, **PAD)

        # Row 2: 4, 5, 6 | = spanning rows 2-3
        self._make_btn(dial, "4", command=num("4")).grid(row=2, column=0, **PAD)
        self._make_btn(dial, "5", command=num("5")).grid(row=2, column=1, **PAD)
        self._make_btn(dial, "6", command=num("6")).grid(row=2, column=2, **PAD)
        self._make_btn(dial, "-", **OP, command=op("-")).grid(row=2, column=3, **PAD)
        self._make_btn(dial, "=", height=156, **OP, command=lambda: self._set_display(self._calc.evaluate())).grid(row=3, column=3, rowspan=2, **PAD)

        # Row 3: 1, 2, 3
        self._make_btn(dial, "1", command=num("1")).grid(row=3, column=0, **PAD)
        self._make_btn(dial, "2", command=num("2")).grid(row=3, column=1, **PAD)
        self._make_btn(dial, "3", command=num("3")).grid(row=3, column=2, **PAD)

        # Row 4: 0 spanning cols 0-2
        self._make_btn(dial, "0", width=240, command=num("0")).grid(row=4, column=0, columnspan=3, **PAD)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CalculatorApp()
    app.mainloop()
