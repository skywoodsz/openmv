# Untitled - By: skywoodsz - 周五 10月 19 2018
import time
from pyb import LED
red_led=LED(1)
while(True):
    red_led.on()
    time.sleep(500)
    red_led.off()
    time.sleep(500)
