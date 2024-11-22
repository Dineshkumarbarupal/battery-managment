import psutil
import time
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if plugged and percent >= 98:  # You can set this to any percentage
        notification.notify(
            title="Battery Full Alert!",
            message=f"Battery is {percent}% charged. Please unplug the charger.",
            timeout=20 # Notification timeout in seconds
        )

if __name__ == "__main__":
    while True:
        check_battery()
        time.sleep(30)  # Check every 60 seconds



