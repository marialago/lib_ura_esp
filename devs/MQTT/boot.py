# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# Robot codes 
from L9110URA import L9110URA
robot = L9110URA(13,12,5,23) 
robot.stop()  

ssid = '****'
password = '****'
mqtt_server = '****'
server_port=1883
mqtt_user='mqtt'
mqtt_password='****'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'URA/robo1/acao'
topic_pub = b'URA/robo1/linhaE'

last_message = 0
message_interval = 30
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())




