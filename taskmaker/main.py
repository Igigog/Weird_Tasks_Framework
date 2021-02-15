import db
import os
import logging
from datetime import datetime, timezone

date_time = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
anomaly_version = "1.5.1"
op = "{"
cl = "}"
TEXT_HEADER = "igi_task_text_"
STAGES = 2
SPACE_COUNT = 21
FILE_HEADER = f""";============================================================
;
;	Anomaly {anomaly_version}
;	{db.AUTHOR}
;   Last change: {date_time} UTC
;
;============================================================
"""


def spaces(string):
    count = SPACE_COUNT - len(str(string))
    return " "*count if count > 0 else ""


def collect_tasks(tags):
	npc_tasks = set()
	for task_tags, tasks in db.quests.items():
		if tags.issuperset(task_tags):
			npc_tasks.update(tasks)
	return npc_tasks


def write_npc_header(f, npc_id, tags):
	header = f"""
;============================================================
;{" "*(29-len(str(tags))//2)}{tags} 
;{" "*(29-len(npc_id)//2)}{npc_id}
;============================================================
"""
	f.write(header)


def write_task(f, task_name, npc):
	icon = db.icons[task_name]
    task_id = f"{npc}_task_{task_name}"
    task_section = f"""
[{task_id}]
icon {spaces("icon")}= {icon}
storyline {spaces("storyline")}= false
prior {spaces("prior")}= 2000
repeat_timeout {spaces("repeat_timeout")}= 16200
precondition {spaces("precondition")}= {op + f"=validate_generic_task({task_id})" + cl} true, false

title_functor {spaces("title_functor")}= igi_task_generic_text
descr_functor {spaces("descr_functor")}= igi_task_generic_text
job_descr {spaces("job_descr")}= {TEXT_HEADER}{task_id}_job_descr
task_complete_descr {spaces("task_complete_descr")}= {TEXT_HEADER}{task_id}_finish

stage_complete {spaces("stage_complete")}= {STAGES}
status_functor {spaces("status_functor")}= igi_task_generic_status
target_functor {spaces("target_functor")}= igi_task_generic_target
on_job_descr {spaces("on_job_descr")}= %=igi_task_generic_setup({task_id})%

on_complete {spaces("on_complete")}= %=igi_task_generic_finish({task_id}:true)%
on_fail {spaces("on_fail")}= %=igi_task_generic_finish({task_id}:false))%
condlist_0 {spaces("condlist_0")}= {op + f"!task_giver_alive({task_id})" + cl} fail
;------------------------------------------------
""")
	
	f.write(task_section)


def main():
    try:
        os.mkdir("task")
    except FileExistsError:
        pass
    
    for location, npcs in db.locations.items():
        with open(f"task/tm_igi_{db.PREFIX}_tasks_{location}.ltx", 'w') as f:
            f.write(FILE_HEADER)
            for npc, tags in npcs.items():
                tasks = collect_tasks(tags)
                write_npc_header(f, npc, tags)
                for task_name in tasks:
                    write_task(f, task_name, npc)


def write_warfare_faction_header(f, faction):
	header = f"""
;============================================================
;
;{spaces(faction)}{faction} 
;
;============================================================
"""
	f.write(header)


def write_warfare():
	try:
        os.mkdir("task")
    except FileExistsError:
        pass
        
    with open(f"task/tm_igi_{db.PREFIX}_tasks_warfare.ltx", "w") as f:
		f.write(FILE_HEADER)    
		for faction, faction_tags in db.warfare_factions.items():
			write_warfare_faction_header(f, faction)
			for npc_type, type_tags in db.warfare_npc_types.items():
				tags = set()
				tags.update(faction_tags)
				tags.update(type_tags)
				tasks = collect_tasks(tags)
				
				for task_name in tasks:
					write_task(f, task_name, f"sim_default_{faction}_{npc_type}")


if __name__ == '__main__':
    try:
        main()
        write_warfare()
        input("Ltx creating complete! Press Enter to exit...")
    except Exception as e:
        console = logging.StreamHandler()
        logging.getLogger().addHandler(console)
        logging.exception(e)
        input("Press Enter to exit...")
    
