import pyupm_grovemoisture as upmMoisture
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import mraa
import time
import sys
import math

#Initialize ports
# Create the temperature sensor object using AIO pin A0
#temp = mraa.Aio(0)
temp = grove.GroveTemp(0)

# Instantiate a Grove Moisture sensor on GPOI pin 7
myMoisture = mraa.Gpio(7)
myMoisture.dir(mraa.DIR_IN)

# Create the relay switch object using GPIO pin 6
relay = grove.GroveRelay(6)

# Create the button object using GPIO pin 5
button = grove.GroveButton(5)

#Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# white
myLcd.setColor(255, 255, 255)
myLcd.clear()
myLcd.setCursor(0,3)
myLcd.write("Smart Pot")
myLcd.setCursor(1,1)
myLcd.write("Instrumentacion")

time.sleep(3)

# Green
myLcd.setColor(255, 255, 102)
myLcd.clear()
myLcd.setCursor(0,3)
myLcd.write("Jhon Toro")
myLcd.setCursor(1,0)
myLcd.write("Osvaldo Renteria")
time.sleep(3)

while 1:
        T = temp.value()
        tempval = "Temp:"+ str(T)
        M = myMoisture.read()
        stateButton = button.value()

        if (stateButton==1):
                # Red
                myLcd.setColor(255, 51, 51)
                myLcd.clear()
                myLcd.setCursor(0,1)
                myLcd.write("BOTON ACTIVADO")
                myLcd.setCursor(1,0)
                myLcd.write("Riego  Encendido")
                relay.on()
                time.sleep(6)
        else:
             	relay.off()

        if (M==1):
                moistureval = "Soil:DRY"
                Motor = "Riego Encendido"
                relay.on()
        else:
             	moistureval = "Soil:WET"
                Motor = "Riego Apagado"
                relay.off()
	  
         # blue
        myLcd.setColor(36, 171, 229)
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write(tempval)
	      myLcd.setCursor(0,8)
        myLcd.write(moistureval)
        myLcd.setCursor(1,1)
        myLcd.write(Motor)
        time.sleep(1)
