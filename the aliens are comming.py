from phue import Bridge
import random
import time

bridge_ip = "your bridge ip goes here"


b = Bridge(bridge_ip)

b.connect()

lamp_1 = "name of your lamp"
lamp_2 = "name of your other lamp"

b.get_light(lamp_1, "on")
b.get_light(lamp_2, "on")

while True:
    sleep_time_livingroom = random.randint(1, 3)
    brightness_livingroom = random.randint(1, 254)
    sleep_time_kitchen = random.randint(1, 3)
    brightness_kitchen = random.randint(1, 254)
    b.set_light(lamp_1, "on", True)
    b.set_light(lamp_1, "bri", brightness_livingroom)
    time.sleep(sleep_time_livingroom)
    b.set_light(lamp_1, "on", False)

    b.set_light(lamp_2, "on", True)
    b.set_light(lamp_2, "bri", brightness_kitchen)
    time.sleep(sleep_time_kitchen)
    b.set_light(lamp_2, "on", False)
