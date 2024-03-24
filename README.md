# PyHardwareMonitor
Python interface for [OpenHardwareMonitor](https://github.com/openhardwaremonitor/openhardwaremonitor) and [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor).


### Usage
#### Install
The current version is based on :
* OpenHardwareMonitor [v0.9.6](https://openhardwaremonitor.org/files/openhardwaremonitor-v0.9.6.zip) `OpenHardwareMonitorLib.dll`.
* LibreHardwareMonitor [v0.9.3](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.3/LibreHardwareMonitor-net472.zip) `LibreHardwareMonitorLib.dll` with optional `HidSharp.dll`.

This project require [pythonnet](https://github.com/pythonnet/pythonnet) (`pip install pythonnet`).

Check [example_basic.py](example_basic.py) for usage example.


### Examples
#### `example_basic.py`

<details>
<summary>OpenHardwareMonitor as admin</summary>

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

</details>
<details>
<summary>LibreHardwareMonitor as admin</summary>

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

</details>
<details>
<summary>OpenHardwareMonitor as user</summary>

```
{
  "OpenHardwareMonitor.Hardware.CPU.AMD17CPU": {},
  "OpenHardwareMonitor.Hardware.Nvidia.NvidiaGPU": {
    "/nvidiagpu/0/temperature/0": 24.0
  }
}
```

</details>
<details>
<summary>LibreHardwareMonitor as user</summary>

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

</details>


#### `example_monitor.py`
`python example_monitor.py --sensors "/amdcpu/0/temperature/2" "/gpu-nvidia/0/temperature/2" --refresh-rate 2`

<details>
<summary>CPU stress test</summary>

```
/amdcpu/0/temperature/2         : 45.0
/gpu-nvidia/0/temperature/2     : 35.59
/amdcpu/0/temperature/2         : 44.75
/gpu-nvidia/0/temperature/2     : 36.75
/amdcpu/0/temperature/2         : 68.88
/gpu-nvidia/0/temperature/2     : 36.0
/amdcpu/0/temperature/2         : 79.88
/gpu-nvidia/0/temperature/2     : 35.62
/amdcpu/0/temperature/2         : 84.12
/gpu-nvidia/0/temperature/2     : 35.78
/amdcpu/0/temperature/2         : 86.12
/gpu-nvidia/0/temperature/2     : 35.59
/amdcpu/0/temperature/2         : 87.25
/gpu-nvidia/0/temperature/2     : 35.62
/amdcpu/0/temperature/2         : 87.75
/gpu-nvidia/0/temperature/2     : 35.75
/amdcpu/0/temperature/2         : 88.38
/gpu-nvidia/0/temperature/2     : 36.91
/amdcpu/0/temperature/2         : 89.25
/gpu-nvidia/0/temperature/2     : 35.88
/amdcpu/0/temperature/2         : 89.75
/gpu-nvidia/0/temperature/2     : 35.53
/amdcpu/0/temperature/2         : 90.25
/gpu-nvidia/0/temperature/2     : 35.59
/amdcpu/0/temperature/2         : 90.5
/gpu-nvidia/0/temperature/2     : 35.47
/amdcpu/0/temperature/2         : 90.75
/gpu-nvidia/0/temperature/2     : 35.5
/amdcpu/0/temperature/2         : 91.0
/gpu-nvidia/0/temperature/2     : 35.53
/amdcpu/0/temperature/2         : 91.38
/gpu-nvidia/0/temperature/2     : 35.41
/amdcpu/0/temperature/2         : 89.0
/gpu-nvidia/0/temperature/2     : 35.5
/amdcpu/0/temperature/2         : 83.25
/gpu-nvidia/0/temperature/2     : 36.88
/amdcpu/0/temperature/2         : 78.5
/gpu-nvidia/0/temperature/2     : 36.88
/amdcpu/0/temperature/2         : 74.13
/gpu-nvidia/0/temperature/2     : 35.59
```

</details>

#### Acknowledgement
This work is inspired by [1](https://stackoverflow.com/a/62936850), [2](https://stackoverflow.com/a/49909330).
