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
            print(f"total power consumed: {y/1000}kW")
        else:
            print(f"total power consumed: {y}W")
        print(f"average power consumption: {(y/(i+1))} W\n")
        time.sleep(3)
except KeyboardInterrupt:
    print("Interrupted by user")
    open("log.txt", "a").write(f"[{timestamp}] - average power consumption: {(y/(i+1))} W\n")
x.close()