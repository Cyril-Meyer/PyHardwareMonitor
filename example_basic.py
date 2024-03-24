import json
import ohm
import lhm

def view_all_temp(hm):
    print(json.dumps(hm.get_all_temp(), indent=2))

hm = ohm.OHM()
view_all_temp(hm)

hm = lhm.LHM()
view_all_temp(hm)
