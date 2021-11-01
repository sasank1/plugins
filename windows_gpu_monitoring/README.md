# Plugin to monitor windows GPU Devices

### Prerequisites

- Download and install the latest version of the [Site24x7 Windows agent] (https://www.site24x7.com/app/client#/admin/inventory/monitors-configure/SERVER/windows) in the server where you plan to run the plugin.
- Plugin Uses "GPUtil" python module to get the gpu devices performance metrics, Execute the following command in your Command Prompt to install GPUtil

      pip install gputil

### Plugin installation

---

##### Windows

- Create a directory "windows_gpu_monitoring" under Site24x7 Windows Agent plugin directory :

      Windows     ->   C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins\windows_gpu_monitoring

- Download the file "windows_gpu_monitoring.py" and place it under the "windows_gpu_monitoring" directory.

- Execute the below command to check for the valid json output.

      python windows_gpu_monitoring.py

The agent will automatically execute the plugin within five minutes and send performance data to the Site24x7 data center.

### Metrics Captured

- Memory Utilization
- CPU Utilization
- Temperature
- Individual Core Utilization
- Device Name
