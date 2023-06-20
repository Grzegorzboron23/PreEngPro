#Here is a list of functions, when called they return the array of bytes.
# CRC needs to be added, and they can be send
from Queue import Queue

CMD_SIZE = 10

def GlueCMD(arg0, arg1):
    data = bytearray([0])
    data.extend(arg0.to_bytes(4, 'little'))
    data.extend(arg1.to_bytes(4, 'little'))
    data.append(0)
    assert (len(data) == CMD_SIZE)
    return data

#Exemplary command:
def CMD_PING(arg0,arg1): #args were left for compatibility
    #Create arguments
    arg0 = 0xaa5555aa
    arg1 = 0xaa5555aa
    return GlueCMD(arg0,arg1)

def CMD_BLINK_LED():
    return CMD_PING()

def CMD_IF_SET_SPI(baudrate,duplex,CS,polar,MSswitch):
    arg0 = 0x00000000 | ( baudrate | (duplex<<8) | (CS<<16) | (polar<<24) | (MSswitch<<28) )
    arg1 = 0x00000000
    return GlueCMD(arg0,arg1)


#CMD higher than 63:

def CMD_RD_REG(RegAddr):
    return GlueCMD(RegAddr,0)

def CMD_WR_REG(RegAddr,RegData):
    return GlueCMD(RegAddr,RegData)

    def __init__(self):
        self.queue = Queue()  # Tworzenie instancji klasy Queue

    def add_command_to_queue(self, command):
        self.queue.add_command(command)

    def process_queue(self):
        removed_command = self.queue.remove_command()
        if removed_command:
            print("Usunięta komenda:", removed_command)

    def print_queue(self):
        queue_string = self.queue.get_queue_as_string()
        print("Stan kolejki:", queue_string)

if __name__ == "__main__":
    #Tu testujemy komendy:
    print(CMD_PING())
    print(CMD_IF_SET_SPI(5,1,0,1,1))
    print(CMD_WR_REG(0,2))