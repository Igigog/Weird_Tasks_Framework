import db
import os

op = "{"
cl = "}"
TEXT_HEADER = "igi_task_text_"
STAGES = 2
SPACE_COUNT = 21
FILE_HEADER = """;============================================================
;	Anomaly 1.5.5.0
;	Igigog
;============================================================
"""


def main():
    try:
        os.mkdir("task")
    except FileExistsError:
        pass
    
    for location, npcs in db.locations.items():
        with open(f"task/tm_igi_tasks_{location}.ltx", 'w') as f:
            f.write(FILE_HEADER)
            for npc, typ in npcs.items():
                try:
                    tasks = db.quests[typ]
                except KeyError:
                    continue
                f.write(f"""
;============================================================
;{" "*(29-len(typ)//2)}{typ} 
;{" "*(29-len(npc)//2)}{npc}
;============================================================""")
                for task_name in tasks:
                    icon = db.icons[task_name]
                    task_id = f"{npc}_task_{task_name}"
                    f.write(f"""
[{task_id}]
icon {" "*(SPACE_COUNT-len("icon"))}= {icon}
storyline {" "*(SPACE_COUNT-len("storyline"))}= false
prior {" "*(SPACE_COUNT-len("prior"))}= 2000
repeat_timeout {" "*(SPACE_COUNT-len("repeat_timeout"))}= 16200
precondition {" "*(SPACE_COUNT-len("precondition"))}= {op + f"=validate_generic_task({task_id})" + cl} true, false

title_functor {" "*(SPACE_COUNT-len("title_functor"))}= igi_task_generic_text
descr_functor {" "*(SPACE_COUNT-len("descr_functor"))}= igi_task_generic_text
job_descr {" "*(SPACE_COUNT-len("job_descr"))}= {TEXT_HEADER}{task_id}_job_descr
task_complete_descr {" "*(SPACE_COUNT-len("task_complete_descr"))}= {TEXT_HEADER}{task_id}_finish

stage_complete {" "*(SPACE_COUNT-len("stage_complete"))}= {STAGES}
status_functor {" "*(SPACE_COUNT-len("status_functor"))}= igi_task_generic_status
target_functor {" "*(SPACE_COUNT-len("target_functor"))}= igi_task_generic_target
on_job_descr {" "*(SPACE_COUNT-len("on_job_descr"))}= %=igi_task_generic_setup({task_id})%

on_complete {" "*(SPACE_COUNT-len("on_complete"))}= %=igi_task_generic_finish({task_id}:true)%
on_fail {" "*(SPACE_COUNT-len("on_fail"))}= %=igi_task_generic_finish({task_id}:false))%
condlist_0 {" "*(SPACE_COUNT-len("condlist_0"))}= {op + f"!task_giver_alive({task_id})" + cl} fail
;------------------------------------------------
""")


if __name__ == '__main__':
    main()
