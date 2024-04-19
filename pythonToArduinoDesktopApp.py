#================================================================
#   In this file:
#       ->Connect and send data to arduino uno through ports
#       ->Display simple desktop window to control actions
#================================================================

#===============================IMPORTS==========================
import PySimpleGUI as sg
import serial.tools.list_ports

#===============================PORT STUFF=======================
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input("Selected Com Port for Arduino #: ")

for i in range(len(portsList)):
    if(portsList[i].startswith("COM" + str(com))):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

#===============================WINDOW LAYOUT======================
layout = [
    [sg.Button('ON', key='-ON-', expand_x=True)],
    [sg.Button('OFF', key='-OFF-', expand_x=True)],
    [sg.Button('EXIT', key='-EXIT-', expand_x=True)]
    ]

window = sg.Window('Project Menu',
                   layout,
                   size = (300,300),
                   )

#===============================MAIN WINDOW LOOP====================
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ['-ON-']:
        command = "ON"
        serialInst.write(command.encode('utf-8'))
    if event in ['-OFF-']:
        command = "OFF"
        serialInst.write(command.encode('utf-8'))
    if event in ['-EXIT-']:
        exit()

window.close() 