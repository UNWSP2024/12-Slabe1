import tkinter

class my_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.input_frame = tkinter.Frame(self.main_window)
        self.rate_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.minutes_label = tkinter.Label(self.input_frame, text="Minutes:")
        self.minutes_entry = tkinter.Entry(self.input_frame)
        self.rate_value = tkinter.StringVar(value="daytime")

        self.daytime_radio = tkinter.Radiobutton(
            self.rate_frame,
            text="Daytime ($0.02/min)",
            variable=self.rate_value,
            value="daytime",
        )
        self.evening_radio = tkinter.Radiobutton(
            self.rate_frame,
            text="Evening ($0.12/min)",
            variable=self.rate_value,
            value="evening",
        )
        self.offpeak_radio = tkinter.Radiobutton(
            self.rate_frame,
            text="Off-Peak ($0.05/min)",
            variable=self.rate_value,
            value="offpeak",
        )

        self.total_value = tkinter.StringVar(value="$0.00")
        self.total_label = tkinter.Label(self.button_frame, text="Total charge:")
        self.total_display = tkinter.Label(self.button_frame, textvariable=self.total_value)

        self.calculate_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text='quit', command=self.main_window.destroy)

        self.input_frame.pack(side='left')
        self.rate_frame.pack(side='right')
        self.button_frame.pack(side='bottom')

        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        self.daytime_radio.pack(anchor='w')
        self.evening_radio.pack(anchor='w')
        self.offpeak_radio.pack(anchor='w')

        self.total_label.pack(side='left')
        self.total_display.pack(side='left')
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.main_window.mainloop()

    def calculate(self):
        try:
            minutes = float(self.minutes_entry.get())
        except ValueError:
            self.total_value.set("Invalid minutes")
            return

        rate = {
            "daytime": 0.02,
            "evening": 0.12,
            "offpeak": 0.05,
        }[self.rate_value.get()]

        total = minutes * rate
        self.total_value.set(f"${total:.2f}")


if __name__ == '__main__':
    gui = my_GUI()
