# Igi Tasks
### Special thanks to GhenTuong

This is my addon for S.T.A.L.K.E.R. Anomaly based on GhenTuong Tasks. 
The main idea is making global handler for all types of quests... Well, you can call it *quest compiler*.
Although it's possibilities are strictly limited, I will try to do it as suitable to random-generated tasks as possible.

## To create a task:
1. First of all, you need to construct a task
In /scripts/igi_quests add a quest setup to CONSTRUCTOR as ['*quest_name*'] = { *quest setup* }
For quest setup info see documentation below.
2. Add your quest to any location in /configs/misc/task
3. Add your quest description to /configs/text

## Quest setup
gt_setup.setup_quest() is a function used to rework user-defined setup to machine-friendly (but also human-friendly, I love debugging too).
It's main purpose is to trigger all random choices and define clear (almost) non-random items to be used by another functions.
All quest-specific choices are triggered at this moment, so all items don't posess quest-related relations.
Values not used by setup_quest are transfered untouched.

## Create target
gt_helper.create_target() uses CACHE created in setup_quest to create/find item from a given template. It makes completely non-random
game objects and saves their data of type { id (int), section_name (string) } in a groups with length defined by `amount`. 

## CACHE structure
```lua
CACHE = {
	"smarts" = {*list of string smart_name*},
	"packages" = {
		{data of package_group},
		{...},
	}
	"squads" = {
		{data of squad_group},
		{...},
	}
	"items" = {
		{data of item_group},
		{...},
	}
	"target" = { // here is data of actual ingame objects
		"packages", "squads", "items" = { list of groups of:
			{ list of obj_data:
				{id (int), section_name (string)},
				{...},
			},
			{...},
		}
	}
	"description" = {
		"factions" = {*list of factions*},
		"targets" = {*list of targets*},
		"smarts" = {*list of smarts*},
	},
	"task_name" = *task name*,
}
```