from hm import HM
# Import OpenHardwareMonitor using pythonnet (clr)
import clr
clr.AddReference('LibreHardwareMonitorLib')
import LibreHardwareMonitor as lhm


class LHM(HM):
    def __init__(self, CPU=True, GPU=True, Motherboard=False, RAM=False, HDD=False, PSU=False, Network=False) -> None:
        self.computer = lhm.Hardware.Computer()
        self.computer.IsCpuEnabled = CPU
        self.computer.IsGpuEnabled = GPU
        self.computer.IsMemoryEnabled = RAM
        self.computer.IsMotherboardEnabled = Motherboard
        self.computer.IsNetworkEnabled = Network
        self.computer.IsPsuEnabled = PSU
        self.computer.IsStorageEnabled = HDD
        self.computer.Open()
