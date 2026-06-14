#SOUND CHECKKK

import winsound
import time

last_alert_time = 0

def smart_alert(risk):

    global last_alert_time

    cooldown = 3

    if time.time() - last_alert_time < cooldown:
        return

    if risk == "high":
        winsound.Beep(1000, 400)
        print("🚨 High distraction risk")

        last_alert_time = time.time()

    elif risk == "medium":
        print("⚠️ Medium distraction risk")