import tkinter

class my_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.gas_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.gas_label = tkinter.Label(self.gas_frame, text="Gallons of gas:")
        self.gas_value = tkinter.Entry(self.gas_frame)
        self.miles_label = tkinter.Label(self.miles_frame, text="Miles driven:")
        self.miles_value = tkinter.Entry(self.miles_frame)
        self.mileage_value = tkinter.StringVar()

        self.mileage_label = tkinter.Label(self.button_frame, textvariable= self.mileage_value)

        self.calculate_button = tkinter.Button(self.button_frame, text= 'Calculate', command= self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text= 'quit', command= self.main_window.destroy)

        self.button_frame.pack(side='bottom')
        self.gas_frame.pack(side='left')
        self.miles_frame.pack(side='right')

        self.gas_label.pack(side='left')
        self.gas_value.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_value.pack(side='left')

        self.mileage_label.pack(side='left')
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.main_window.mainloop()

    def calculate(self):
        self.mileage_value.set(float(self.miles_value.get()) / float(self.gas_value.get()))

if __name__ == '__main__':
    gui = my_GUI()