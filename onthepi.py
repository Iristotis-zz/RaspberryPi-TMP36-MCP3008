# RaspberryPi TMP36 ADC Reading for SciOly
# AUTHOR: Aaron "Iristotis" Bennett @ TheFSI
# LICENSE: GNU General Public License 3.0

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

# SOFTWARE SPI
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# HARDWARE SPI
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# OPENING TEXT FILES FOR LOG & TEMPERATURE
f = open("log.txt","w+")
f2 = open("templog.txt","w+")
f.write("Opened Files...")
f2.close()
# CREATING THE VARIABLE FOR READING TMP36 ON CHANNEL 8
adcreading = mcp.read_adc(8)
f.write("ADC Is on Channel 8")

# CALIBRATE THE TEMPERATURE
cal = 0

# READING THE ADC & WRITING TEMPERATURES IN LOOP
while True:
# READING ADC READING & CONVERTING TO MILLIVOLTS
    millivolts = adcreading * ( 3300.0 / 1023.0 )
    temp_C = ((millivolts - 100.0) / 10.0) - 40.0 + cal
    temp_F = ( temp_C * 9.0 / 5.0 ) + 32 )
    temp_K = ( temp_C + 273.15 )
    f.write("Read Temperatures...")
    print(" temp_C " + " temp_F " + " temp K ")
    time.sleep(0.5)
# WRITING TEMPERATURE C TO FILE THAT WILL BE READ BY macOS
    f2 = open("templog.txt","w+")
    f2.write(temp_C)
    f2.close()
    f.write("Wrote Temperature C to File...")
    time.sleep(0.5)
