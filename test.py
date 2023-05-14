import tkinter
from tkinter import ttk

def ConfigWindow():
    global root
    new = tkinter.Toplevel(root)
    new.geometry("400x300")
    new.title("Communication selector")
    notebook = ttk.Notebook(new)
    notebook.pack(fill='both', expand='yes')
    # add tabs for I2C, UART, and SPI
    i2c_frame = ttk.Frame(notebook)
    notebook.add(i2c_frame, text='I2C')
    uart_frame = ttk.Frame(notebook)
    notebook.add(uart_frame, text='UART')
    spi_frame = ttk.Frame(notebook)
    notebook.add(spi_frame, text='SPI')
    # add widgets to each tab
    tkinter.Label(i2c_frame, text="I2C communication").pack()
    tkinter.Label(uart_frame, text="UART communication").pack()
    tkinter.Label(spi_frame, text="SPI communication").pack()

def on_config_button_click():
    ConfigWindow()

root = tkinter.Tk()
ObjConfigFrame = tkinter.Frame(root)
ObjConfigFrame.pack()
ObjConfig1Btn = tkinter.Button(ObjConfigFrame, text="Config", width=10, command=on_config_button_click)
ObjConfig1Btn.grid(column=0, row=1, padx=2, pady=2)
root.mainloop()