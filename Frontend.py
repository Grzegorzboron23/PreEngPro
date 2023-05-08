import tkinter
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

    ObjConfig1Btn = tkinter.Button(ObjConfigFrame, text="Config", width = 10)
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
    new = tkinter.Toplevel(root)
    new.geometry("260x250")
    new.title("Port selector")
    tkinter.Label(new, text="Select port:").grid(column=0,row=0,sticky=tkinter.W)
    tkinter.Label(new, text="Select baudrate:").grid(column=0, row=2, sticky=tkinter.W)
    # Port selector:
    FramePort = tkinter.Frame(new)
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



if __name__ == "__main__":
    FrontInit()