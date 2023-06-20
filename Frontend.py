import tkinter
from msilib.schema import ComboBox
from tkinter import ttk
import BackendConnect


#for backend calls:
import Commands
import Backend

# Objects:
ObjTextCMD = 0
ObjTextData = 0

ObjInfoFrame = 0
ObjCMD1 = 0
ObjCMD2 = 0
ObjCMD3 = 0
ObjCMD1Btn = 0
ObjCMD2Btn = 0
ObjCMD3Btn = 0

ObjConfigFrame = 0
ObjConfigLabel = 0
ObjConfig1Btn = 0
ObjConfig2Btn = 0
ObjConfig3Btn = 0
ObjConfig4Btn = 0


root = tkinter.Tk(className=' Projekt zespołowy - Interfejs USB <-> IIC,UART,SPI v0.1')

def FrontInit():
    global root
    frm = ttk.Frame(root, padding=10)
    root.geometry("800x330")

    #
    # The grid will be 2x2
    # Upper are two text boxes
    # Lower are two menues, left with data to be send, right with selections
    #

    #Objects:
    global ObjTextCMD
    global ObjTextData

    global ObjInfoFrame
    global ObjCMD1
    global ObjCMD2
    global ObjCMD3
    global ObjCMD1Btn
    global ObjCMD2Btn
    global ObjCMD3Btn

    global ObjConfigFrame
    global ObjConfigLabel
    global ObjConfig1Btn
    global ObjConfig2Btn
    global ObjConfig3Btn
    global ObjConfig4Btn

    #Descriptions:

    tkinter.Label(root,text="Data: ",font=("Arial", 20)).grid(column = 0, row = 0, padx = 5, pady = 0,sticky=tkinter.W)
    tkinter.Label(root,text="Status: ",font=("Arial", 20)).grid(column=1, row= 0, padx=5, pady=0,sticky=tkinter.W)

    #data text:
    ObjTextCMD = tkinter.Text(root, height = 10, width = 24)
    ObjTextCMD.grid(column=1, row=1, padx=5, pady=5)

    #command text:
    ObjTextData = tkinter.Text(root, height = 10, width = 60)
    ObjTextData.grid(column=0, row=1, padx=5, pady=5, ipadx= 50)

    #input objects:
    ObjInfoFrame = tkinter.Frame(root,bd = 5)
    ObjInfoFrame.grid(column=0, row=2, padx=0, pady=0,columnspan= 2, sticky=tkinter.W)


    FRAME_LEN = 40

    ObjCMD1 = tkinter.Text(ObjInfoFrame, height=1, width=FRAME_LEN)
    ObjCMD2 = tkinter.Text(ObjInfoFrame, height=1, width=FRAME_LEN)
    ObjCMD3 = tkinter.Text(ObjInfoFrame, height=1, width=FRAME_LEN)
    ObjCMD1Btn = tkinter.Button(ObjInfoFrame, text="Send!")
    ObjCMD2Btn = tkinter.Button(ObjInfoFrame, text="Send!")
    ObjCMD3Btn = tkinter.Button(ObjInfoFrame, text="Send!")
    ObjCMD1.grid(column=0, row=0, padx=2, pady=2)
    ObjCMD2.grid(column=0, row=1, padx=2, pady=2)
    ObjCMD3.grid(column=0, row=2, padx=2, pady=2)
    ObjCMD1Btn.grid(column=1, row=0, padx=2, pady=2)
    ObjCMD2Btn.grid(column=1, row=1, padx=2, pady=2)
    ObjCMD3Btn.grid(column=1, row=2, padx=2, pady=2)

    #output object:
    ObjConfigFrame = tkinter.Frame(root, bd=5)
    ObjConfigFrame.grid(column=1, row=2, padx=0, pady=0)

    ObjConfigLabel = tkinter.Label(ObjConfigFrame,text= "Połączono z ...ect")
    ObjConfigLabel.grid(row=0, column=0, columnspan=2)

    ObjConfig1Btn = tkinter.Button(ObjConfigFrame, text="Config", width = 10, command=ConfigWindow)
    ObjConfig1Btn.grid(column=0, row=1, padx=2, pady=2)

    ObjConfig2Btn = tkinter.Button(ObjConfigFrame, text="Port", width = 10, command=PortWindow)
    ObjConfig2Btn.grid(column=1, row=1, padx=2, pady=2)

    ObjConfig3Btn = tkinter.Button(ObjConfigFrame, text="Ping", width = 10, command=lambda : Backend.SerialSendCMD(Commands.CMD_PING(0,0)))
    ObjConfig3Btn.grid(column=0, row=2, padx=2, pady=2)

    ObjConfig4Btn = tkinter.Button(ObjConfigFrame, text="Exit", command=root.destroy, width = 10)
    ObjConfig4Btn.grid(column=1, row=2, padx=2, pady=2)


    #ttk.Label(frm, text="Connected to "+Backend.SerialGet().name ).grid(column=0, row=0)
    root.mainloop()

