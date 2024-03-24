import argparse
import json
import time
import lhm
# import ohm

parser = argparse.ArgumentParser()
parser.add_argument('--sensors', type=str, nargs='*',
                    help='List of sensors to monitor')
parser.add_argument('--refresh-rate', type=float, default=1.0,
                    help='Refresh rate in seconds')
parser.add_argument('--list-sensors', action='store_true',
                    help='List all available sensors')
args = parser.parse_args()

hm = lhm.LHM()

print(args)

if args.list_sensors:
    print(json.dumps(hm.get_all(), indent=2))
    exit(0)

while True:
    for sensor in args.sensors:
        print(f'{sensor:32}: {hm.get_sensor(sensor, hm.get_all())}')
    time.sleep(args.refresh_rate)
