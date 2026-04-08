import customtkinter as ctk

DISPLAY_PADDING = 16

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
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

    def _make_btn(self, parent, text, width=72, height=72, fg="#1D263B", hover="#5C6784"):
        return ctk.CTkButton(
            parent, text=text, width=width, height=height,
            font=ctk.CTkFont(size=20), fg_color=fg, hover_color=hover,
        )

    def _build_dial(self):
        dial = ctk.CTkFrame(self, fg_color="transparent")
        dial.pack(padx=20, pady=(8, 20))

        PAD = {"padx": 6, "pady": 6}
        OP  = {"fg": "#3B3355", "hover": "#6C5F8A"}
        AC  = {"fg": "#5C1A1A", "hover": "#8B2E2E"}

        # Row 0: AC, DEL, /, *, -
        self._make_btn(dial, "AC",  **AC).grid(row=0, column=0, **PAD)
        self._make_btn(dial, "DEL", **AC).grid(row=0, column=1, **PAD)
        self._make_btn(dial, "/",  **OP).grid(row=0, column=2, **PAD)
        self._make_btn(dial, "*",  **OP).grid(row=0, column=3, **PAD)
        self._make_btn(dial, "-",  **OP).grid(row=0, column=4, **PAD)

        # Rows 1-2: 7-9 and 4-6 | + spanning both rows at col 3
        self._make_btn(dial, "7").grid(row=1, column=0, **PAD)
        self._make_btn(dial, "8").grid(row=1, column=1, **PAD)
        self._make_btn(dial, "9").grid(row=1, column=2, **PAD)
        self._make_btn(dial, "4").grid(row=2, column=0, **PAD)
        self._make_btn(dial, "5").grid(row=2, column=1, **PAD)
        self._make_btn(dial, "6").grid(row=2, column=2, **PAD)
        self._make_btn(dial, "+", width=156, height=156, **OP).grid(row=1, column=3, rowspan=2, columnspan=2, **PAD)

        # Row 3: 1, 2, 3 | Enter spanning cols 3-4
        self._make_btn(dial, "1").grid(row=3, column=0, **PAD)
        self._make_btn(dial, "2").grid(row=3, column=1, **PAD)
        self._make_btn(dial, "3").grid(row=3, column=2, **PAD)
        self._make_btn(dial, "Enter", width=156, **OP).grid(row=3, column=3, columnspan=2, **PAD)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CalculatorApp()
    app.mainloop()
