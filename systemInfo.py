import platform

print(f"""
Architecture Details - {platform.architecture()}
System OS - {platform.uname()[0]}
Node - {platform.uname()[1]}
Release - {platform.uname()[2]}
Version - {platform.uname()[3]}
Machine - {platform.uname()[4]}
Processer - {platform.uname()[5]}

""")
"""
"Platform Details" = platform.platform()
'System OS' = platform.system()
"Processer name" = platform.processor()
"System release version" = platform.version()
'machine' = platform.machine()
'node' = platform.node()
"""
