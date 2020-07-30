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

## How it works:
1. First of all, the function parses quest constructor from igi_quests and
creates CACHE with all needed data for next steps
2. With data from setup all the objects are created and saved in CACHE
3. The whole task is divided by instant and continuous subtasks
4. Task is done when all instant tasks are done and all continuous are ready to finish

## Preconditions
TODO

## Setup
gt_setup.setup_quest() is a function used to rework user-defined setup to machine-friendly (but also human-friendly, I love debugging too).
It's main purpose is to trigger all random choices and define clear (almost) non-random items to be used by another functions.
All quest-specific choices are triggered at this moment, so all items don't posess quest-related relations.
Values not used by setup_quest are transfered untouched.

### Smarts
Smarts posess three optional arguments: amount, is_nearby, is_online.
- `is_nearby`: use levels that are adjanced to current player level
- `is_online`: use smarts from player level

### Squads
Squads as well as items might have online activities; These are documented below
Squads might be stalkers or mutants of pre-defined types. For types see gt_database.
Stalker squads might have any faction in game or these faction types:
- Enemy: enemy for both quest giver and player
- Client: Enemy for enemy
- Quest_giver
- Player
Squad can define subtask

### Packages
Packages are lootboxes with predefined loot type. 
Package type must be defined in gt_database.PACKAGE, for random choice use QUEST_TO_POSSIBLE_GOODS.
Package can define subtask.

### Items
Items can be created or found in world or in npc inventory.
Use list of endings if item can be inside container of some sort (like artifact containers)
Item can define subtask

## Create target
gt_helper.create_target() uses CACHE created in setup_quest to create/find item from a given template. It makes completely non-random
game objects and saves their data in a groups with length defined by `amount`. 
TODO

## Subtasks
TODO

## Win condition
TODO

## CACHE structure TODO
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