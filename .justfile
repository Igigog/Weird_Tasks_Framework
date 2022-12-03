set shell := ["powershell.exe", "-c"]

run:
    ..\..\ModOrganizer.exe "moshortcut://:Anomaly (DX11-AVX)"

modorg:
    ..\..\ModOrganizer.exe

pack:
    #!/usr/bin/sh
    VERSION=$(grep '^TASKS_VERSION =' gamedata/scripts/igi_generic_task.script | sed 's/TASKS_VERSION = "\(.*\)".*/\1/')
    cd ..
    7z a -tzip "WTF_$VERSION.zip" *ask*/gamedata
