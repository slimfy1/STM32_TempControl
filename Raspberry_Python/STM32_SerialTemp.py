from gpiozero import CPUTemperature
import io
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.close()
time.sleep(2)
ser.open()
while 1:
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    t = f.readline ()
    cputemp = int(t)
    ser.write(t.encode())
    print(cputemp)
    time.sleep(1)
