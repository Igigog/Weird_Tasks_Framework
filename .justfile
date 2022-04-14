set shell := ["powershell.exe", "-c"]

run:
    ..\..\ModOrganizer.exe "moshortcut://:Anomaly (DX11-AVX)"

modorg:
    ..\..\ModOrganizer.exe

lua:
    lua5.1 run.lua

luai:
    lua5.1 -i for_tests/lua_interactive.lua
