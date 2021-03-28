Requirements:
A db.py file must be present in the root folder (same as this file)
Don't forget to add AUTHOR and PREFIX on top of db file

You'll need icon for every task written in icons table. Example:
icons = {
	"gt_transaction": "ui_inGame2_Sdelka",
    "gt_supply": "ui_inGame2_Osobiy_zakaz",
}

This tool supports two quest construction modes (hybrid mode supported):

1) Tag to Tasks:
	Uses set (frozenset) of npc tags as key and list of tasks as value.
	If npc has ALL of key tags, then ALL tasks from value list 
	will be assigned to him.

::Example Tag to Tasks::
quests = {
    fs(["Barkeep"]): [
        "task1",
        "task2",
    ],
    fs(["Mechanic", "Warfare"]): [
        "task1"
    ],
}
In this example Barkeep is assigned task1 and task2, and all warfare mechanics are assigned task1


2) Task to NPCs:
	Uses task name as key and list of npc tag sets as value
	Task is assigned to npc if has all tags of 
	at least one of value sets.

::Example Task to NPCs::
quests = {
    "task1": [
    {"Mechanic", "Duty"},
    {"Leader", "ClearSky", "Ecolog"},
    {"Bandit", "Freedom"},
    ],
    "task2": [
    {"Leader", "Mechanic", "Monolith"},
    {"Medic"},
    ],
}

In this example task1 will be assigned to the mechanic(s) of Duty, the leader(s) of ClearSky and Ecolog, and Bandits and Freedom.
task2 will be assigned to the leader(s) and mechanic(s) of Monolith, along with all medics in the game.

::Example Hybrid Mode::
quests = {
    "arszi_scout": [
        {"Leader", "Agroprom", "Army"},
        {"Trader", "Bar", "Duty"},
    ],
    fs(["Butcher"]): [
        "arszi_fetch_trophy",
        "arszi_fetch_hide",
    ],
}
