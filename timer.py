import utime

def uptime_in_hours():
    start_time = utime.ticks_ms()
    while True:
        current_time = utime.ticks_ms()
        uptime_ms = current_time - start_time
        uptime_hours = uptime_ms / (1000 * 60 * 60)
        print("Uptime: {:.2f} hours".format(uptime_hours))
        utime.sleep(1)










