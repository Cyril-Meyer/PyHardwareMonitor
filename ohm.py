from hm import HM
# Import OpenHardwareMonitor using pythonnet (clr)
import clr
clr.AddReference('OpenHardwareMonitorLib')
import OpenHardwareMonitor as ohm


class OHM(HM):
    def __init__(self, CPU=True, GPU=True, Motherboard=False, RAM=False, HDD=False, FanController=False) -> None:
        self.computer = ohm.Hardware.Computer()
        self.computer.MainboardEnabled = Motherboard
        self.computer.CPUEnabled = CPU
        self.computer.RAMEnabled = RAM
        self.computer.GPUEnabled = GPU
        self.computer.HDDEnabled = HDD
        self.computer.FanControllerEnabled  = FanController
        self.computer.Open()
