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

    def _build_dial(self):
        dial = ctk.CTkFrame(self, fg_color="transparent")
        dial.pack(padx=20, pady=(8, 20))

        rows = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
        ]

        for row_idx, row in enumerate(rows):
            for col_idx, label in enumerate(row):
                btn = ctk.CTkButton(
                    dial,
                    text=label,
                    width=72,
                    height=72,
                    font=ctk.CTkFont(size=20),
                )
                btn.grid(row=row_idx, column=col_idx, padx=6, pady=6)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CalculatorApp()
    app.mainloop()
