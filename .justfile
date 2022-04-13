set shell := ["powershell.exe", "-c"]

run:
    - Remove-Item "D:\Games\Anomaly\MO2\mods\Weird_Tasks_Framework" -Recurse
    Copy-Item "D:\Tasks\Weird_Tasks_Framework" -Destination "D:\Games\Anomaly\MO2\mods\Weird_Tasks_Framework"
    Invoke-Item -Path "D:\Desktop\MO2Anomaly.lnk"

lua:
    lua5.1 run.lua

luai:
    lua5.1 -i for_tests/lua_interactive.lua
