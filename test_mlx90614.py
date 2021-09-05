import Adafruit_GPIO.I2C as I2C
import time

I2C.require_repeated_start()
sleep_time = 1

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
    print("Temp. Objecto: {}C , Temp. Ambiente: {}C".format(round(t, 3), round(a, 3)))
#FINAL DE LA FUNCION DE MEDIR TEMPERATURA        

if __name__ == '__main__':
    print ( "Inicio de Prueba del Chip MLX90614" )
    print ( "Presione Ctrl-C para salir" )
    while True:
        read_temp_sensor()
        print ( "En espera por ", sleep_time, " segundos")
        print ( "*" * 40)
        time.sleep(sleep_time)
    except KeyboardInterrupt:
        print ( "Prueba Terminada" )

# FIN DE LA FUNCION DEL SENSOR APDS9960