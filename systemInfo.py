import platform

details = {}

details["Platform Details"] = platform.platform()

details['System Name'] = platform.system()

details["Processer name"] = platform.processor()

details['Architecture Details'] = platform.architecture()

for k,v in details.items():
    print(k,"-",v)