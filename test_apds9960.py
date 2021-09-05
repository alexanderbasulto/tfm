import Adafruit_GPIO.I2C as I2C
import board
import time
from adafruit_apds9960.apds9960 import APDS9960
import busio
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

I2C.require_repeated_start()

sleep_time = 1
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
sensor.enable_color = True


# INICIO DE LA FUNCION DEL SENSOR APDS9960
if __name__ == '__main__':
    print ( "Inicio de Prueba el Chip APDS9960" )
    print ( "Presione Ctrl-C para salir" )
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    v_cerca = sensor.proximity
    print("Valor de Proximidad: ", v_cerca)
    try:
        while True:
            gesture = apds.gesture()

            if gesture == 0x01:
                print("arriba")
            elif gesture == 0x02:
                print("abajo")
            elif gesture == 0x03:
                print("izquierda")
            elif gesture == 0x04:
                print("derecha")

    except KeyboardInterrupt:
        print ( "Prueba Terminada" )

# FIN DE LA FUNCION DEL SENSOR APDS9960