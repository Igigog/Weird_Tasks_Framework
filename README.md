# Weird Tasks Framework
# OUTDATED
### Special thanks to GhenTuong

This is my addon for S.T.A.L.K.E.R. Anomaly based on GhenTuong Tasks. 
The main idea is making global handler for all types of quests... Well, you can call it *quest intepreter*.
Although it's possibilities are strictly limited, I will try to do it as suitable to random-generated tasks as possible.

## To create a task:
1. First of all, you need to construct a task
In /scripts/igi_tasks.script add a task setup as variable ```*quest_name* = { *quest setup* }```
2. Set up preconditions and task icon in /configs/igi_tasks/task_info.ltx
2. Add your quest to any location in /configs/misc/task
3. Add your quest description to /configs/text

## Starting out
If you want to create a task and NOT script anything, then you must accustom to just a few files:
- igi_tasks.script
- task_info.ltx
- /configs/misc/task folder
- /configs/text/ folder
Which are essential for creating a task using this addon. Another script files are made for modder use only and mainly won't affect your line of work

## Modules
1. [Activities](#activities)
2. [Database](#database)
3. [Description](#description)
4. [Generic Task](#generic-task)
5. [Helper](#helper)
6. [Linker](#linker)
7. [Precondition](#precondition)
8. [Setup](#setup)
9. [Subtask](#subtask)
10. [Target](#target)
11. [Tasks](#tasks)
12. [Utils](#utils)

## Activities
/scripts/igi_activities.script defines the pool of activities that can be made with whatever entity you want as well as conditions for them to happen.
Activities are triggered just once, continuous activities are not implemented.
#### Implemented conditions:
- ```is_online``` - whenever entity is online. It don't use callbacks and just checks if object is online every few seconds.
- ```if_low_condition``` - whenever entity is under 90% condition.

#### Implemented activities:
- ```change_faction``` - change squad faction to any faction or to a role defined in setup (faction or role in arg)
- ```repair```(true in arg) - set entity condition to random value 90%-100%

## Database
/scripts/igi_db.script uses .ltx files from /config/igi_tasks.
Here I've defined TableView class which works almost as lua table (Not fully due to Lua 5.1 limitations) but takes values from .ltx instead of RAM
For loops TableView must be represented as actual lua table with :as_table() method. For multiple loops it's preferred to cache as_table's data in a variable.

## Description
/scripts/igi_description.script module structurizes description data prepared in setup to... make a description. Nothing interesting here.

## Generic Task
/scripts/igi_generic_task.script is the heart of every task created in this addon.
This script implements all the functors used in engine to run a task.
TODO

## Helper
/scripts/igi_helper.script is just a dump of functions which belongs to no other module

## Linker
/scripts/igi_linker.script is used for all entity dependencies and entity id work.
This file serves to two main reasons:
1. Check if all the dependencies in task can be resolved
2. Actually resolve them (using entity id's created in linker)

## Precondition
/scripts/igi_precondition.script is used to check preconditions from /config/igi_tasks/task_info.ltx

## Setup
/scripts/igi_setup.script serves two main purposes:
1. Checks if task can be prepared (mainly find items used in task in world)
2. Prepare all important entity data before actual entity creation. For example: here are all the factions used in task created

## Subtask
/scripts/igi_subtask.script is the main gameplay module.
There are two types of subtasks:
1. Instant tasks. These can be completed fully inside task timeframe (example: kill anyone)
2. Continuous tasks. These can only be prepared to complete and will end with task finish (example: deliver an item)


Task goes to stage 1 when all the instant tasks are completed.
Task goes to stage 2 when all the continuous tasks are ready to finish.
Continuous tasks are the only ones that can be failed.

#### Implemented subtasks:
- ```kill```
- ```return``` - deliver entity to task giver
- ```get``` - take item to your inventory

## Target
/scripts/igi_target.script is creating actual objects for the task.
Order of creation is defined by linker.

## Tasks
/scripts/igi_tasks.script is where the task constructor is stored. This is the main file that defines task gameplay.

## Utils
/scripts/igi_utils.script is a dump of functions used mainly for lua and not for any STALKER things.