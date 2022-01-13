# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()import machine
import machine
import time
import network
import os
import paho.mqtt as mqttclient

Connected = False
broker_adress = "151.106.113.229"
port1= 1883
user = "greekindo"
password = "@greekindo123"


uart = machine.UART(2, 115200)
strMsg = ''
mode = ""
sta_if = network.WLAN(network.STA_IF)
config_array = ['','','','']

def on_connect(client, usedata,flags,rc):
    if rc==0:
        print("Client is connected")
        global Connected
        Connected = True
        client.subscribe("TEST")
    else:
        print("Connection Failed")
def on_message(client, userdata, msg):
    global ReceiveData
    print(str(msg.payload))
    ReceiveData = msg.payload

while True:
    f = open("config.txt", "a")
    f = open("config.txt", "r")
    config_array = f.readlines()
    print(config_array)
    sta_if.active(True)
    sta_if.connect("ac55", "201106001")
    if sta_if.isconnected():
        try:
            client = mqttclient.Client()
            client.username_pw_set(config_array[2],password=config_array[3])
            client.on_message = on_message
            client.on_connect=on_connect
            client.connect(broker_adress,port=port1)
            client.loop_start()
            time.sleep(1)
        except:
            pass
        if mode == "monitoring":
            pass
        elif mode == "configuration":
            pass
    elif uart.any() > 0:
        strMsg = uart.read()
        f = open("config.txt", "x")
        f.write(strMsg)
        f.close()
        time.sleep(1)
    else:
        pass
        



