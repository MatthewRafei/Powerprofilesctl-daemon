import os
import time

def check_ac_state():
   ac_value = 0
   current_ac_value = open('/sys/class/power_supply/AC/online', 'r')
   ac_value = int(current_ac_value.read())
   return ac_value


def get_battery_percentage():
    current_battery_percentage = 0
    get_battery_percentage = open('/sys/class/power_supply/BAT0/capacity', 'r')
    current_battery_percentage = int(get_battery_percentage.read())
    return current_battery_percentage



def main():
    while True:
        if check_ac_state() == 1:
            os.system('powerprofilesctl set performance')
        elif check_ac_state() == 0:
            if get_battery_percentage() > 20:
                os.system('powerprofilesctl set balanced')
            elif get_battery_percentage() <= 20:
                os.system('powerprofilesctl set power-saver')
        time.sleep(1)


if __name__ == '__main__':
    main()





