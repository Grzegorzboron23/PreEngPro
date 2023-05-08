import serial
import serial.tools.list_ports
import Definitions
import Backend

def SerialFindSerialDevices():
    ports = []
    for port in serial.tools.list_ports.comports():
        print(port.pid)
        if(port.pid == Definitions.PREENGDEV_PID):
            ports.append(port.name)
    return ports

def SerialAutoConnect():
    ports = SerialFindSerialDevices()
    print("SerialAutoConnect: Ports:", ports)
    if(len(ports) == 1):
        return Backend.SerialInit(ports[0])
    return False



