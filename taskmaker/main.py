import os
import logging
import db
from datetime import datetime, timezone
from textwrap import dedent

ANOMALY_VERSION = "1.5.1"
TEXT_HEADER = "igi_task_text_"
FILE_PATH = "task/tm_igi_"
STAGES = 2
SPACE_COUNT = 21
OP = "{"
CL = "}"


def collect_tasks(npc, quests):
    all_tasks = quests.items()
    npc_tasks = set()
    for k,v in all_tasks:
        if type(v) != type(list()):
            raise SyntaxError(f"Quest value is not list! {type(v)}")

        if type(k) == type(frozenset()):
            if npc.issuperset(k):
                npc_tasks.update(v)
        elif type(k) == type(str()):
            for tags in v:
                if npc.issuperset(tags):
                    npc_tasks.add(k)
        else:
            raise SyntaxError(f"Unhandled quests key type! {type(k)}")
    return npc_tasks


def main():
    try:
        os.mkdir("task")
    except FileExistsError:
        pass
    write = Writer(db.AUTHOR)
    for location, npcs in db.locations.items():
        location_file = False
        for npc in npcs:
            npc_tags = db.npc.get(npc)
            if npc_tags:
                tasks = collect_tasks(npc_tags, db.quests)
                if tasks:
                    if not location_file:
                        write.new_file(db.PREFIX, location)
                        location_file = True
                    write.npc_header(npc, npc_tags)
                    for task_name in tasks:
                        write.task(task_name, npc, db.icons)


def warfare():
    try:
        os.mkdir("task")
    except FileExistsError:
        pass
    
    write = WarfareWriter(db.AUTHOR)
    warfare_file = False
    
    for faction, faction_tags in db.warfare_factions.items():
        faction_header = False
        for npc_type, type_tags in db.warfare_npc_types.items():
            tags = {"Warfare"} | faction_tags | type_tags
            tasks = collect_tasks(tags, db.quests)
            for task_name in tasks:
                if not warfare_file:
                    write.new_file(db.PREFIX)
                    warfare_file = True
                if not faction_header:
                    write.warfare_faction_header(faction)
                    faction_header = True

                write.task(task_name, f"sim_default_{faction}_{npc_type}",db.icons)


class Writer:
    
    def __init__(self, author):
        self.author = author
        self.date_time = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
    
    
    def new_file(self, prefix, location):
        self.file = open(f"{FILE_PATH}{prefix}_tasks_{location}.ltx", 'w')
        self.write_file_header()
        
    
    def write_file_header(self):
        header = f"""\
        ;============================================================
        ; 
        ;    Anomaly {ANOMALY_VERSION} 
        ;    {self.author} 
        ;    Last change: {self.date_time} UTC 
        ;
        ;============================================================
        """
        self.file.write(dedent(header))
        

    def npc_header(self, npc_id, tags):
        header = f"""\
        ;============================================================
        ;{" "*(29-len(str(tags))//2)}{tags} 
        ;{" "*(29-len(npc_id)//2)}{npc_id}
        ;============================================================
        """
        self.file.write(dedent(header))

    
    def task(self, task_name, npc, icons):
        spaces = self.spaces
        icon = icons.get(task_name)
        task_id = f"{npc}_task_{task_name}"
        task_section = f"""
        [{task_id}]
        icon {spaces("icon")}= {icon}
        storyline {spaces("storyline")}= false
        prior {spaces("prior")}= 2000
        repeat_timeout {spaces("repeat_timeout")}= 16200
        precondition {spaces("precondition")}= {OP + f"=validate_generic_task({task_id})" + CL} true, false

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
        condlist_0 {spaces("condlist_0")}= {OP + f"!task_giver_alive({task_id})" + CL} fail

        """

        self.file.write(dedent(task_section))
    
    
    def spaces(self, string):
        count = SPACE_COUNT - len(str(string))
        return " "*count if count > 0 else ""
        
        
        
class WarfareWriter(Writer):

    def __init__(self, author):
        super().__init__(author)
    
    
    def new_file(self, prefix):
        self.file = open(f"{FILE_PATH}{prefix}_tasks_warfare.ltx", 'w')
        self.write_file_header()
    
    def warfare_faction_header(self, faction):
        header = f"""\
        ;============================================================
        ;
        ;{self.spaces("Faction: "+faction.capitalize())}{"Faction: "+faction.capitalize()} 
        ;
        ;============================================================
        """
        self.file.write(dedent(header)) 


if __name__ == '__main__':
    try: 
        main()
        warfare()
        input("Ltx creating complete! Press Enter to exit...")
    except Exception as e:
        console = logging.StreamHandler()
        logging.getLogger().addHandler(console)
        logging.exception(e)
        input("Press Enter to exit...")
