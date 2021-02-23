import RPi.GPIO as GPIO                             # Import Raspberry Pi GPIO library
import time                                         # Import the sleep function from the time module

GPIO.setwarnings(False)                             # Ignore warning for now
GPIO.setmode(GPIO.BCM)                              # Use physical pin numbering
GPIO.setup(18, GPIO.OUT)                            # Set pin 8 to be an output pin and set initial value to low (off)

while True:                                         # Run forever
     GPIO.output(18, True)                          # Turn on
     time.sleep(2)                                  # Sleep for 1 second
     GPIO.output(18, False)                         # Turn off
     time.sleep(2) 