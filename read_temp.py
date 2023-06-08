import serial
from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler

ser = serial.Serial('COM3', baudrate=115200,timeout=100)  # Replace '/dev/ttyUSB0' with the appropriate port

logging.basicConfig(format='%(asctime)s, %(message)s',datefmt='%y/%m/%d %H:%M', level=logging.INFO)



root = logging.getLogger()
temp_log = TimedRotatingFileHandler('./temp_log.log', when='D', interval=7,
                                                     backupCount=4)  # log errors in a weekly file, save monthly backup

formatter = logging.Formatter('%(asctime)s, %(message)s',
                              datefmt='%y/%m/%d %H:%M')
temp_log.setFormatter(formatter)

root.setLevel(logging.INFO)
root.addHandler(temp_log)




while (1):
    temp1_s = ser.readline().decode().strip()
    #print(temp1_s)
    if "Temperature:" in temp1_s:
        temp1 = temp1_s.split(':')[1]
    #print(temp1)

    temp2_s = ser.readline().decode().strip()
    if "Temperature2:" in temp2_s:
        temp2 = temp2_s.split(":")[1]
    #print(temp2)

    hum_s = ser.readline().decode().strip()
    if "Humidity:" in hum_s:
        hum = hum_s.split(":")[1]
    #print(hum)
    root.info("{0}, {1}, {2}".format(temp1,temp2,hum))
    
    sleep(5)
