# Plugin for Monitoring GPU Device

### PreRequisites
---
##### Linux
- Plugin Uses "gpustat" python module to get the gpu device performance metrics	for Linux 
	
      Execute the following command in your server to install gpustat - pip install gpustat

- Plugin Uses "gpustat -cp" command to get the individual core utilization
---
##### Windows
- Download and install the latest version of the [Site24x7 Windows agent] (https://www.site24x7.com/app/client#/admin/inventory/monitors-configure/SERVER/windows) in the server where you plan to run the plugin.
- Plugin Uses "GPUtil" python module to get the gpu devices performance metrics, Execute the following command in your Command Prompt to install GPUtil

      pip install gputil

### Plugin installation
---
##### Linux 

- Create a directory "gpu_monitoring" under Site24x7 Linux Agent plugin directory - /opt/site24x7/monagent/plugins/gpu_monitoring
- Download the file "gpu_monitoring.py" and place it under the "gpu_monitoring" directory
  
  wget https://raw.githubusercontent.com/site24x7/plugins/master/gpu_monitoring/gpu_monitoring.py
---
##### Windows

- Create a directory "gpu_monitoring" under Site24x7 Windows Agent plugin directory :

      Windows     ->   C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins\gpu_monitoring

- Download the file "gpu_monitoring.py" and place it under the "gpu_monitoring" directory.
---
- Execute the below command to check for the valid json output.

      python gpu_monitoring.py 
- The agent will automatically execute the plugin within five minutes and send performance data to the Site24x7 data center.

### Metrics Captured

- Memory Utilization
- CPU Utilization
- Temperature
- Individual Core Utilization
- Device Name
