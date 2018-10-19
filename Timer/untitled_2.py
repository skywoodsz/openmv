# Untitled - By: skywoodsz - 周五 10月 19 2018
import time
from pyb import LED
from pyb import Timer
led=LED(1)
led.on()
#绑定事件方式1
def led_on_off():
    global led#向全局寻求led变量
    led.toggle()#反转led

timer=Timer(4)#设置定时器4
timer.init(freq=1)#设置定时器频率：1s执行几次
timer.callback(lambda t:led_on_off())#定时器中断函数/回调函数
while(True):#其后必须有语句体
    time.sleep(1000)

#绑定事件方式2
'''
def led_on_off(timer):#不同！
    global led#向全局寻求led变量
    led.toggle()#反转led

timer=Timer(4)#设置定时器4
timer.init(freq=1)#设置定时器频率：1s执行几次
timer.callback(led_on_off)#定时器中断函数/回调函数。不同！
while(True):#其后必须有语句体
    time.sleep(1000)

'''
