set shell := ["powershell.exe", "-c"]

run:
    ..\..\ModOrganizer.exe "moshortcut://:Anomaly (DX11-AVX)"

modorg:
    ..\..\ModOrganizer.exe

lua:
    lua5.1 run.lua

luai:
    lua5.1 -i for_tests/lua_interactive.lua

pack:
    #!/usr/bin/sh
    VERSION=$(grep '^TASKS_VERSION =' gamedata/scripts/igi_generic_task.script | sed 's/TASKS_VERSION = "\(.*\)".*/\1/')
    cd ..
    7z a -tzip "WTF_$VERSION.zip" *ask*/gamedata
    7z d -tzip "WTF_$VERSION.zip" test_task