#Gettert / settery:

def FrontSetPort(port):
    global ObjConfigLabel
    if(type(port) == str):

        ObjConfigLabel.config(text = "Open port: " + port, fg = "black")
    else:
        ObjConfigLabel.config(text="Port is closed", fg = "red")


def PortWindow(): #button to be set inactive
    global root
    global ObjConfig2Btn
    ObjConfig2Btn['state'] = tkinter.DISABLED
    #todo: Preserve against running more than one config at a time
    new = tkinter.Toplevel(root) #okno
    new.geometry("260x250") #parametry okna
    new.title("Port selector") #label
    tkinter.Label(new, text="Select port:").grid(column=0,row=0,sticky=tkinter.W) #opis
    tkinter.Label(new, text="Select baudrate:").grid(column=0, row=2, sticky=tkinter.W)#drugi opis
    # Port selector:
    FramePort = tkinter.Frame(new) #dwa przyciski w jednym poziomie
    FramePort.grid(column=0,row=1,sticky=tkinter.E)
    ComboBox = ttk.Combobox(FramePort)
    PortWindowRefresh(ComboBox)
    ComboBox.pack()


    #add the buttons:
    FrameBtns = tkinter.Frame(new)
    FrameBtns.grid(column=0,row=4)
    tkinter.Button(FrameBtns,text="Scan ports",width=10,padx=10,command= lambda : PortWindowRefresh(ComboBox)).grid(row=0,column=0, padx=14)
    tkinter.Button(FrameBtns, text="Apply",width=10,padx=10, command= lambda : PortWindowApply(0,ComboBox.get(),new)).grid(row=0, column=1, padx=14)
    #Create a List:
    #Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)


