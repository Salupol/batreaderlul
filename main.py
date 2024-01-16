import time

x = open("/sys/class/power_supply/BAT0/power_now", "r")
y = 0

for i in range(1000):
    x.seek(0)
    power = int(x.read())/1000000
    y += power
    print(f"power consume: {power}W")
    if y > 1000:
        print(f"total power consumed: {y/1000}kW")
    else:
        print(f"total power consumed: {y}W")
    print(f"average power consumption: {(y/(i+1))}W")
    time.sleep(3)
x.close()