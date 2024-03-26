import argparse
import json
import threading
import time

import pystray

import lhm
# import ohm
import icons

parser = argparse.ArgumentParser()
parser.add_argument('--sensors', type=str, nargs='*',
                    help='List of sensors to monitor')
parser.add_argument('--refresh-rate', type=float, default=1.0,
                    help='Refresh rate in seconds')
parser.add_argument('--show-value', action='store_true',
                    help='Show 1st sensor value on icon')
args = parser.parse_args()

if args.sensors is None or len(args.sensors) == 0:
    raise ValueError('At least one sensor must be specified')

hm = lhm.LHM()

def stray_icon(temp=None, low=30, high=70, text=args.show_value):
    if temp is None:
        return icons.create_icon(width=128, height=128, shape='thermometer', color='black')

    if temp < low:
        color = 'blue'
    elif temp > high:
        color = 'red'
    elif temp > low + (high - low) / 2.0:
        color = 'orange'
    else:
        color = 'green'

    if text:
        return icons.create_icon(width=128, height=128, shape='thermometer', color=color, text=f'{round(temp)}')
    else:
        return icons.create_icon(width=128, height=128, shape='thermometer', color=color)

def stray_menu():
    menu_list = []
    global hm
    sensors = hm.get_all()

    for i, sensor in enumerate(args.sensors):
        sensor_str = sensor
        if 'cpu' in sensor:
            sensor_str = 'CPU'
        elif 'gpu' in sensor:
            sensor_str = 'GPU'

        menu_list.append(pystray.MenuItem(f'{hm.get_sensor(sensor, sensors):.1f}°C {sensor_str}', lambda: None))

        if i == 0:
            stray.icon = stray_icon(hm.get_sensor(sensor, sensors))

    menu_list.append(pystray.MenuItem('Exit', lambda: stray.stop()))

    return menu_list

stray = pystray.Icon('PyHardwareMonitor',
                     icon=stray_icon(),
                     menu=pystray.Menu(stray_menu)
                     )

def update():
    s_sleep = 0.1
    n_sleep = int(args.refresh_rate / s_sleep)

    while True:
        if stray is None:
                break
        else:
            stray.update_menu()
            # stray.icon = icons.create_icon(width=128, height=128, shape='thermometer', color=rgba)

        for i in range(n_sleep):
            time.sleep(s_sleep)
            if stray is None:
                break

update_thread = threading.Thread(target=update)
update_thread.start()

stray.run()
stray = None
