# PyHardwareMonitor
Python interface for [OpenHardwareMonitor](https://github.com/openhardwaremonitor/openhardwaremonitor) and [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor).


### Usage
#### Install
The current version is based on :
* [OpenHardwareMonitor v0.9.6](https://openhardwaremonitor.org/files/openhardwaremonitor-v0.9.6.zip) `OpenHardwareMonitorLib.dll`.
* [LibreHardwareMonitor v0.9.3](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.3/LibreHardwareMonitor-net472.zip) `LibreHardwareMonitorLib.dll` with optional `HidSharp.dll`.

This project require [pythonnet](https://github.com/pythonnet/pythonnet) (`pip install pythonnet`).

Check [example_basic.py](example_basic.py) for usage example.


### Examples
#### `example_basic.py`

OpenHardwareMonitor as admin:
```
{
  "OpenHardwareMonitor.Hardware.CPU.AMD17CPU": {
    "/amdcpu/0/temperature/0": 39.25,
    "/amdcpu/0/temperature/4": 41.0
  },
  "OpenHardwareMonitor.Hardware.Nvidia.NvidiaGPU": {
    "/nvidiagpu/0/temperature/0": 24.0
  }
}
```
LibreHardwareMonitor as admin:
```
{
  "LibreHardwareMonitor.Hardware.Cpu.Amd17Cpu": {
    "/amdcpu/0/temperature/2": 39.75000762939453,
    "/amdcpu/0/temperature/4": 35.75,
    "/amdcpu/0/temperature/3": 33.05620193481445
  },
  "LibreHardwareMonitor.Hardware.Gpu.NvidiaGpu": {
    "/gpu-nvidia/0/temperature/0": 24.0,
    "/gpu-nvidia/0/temperature/2": 35.375,
    "/gpu-nvidia/0/temperature/3": 34.125
  }
}
```

OpenHardwareMonitor as user:
```
{
  "OpenHardwareMonitor.Hardware.CPU.AMD17CPU": {},
  "OpenHardwareMonitor.Hardware.Nvidia.NvidiaGPU": {
    "/nvidiagpu/0/temperature/0": 24.0
  }
}
```
LibreHardwareMonitor as user:
```
{
  "LibreHardwareMonitor.Hardware.Cpu.Amd17Cpu": {
    "/amdcpu/0/temperature/2": 0.0
  },
  "LibreHardwareMonitor.Hardware.Gpu.NvidiaGpu": {
    "/gpu-nvidia/0/temperature/0": 24.0,
    "/gpu-nvidia/0/temperature/2": 35.34375,
    "/gpu-nvidia/0/temperature/3": 34.5625
  }
}
```


#### Acknowledgement
This work is inspired by [1](https://stackoverflow.com/a/62936850), [2](https://stackoverflow.com/a/49909330).
