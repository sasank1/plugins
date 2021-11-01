#!/usr/bin/python

import platform
import json

PLUGIN_VERSION = "1"
HEARTBEAT_REQUIRED = "true"

result_json = {}
metric_units = {}


def metric_collector():
    try:
        if(platform.system() == "Windows"):
            import GPUtil
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                result_json[gpu.name + "_memory_utilzation"] = round((gpu.memoryUtil)*100, 2)
                result_json[gpu.name + "_used_memory"] = gpu.memoryUsed
                result_json[gpu.name + "_total_memory"] = gpu.memoryTotal
                result_json[gpu.name + "_temperature"] = gpu.temperature

                metric_units[gpu.name + "_memory_utilzation"] = "%"
                metric_units[gpu.name + "_used_memory"] = "MB"
                metric_units[gpu.name + "_total_memory"] = "MB"
                metric_units[gpu.name + "_temperature"] = "Celsius"

        elif(platform.system() == "Linux"):
            import gpustat
            import subprocess
            output = gpustat.new_query()
            for each_line in output:
                result_json["memory"] = str(int(each_line.memory_used))
                result_json["utilization"] = str(int(each_line.utilization))
                result_json["temperature"] = str(int(each_line.temperature))
                result_json["device_name"] = each_line.name.split(" ")
                cmd = 'gpustat -cp'
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                p_status = p.wait()
                core_output = output.split('\n')
                for each in core_output:
                    if each.startswith('['):
                        core_out_line = each.split()    
                        core_out="core_"+core_out_line[0].replace('[', '').replace(']', '')
                        result_json[core_out] = core_out_line[5]


        result_json["plugin_version"] = PLUGIN_VERSION
        result_json["units"]=metric_units

    except Exception as e:
        result_json["msg"]=str(e)
        result_json["status"]=0

    result_json["heartbeat_required"] = HEARTBEAT_REQUIRED



if __name__ == '__main__':
    metric_collector()
    print(json.dumps(result_json, indent=4, sort_keys=True))
