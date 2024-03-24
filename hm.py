class HM:
    def __init__(self) -> None:
        self.computer = None
        raise NotImplementedError("This class is not meant to be instantiated")
    
    def update(self):
        for hardware in self.computer.Hardware:
            hardware.Update()
    
    def get_all(self):
        self.update()
        info = {}
        for hardware in self.computer.Hardware:
            info[str(hardware)] = {}
            for sensor in hardware.Sensors:
                info[str(hardware)][str(sensor.Identifier)] = sensor.get_Value()

        return info

    def get_all_temp(self):
        self.update()
        info = {}
        for hardware in self.computer.Hardware:
            info[str(hardware)] = {}
            for sensor in hardware.Sensors:
                if 'temperature' in str(sensor.Identifier):
                    info[str(hardware)][str(sensor.Identifier)] = sensor.get_Value()

        return info
