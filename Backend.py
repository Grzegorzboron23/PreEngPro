#The idea is to put an array of characters by a command make function,
#then, serialize it to bytes and send through a serial port

import serial
import HelpfulFunctions as HF


#Global variable
serialPort = False

def SerialInit(path:str, baud:int):
    global serialPort
    if baud == 0:
        baud = 115200
    try:
        serialPort = serial.Serial(path,baud) #TODO: put more arguments.
        if(serialPort.isOpen()):
            print("SerialInit: Serial is open!")
            return serialPort
        print("SerialInit: Failed to open the port",path)
        return False
    except( BaseException ): #TODO: Distingush the exceptions.
        print("SerialInit: serial.Serial has thrown an exception!")
    return False


def SerialSendCMD(command: bytearray):
    global serialPort
    #append the CRC:
    CRC = HF.CRC8(command,len(command)-1)
    command[len(command)-1] = CRC

    #send the command:
    try:
        serialPort.write(command)
    except (serial.SerialException):
        print("SerialSendCMD: SerialException!")
        #FrontSetPort(0)
    return

def SerialGet():
    global serialPort
    return serialPort