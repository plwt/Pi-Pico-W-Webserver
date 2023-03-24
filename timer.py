import machine
from machine import Timer  
import time  

timeInit = time.time()  

def printTime(self):  
    timeDiff = time.time()-timeInit  
    (minutes, seconds) = divmod(timeDiff, 60)  
    (hours, minutes) = divmod(minutes, 60)  
    (days,hours) = divmod(hours, 24)
    #what to do comes next, I serial printed it for now  
    ti = print(str(days)+":"+f"{hours:02d}"+":"+f"{minutes:02d}"+":"+f"{seconds:02d}")  

timer=Timer(-1)  
delay = 10 #in seconds  
timer.init(period=delay*1000, mode=Timer.PERIODIC, callback=printTime)  
#default is a dummy placeholder,
#the timer callback sends a 'self' value which caused an error during testing  
printTime('default')  