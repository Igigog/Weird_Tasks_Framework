set shell := ["powershell.exe", "-c"]

run:
    Invoke-Item -Path "D:\Desktop\MO2Anomaly.lnk"

modorg:
    ..\..\ModOrganizer.exe

lua:
    lua5.1 run.lua

luai:
    lua5.1 -i for_tests/lua_interactive.lua