def ConfigWindow(): #button to be set inactive, at the top
    global root
    global ObjConfig1Btn
    ObjConfig1Btn['state'] = tkinter.DISABLED
    new = tkinter.Toplevel(root) #tworzenie okna
    new.geometry("380x280") #tworzenie wymiarów okna
    new.title("Communication selector") #label
    notebook = ttk.Notebook(new) #tworzenie notebooka który umożliwi zrobić zakładki
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
    i2c_apply_btn = tkinter.Button(i2c_frame, text="Apply" , command=lambda: handle_buttons("i2c")) #apply button
    i2c_apply_btn.pack(side='top')


    tkinter.Label(uart_frame, text="UART communication").pack()
    uart_apply_btn = tkinter.Button(uart_frame, text="Apply", command=lambda: handle_buttons("uart_apply_btn")) #apply button
    uart_apply_btn.pack(side='top')


    # dodanie nowych okien do wyboru CPOL vs CPHA, Slave vs Master, Half-duplex vs Full-duplex
    # add radio buttons to the SPI tab
    tkinter.Label(spi_frame, text="SPI communication").grid(row=0, column=0, sticky=tkinter.W)
    cpol_cpha_frame = ttk.Frame(spi_frame)
    cpol_cpha_frame.grid(row=1, column=0, sticky=tkinter.W)
    cpol_label = tkinter.Label(cpol_cpha_frame, text="Clock polarity (CPOL):")
    cpol_label.pack(side='left')
    cpol_var = tkinter.StringVar()
    cpol_var.set("0")
    cpol_r1 = tkinter.Radiobutton(cpol_cpha_frame, text="0", variable=cpol_var, value="0")
    cpol_r1.pack(side='left')
    cpol_r2 = tkinter.Radiobutton(cpol_cpha_frame, text="1", variable=cpol_var, value="1")
    cpol_r2.pack(side='left')
    cpha_label = tkinter.Label(cpol_cpha_frame, text="Clock phase (CPHA):")
    cpha_label.pack(side='left')
    cpha_var = tkinter.StringVar()
    cpha_var.set("0")
    cpha_r1 = tkinter.Radiobutton(cpol_cpha_frame, text="0", variable=cpha_var, value="0")
    cpha_r1.pack(side='left')
    cpha_r2 = tkinter.Radiobutton(cpol_cpha_frame, text="1", variable=cpha_var, value="1")
    cpha_r2.pack(side='left')

    slave_master_frame = ttk.Frame(spi_frame)
    slave_master_frame.grid(row=2, column=0, sticky=tkinter.W)
    slave_label = tkinter.Label(slave_master_frame, text="Slave or Master:")
    slave_label.pack(side='left')
    slave_var = tkinter.StringVar()
    slave_var.set("slave")
    slave_r1 = tkinter.Radiobutton(slave_master_frame, text="Slave", variable=slave_var, value="slave")
    slave_r1.pack(side='left')
    master_r2 = tkinter.Radiobutton(slave_master_frame, text="Master", variable=slave_var, value="master")
    master_r2.pack(side='left')
    # add half-duplex vs full-duplex radiobuttons
    duplex_frame = ttk.Frame(spi_frame)
    duplex_frame.grid(row=3, column=0, sticky=tkinter.W)
    duplex_label = tkinter.Label(duplex_frame, text="Half-duplex or Full-duplex:")
    duplex_label.pack(side='left')
    duplex_var = tkinter.StringVar()
    duplex_var.set("half-duplex")
    half_duplex_r1 = tkinter.Radiobutton(duplex_frame, text="Half-duplex", variable=duplex_var, value="half-duplex")
    half_duplex_r1.pack(side='left')
    full_duplex_r2 = tkinter.Radiobutton(duplex_frame, text="Full-duplex", variable=duplex_var, value="full-duplex")
    full_duplex_r2.pack(side='left')


    # add the apply button
    spi_apply_btn = tkinter.Button(spi_frame, text="Apply", width=10, padx=10,command= lambda : PortWindowApply(0,ComboBox.get(),new)).grid(row=4, column=0, padx=14)






def PortWindowApply(SelectedBoudrate,SelectedPort,WindowToKill):
    global ObjConfig2Btn
    try:
        Backend.SerialInit(SelectedPort,SelectedBoudrate)
        WindowToKill.destroy()
        ObjConfig2Btn['state'] = tkinter.NORMAL
    except(BaseException):
        print("PortWindowApply: Wrong port arguments!")


def PortWindowRefresh(ComboBox):
    Ports = BackendConnect.SerialFindSerialDevices()  # can be changed to use the refresh button.

    if(len(Ports) > 0):
        ComboBox.config(values=Ports)
    else:
        ComboBox.config(values=["Device not found"])
    ComboBox.current(0)
    return

def handle_buttons(btn):
    # Wykonaj działanie po kliknięciu przycisku konkretnego
    if btn == "uart_apply_btn":
        print("Przycisk uart_apply_btn został kliknięty!")
    elif  btn =="i2c":
        print("Przycisk i2c_btn został kliknięty!")






if __name__ == "__main__":
    FrontInit()
