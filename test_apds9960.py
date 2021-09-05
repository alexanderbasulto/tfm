import board
import busio
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

I2C.require_repeated_start()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
sensor.enable_color = True

try:
    print ( "Inicio de Prueba el Chip APDS9960" )
    print ( "Presione Ctrl-C para salir" )
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    v_cerca = sensor.proximity
    print("Valor de Proximidad: ", v_cerca)
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
