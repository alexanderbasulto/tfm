# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
import random
import time
import Adafruit_GPIO.I2C as I2C
from azure.iot.device import IoTHubDeviceClient, Message
# Using the Python Device SDK for IoT Hub:
# https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
I2C.require_repeated_start()

#DEFINICION DE VARIABLE SGLOBALES
tc = 36.5
ta= 24.0
sleep_time = 10
aburrido = False
dormido = False
conn_str = "HostName=IothubTFM.azure-devices.net;DeviceId=gateway;SharedAccessKey=GdfSD3J6RF0Eou14oJwTkV+a86AXlrD0QEae3HxAguc="
device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

# Define the JSON message to send to IoT Hub.
MSG_TXT = '{{"ta": {ta},"tc": {tc},"aburrido": {aburrido},"dormido": {dormido}}}'
#********************************************

class Melexis:

    def __init__(self, address=0x5A):
        self._i2c = I2C.Device(address,busnum=1)

    def readAmbient(self):
        return self._readTemp(0x06)

    def readObject1(self):
        return self._readTemp(0x07)

    def readObject2(self):
        return self._readTemp(0x08)

    def _readTemp(self, reg):
        temp = self._i2c.readS16(reg)
        #print("raw temp {}".format(temp))
        temp = temp * .02 - 273.15
        return temp

def read_data_sensor():
    irsensor = Melexis()
    global tc
    global ta
    tc = irsensor.readObject1()
    ta = irsensor.readAmbient()
    print("T. Corporal: {}C , T. Ambiente: {}C".format(round(tc, 3), round(ta, 3)))
    return(tc,ta)

def iothub_send_data():
    msg_txt_formatted = MSG_TXT.format(ta=ta, tc=tc, aburrido=aburrido, dormido=dormido)
    message = Message(msg_txt_formatted)
    # Add a custom application property to the message.
    # An IoT hub can filter on these properties without access to the message body.
    #if tc > 37:
    # message.custom_properties["tempAlert"] = "true"
    #else:
    # message.custom_properties["tempAlert"] = "false"
    # Send the message.
    print( "Enviando Mensaje a Iot-Hub: {}".format(message) )
    device_client.send_message(message)
    print ( "Mensaje enviado con exito" )
    device_client.disconnect()
    return
    
if __name__ == '__main__':
    print ( "Inicio de Aplicacion" )
    print ( "Presione Ctrl-C para salir" )
    try:
        while True:
            print ( "Leyendo Sensores" )
            read_data_sensor()
            iothub_send_data()
            print ( "Sleep por", sleep_time, "segundos")
            print ( "*" * 40)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print ( "IoTHubClient stopped" )
        