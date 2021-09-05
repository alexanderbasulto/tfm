import signal
import sys
import board
import busio
import board
import time
import RPi.GPIO as GPIO  #Importamos el paquete RPi.GPIO y en el código nos refiriremos a el como GPIO
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

pin_led = 21  #Variable que contiene el pin(GPIO.BCM) al cual conectamos la señal del LED
GPIO.setmode(GPIO.BCM)   #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
GPIO.setup(pin_led, GPIO.OUT) #Configuramos el GPIO18 como salida

int_pin = 16
GPIO.setup(int_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sensor.enable_proximity = True
sensor.proximity_interrupt_threshold = (0, 175)
sensor.enable_proximity_interrupt = True

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def button_pressed_callback(channel):
    v_gest = sensor.proximity
    print(v_gest)
    if v_gest >= 200:
        GPIO.output( pin_led , GPIO.HIGH )
        print("Objeto muy cerca!")
        time.sleep(0.5)
    else:
        GPIO.output( pin_led , GPIO.LOW )
        time.sleep(0.5)
        

GPIO.add_event_detect(int_pin, GPIO.FALLING, callback=button_pressed_callback, bouncetime=100)
n = 0

if __name__ == '__main__':
    while 1:   #Implementamos un loop infinito
        n = n + 500
        print (n)
        time.sleep(1)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()