# Weird Tasks Framework
## Made for WTF v3h1 (aka terribly OUTDATED)
### Special thanks to GhenTuong

This is my addon for S.T.A.L.K.E.R. Anomaly based on GhenTuong Tasks. 
The main idea is making global handler for all types of quests... Well, you can call it *quest intepreter*.
Although it's possibilities are strictly limited, I will try to do it as suitable to random-generated tasks as possible.

## Stable parts
1. [Task setup table](#task-table)
1. [Subtask system](#subtasks)
1. [How task is created](#setup-and-create)
1. [Generic status functor](#task-status)
1. [Subtask statuses](#subtask-statuses)
1. [Reward system](#rewards)

## Task table
Tasks are defined by their setup table, currently defined in json and converted to lua table when needed.
Task setup consists of:
- Entity table
- "disabled" boolean
- optional reward and precondition tables

## Subtasks
Subtask = entity with *target*.

Entity = table representing one unit of interaction with world (i.e. item, squad, location). You always
need to define *entity_type* for every entity. As of WTF v3h1 these types are *location*, *item* and *squad*.

*target* field represents what interaction player needs to do with entity (aka what do I do to complete task). Target may change every aspect of entity lifecycle, from preparing to cleanup after task completion. You may define your own targets in scripts as well as inherit another target's functionality
using PATTERN variable.

## Setup and Create
Setup is a entity lifecycle step used for preparation to creation. It's recommended to resolve your random
here, but mainly this step is used to define locations and sections of entities.

Create is a step where entity is generated and prepared for main task walkthrough. After creation step
subtask is no more initialised and it's *status* becomes "running" unless stated otherwise.

## Task status
Status functor from igi_generic_task.script is running in background every 3 seconds. Main status steps:
1. On first run: Create
1. Update map marks for entities
1. Do online activities
1. Update subtask statuses
1. If failed unoptional subtask: task failed
1. If no more running subtasks: task completed
1. If task completed and no need to return: give reward
1. Update map target for task

## Subtask statuses
Statuses are defined in igi_subtask.script. Every task cycle status functors for *running* and *ready to complete* subtasks are called and statuses may be changed.

## Rewards
Rewards may be static or dynamic. Dynamic rewards are defined by *target*, static are written in "predefined_rewards" entity table. You may also set static reward for the whole task.

On task fail rewards are defined by *failed* subtasks. On success by both *failed* and *completed* subtasks because *failed* must be all optional.

## Dynamic groups
Whenever static number of groups is not enough, you can generate group entities dynamically with generate pattern. It unfolds lists (comma-separated strings) into separate entity per list value.

For example, we want to dynamically create location entities by random path from some table. Group entity:
```lua
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&"
}
```
Obviously, it won't work since *where* field is not defined and *where* field can only direct to one location. We can generate locations like this:
```lua
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&",
    ["generate:where"] = "$this.path$"
}
```
Let our path be `"aaa,bbb,ccc"`. Then this construct will unfold into:
```lua
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&",
    where_gen_id = 1,
    where = "aaa"
}
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&",
    where_gen_id = 2,
    where = "bbb"
}
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&",
    where_gen_id = 3,
    where = "ccc"
}
```
Note that after desugaring every generated entity will have the same *order*. You can reference *gen_id* field to set it customly:
```lua
{
    entity_type = "location",
    path = "&TableValueRandom(paths_table)&",
    ["generate:where"] = "$this.path$",
    order = "$this.where_gen_id$"
}
```