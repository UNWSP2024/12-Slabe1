import tkinter

class my_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

        self.check_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()

        self.oil_check = tkinter.Checkbutton(self.check_frame, text="Oil Change - $30.00", variable=self.oil_var)
        self.lube_check = tkinter.Checkbutton(self.check_frame, text="Lube Job - $20.00", variable=self.lube_var)
        self.radiator_check = tkinter.Checkbutton(self.check_frame, text="Radiator Flush - $40.00", variable=self.radiator_var)
        self.transmission_check = tkinter.Checkbutton(self.check_frame, text="Transmission Fluid - $100.00", variable=self.transmission_var)
        self.inspection_check = tkinter.Checkbutton(self.check_frame, text="Inspection - $35.00", variable=self.inspection_var)
        self.muffler_check = tkinter.Checkbutton(self.check_frame, text="Muffler replacement - $200.00", variable=self.muffler_var)
        self.tire_check = tkinter.Checkbutton(self.check_frame, text="Tire Rotation - $20.00", variable=self.tire_var)

        self.total_value = tkinter.StringVar()
        self.total_label = tkinter.Label(self.button_frame, text="Total charges:")
        self.total_display = tkinter.Label(self.button_frame, textvariable=self.total_value)

        self.calculate_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text='quit', command=self.main_window.destroy)

        self.oil_check.pack(anchor='w')
        self.lube_check.pack(anchor='w')
        self.radiator_check.pack(anchor='w')
        self.transmission_check.pack(anchor='w')
        self.inspection_check.pack(anchor='w')
        self.muffler_check.pack(anchor='w')
        self.tire_check.pack(anchor='w')

        self.check_frame.pack(side='left')
        self.button_frame.pack(side='right')

        self.total_label.pack(side='left')
        self.total_display.pack(side='left')
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.main_window.mainloop()

    def calculate(self):
        total = (
            self.oil_var.get() * 30
            + self.lube_var.get() * 20
            + self.radiator_var.get() * 40
            + self.transmission_var.get() * 100
            + self.inspection_var.get() * 35
            + self.muffler_var.get() * 200
            + self.tire_var.get() * 20
        )
        self.total_value.set(f"${total:.2f}")


if __name__ == '__main__':
    gui = my_GUI()
    