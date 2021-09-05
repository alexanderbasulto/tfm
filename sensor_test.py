import Adafruit_GPIO.I2C as I2C
import board
import time
from adafruit_apds9960.apds9960 import APDS9960
import busio
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

I2C.require_repeated_start()
#i2c = board.I2C()
sleep_time = 1
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
sensor.enable_color = True


#SE DEFINE LA FUNCION DEL SENSOR DE TEMPERATURA MLX90614
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
        print("raw temp {}".format(temp))
        temp = temp * .02 - 273.15
        return temp

def read_temp_sensor():
    sensor = Melexis()
    t = sensor.readObject1()
    a = sensor.readAmbient()
    print("Temp. Objecto: {}C , Temp. Ambiante: {}C".format(round(t, 3), round(a, 3)))
#FINAL DE LA FUNCION DE MEDIR TEMPERATURA        


# INICIO DE LA FUNCION DEL SENSOR APDS9960
r, g, b, c = sensor.color_data
print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

def gesture_read():
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")


if __name__ == '__main__':
    print ( "Inicio de Prueba de Sensores" )
    print ( "Presione Ctrl-C para salir" )
    try:
        while True:
            print ( "Leyendo Sensores" )
            print ( "Valores del Chip APDS9960" )
            v_cerca = sensor.proximity
            print("Valor de Proximidad: ", v_cerca)
            gesture_read()
            print ( "*" * 40)
            print ( "Medicion de Temperatura con el Chip MLX90614")
            read_temp_sensor()
            print ( "En espera por ", sleep_time, " segundos")
            print ( "*" * 40)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print ( "Prueba Terminada" )

# FIN DE LA FUNCION DEL SENSOR APDS9960