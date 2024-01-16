import time
import datetime
x = open("/sys/class/power_supply/BAT0/power_now", "r")
y = 0
timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
try:
    for i in range(1000):
        x.seek(0)
        power = int(x.read())/1000000
        y += power
        print(f"[{timestamp}] - power consume: {power}W")
        if y > 1000:
            print(f"total power consumed: {round(y/1000, 2)}kW")
        else:
            print(f"total power consumed: {round(y, 2)}W")
        print(f"average power consumption: {round((y/(i+1)), 2)} W\n")
        time.sleep(3)
except KeyboardInterrupt:
    print("Interrupted by user")
    open("log.txt", "a").write(f"[{timestamp}] - average power consumption: {round((y/(i+1)), 2)} W\n")
x.close()