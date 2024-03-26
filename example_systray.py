import argparse
import json
import time
import lhm
# import ohm
import pystray

import icons

parser = argparse.ArgumentParser()
parser.add_argument('--sensors', type=str, nargs='*',
                    help='List of sensors to monitor')
parser.add_argument('--refresh-rate', type=float, default=1.0,
                    help='Refresh rate in seconds')
args = parser.parse_args()


hm = lhm.LHM()

def stray_menu():
    menu_list = []
    global hm
    sensors = hm.get_all()

    for sensor in args.sensors:
        sensor_str = sensor
        if 'cpu' in sensor:
            sensor_str = 'CPU'
        elif 'gpu' in sensor:
            sensor_str = 'GPU'

        menu_list.append(pystray.MenuItem(f'{hm.get_sensor(sensor, sensors):.1f}°C {sensor_str}', lambda: None))

    menu_list.append(pystray.MenuItem('Exit', lambda: stray.stop()))

    return menu_list

stray = pystray.Icon('PyHardwareMonitor',
                     icon=icons.create_icon(width=128, height=128, shape='thermometer', color='black'),
                     menu=pystray.Menu(stray_menu)
                     )

stray.run_detached()

while True:
    stray.update_menu()
    time.sleep(args.refresh_rate)
