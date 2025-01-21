# Weird Task Framework 4.0

Helo helo :3

This is the WTF guide! Some familiarity with vanilla Anomaly's task system is required to understand it;
if you're totally new, start with the [excellent guide from NLTP_ASHES](https://igigog.github.io/anomaly-modding-book/quests/task_guide.html). You don't need everything, but you will need to understand the task lifecycle.

So, are we starting now?

Disclaimer: it will be ugly in the middle. Just wait.

## We are starting now

Let's take a peek at a vanilla task section (chosen totally randomly, trust me):

```ini
;------------------------------------------------
; Petrenko (Duty Trader)
;------------------------------------------------
[bar_dolg_general_petrenko_stalker_task_1]	;-- Defend Rostok Task
icon = ui_inGame2_Issledovanie_anomaliy
storyline = false
prior = 85
repeat_timeout = 16200
precondition = {=validate_assault_task(bar_dolg_general_petrenko_stalker_task_1:2:1:nil:false:true:nil)} true, false
title = bar_dolg_general_petrenko_stalker_task_1_name
descr = bar_dolg_general_petrenko_stalker_task_1_text
job_descr = bar_dolg_general_petrenko_stalker_task_1_about
task_complete_descr = bar_dolg_general_petrenko_stalker_task_1_finish
stage_complete = 1
target_functor = assault_task_target_functor
status_functor = assault_task_status_functor
status_functor_params = killer, bandit
condlist_0 = {!task_giver_alive(bar_dolg_general_petrenko_stalker_task_1)} fail
on_job_descr = %=setup_assault_task(bar_dolg_general_petrenko_stalker_task_1)%
on_complete = %=reward_random_money(9500:11000) =reward_stash(true) =complete_task_inc_goodwill(50:dolg) =inc_task_stage(bar_dolg_general_petrenko_stalker_task_1) =drx_sl_unregister_task_giver(bar_dolg_general_petrenko_stalker_task_1) =drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)%
on_fail = %=fail_task_dec_goodwill(25:dolg) =drx_sl_unregister_task_giver(bar_dolg_general_petrenko_stalker_task_1) =drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)%
```

There is quite a lot happening here, huh? Let's try to move this task to WTF. These fields are not interesting:

```ini
storyline = false       ; false is default in WTF
prior = 85              ; priority is not a thing as of now
repeat_timeout = 16200  ; 16200 is default
stage_complete = 1      ; WTF has finer-grain control structure
```

Everything else will be there one way or another.

### Boilerplate

In WTF, each task has a `.json` definition file. Let's start by creating one:

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
}
```

Just two fields for now. You __*must*__ define `WTF_VERSION`, otherwise your task won't start. Starting with version 4.0, WTF will try its best to __not break your quests__ with updates. Oh, and icon is also there.

Now, we will need a bit of stuff to make quest logic happen. We are adding the precondition, status functor and on_complete + on_fail. Don't look too much into it, I will explain everything later.

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": [
        "$ xr_conditions.validate_assault_task(nil, nil, {'bar_dolg_general_petrenko_stalker_task_1',2,1,nil,false,true,nil})"
    ],
    "entities": [
        {
            "CONTROLLER": "{status = function(tsk) return task_status_functor.assault_task_status_functor(tsk, 'bar_dolg_general_petrenko_stalker_task_1') end, quest_target = function(tsk) task_functor.assault_task_target_functor('bar_dolg_general_petrenko_stalker_task_1', 'target', tsk) end}"
        }
    ],
    "on_complete": "xr_effects.reward_random_money(9500:11000) xr_effects.reward_stash(true) xr_effects.complete_task_inc_goodwill(50:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)",
    "on_fail": "xr_effects.fail_task_dec_goodwill(25:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)"
}
```

This... sucks, to be quite honest. Looks like atrocious, unreadable mess. It will get better once we make it WTF-native.

Still, there is something to learn here. These lines are removed from `on_complete` and `on_fail` - WTF takes care of it for us.
```
=inc_task_stage(bar_dolg_general_petrenko_stalker_task_1)
=drx_sl_unregister_task_giver(bar_dolg_general_petrenko_stalker_task_1)
```

### Preconditions and Requirements
Notice how the precondition is now called `requirement` and not `precondition`: that's for a reason. There are two types of preconditions you can set in WTF: the ones you set as a game designer, called `preconditions`, and the ones you set as a programmer, called `requirements`. 

`status_functor` of this task will absolutely not work, unless `validate_assault_task` returns `true`. That's a `requirement`, because this task will undoubtedly __break__ or __cause crashes__ unless this requirement is met.

Something like "this task is not available until you have 300 goodwill" will not break anything if it is skipped, so that's a `precondition`. Preconditions are not checked in debug mode.

### Entities

A task in WTF is split into `entities`. For now, we only have one. An `entity` is just a blob of data, and the only special thing about entities is that __each entity__ may have a `CONTROLLER`.

`CONTROLLER` is like a supercharged `status_functor`. I will touch controllers later, but the most important thing in them is that they have `status` and `quest_target` methods, corresponding to `status_functor` and `target_functor`.

Anyway, there is still a bit of stuff to do.

### Task givers

So, remember how each task in vanilla needed a ltx section for each task giver? Forget it, we doin json definitions now, WTF will take care of the rest.

To define which task giver will have your task, you need to add `quest_givers` field to the definition:

```json
"quest_givers": [
    {"Petrenko": true}
]
```

Task givers are defined by sets of `tags`. What we wrote above means
"There is one set of task givers for this task, and that's those with tag `Petrenko`"

Here is how you give your task to every Medic in the game and every Mechanic in the Bar:
```json
"quest_givers": [
    {"Medic": true},
    {"Mechanic": true, "Bar": true}
]
```

You can check tags for every task giver in `gamedata/configs/igi_tasks/base.ltx`. Let's take a peek:

`gamedata/configs/igi_tasks/base.ltx:`
```ini
[npc_tags]
; Bar
bar_visitors_stalker_mechanic      = Mechanic, Bar, Duty
bar_dolg_medic                     = Medic, Bar, Duty
bar_visitors_barman_stalker_trader = Barman, Trader, Loner, Bar, Barkeep
bar_dolg_leader                    = Trader, Bar, Duty, Voronin
bar_dolg_general_petrenko_stalker  = Leader, Bar, Duty, Petrenko
```

Nice. A few things left: condlist, on_job_descr and description. Let's start with condlists.

### Actions

There are no condlists in WTF. Next.

#### Stop but for real?

There kinda are. WTF calls them `actions`. We'll be writing pure lua instead of condlists. Here's how it will look:

```json
"actions": [
    {
        "when": "not xr.conditions.task_giver_alive('bar_dolg_general_petrenko_stalker_task_1')",
        "run": "task_manager.get_task_manager():set_task_failed('bar_dolg_general_petrenko_stalker_task_1') or true"
    }
]
```

Notice the "or true" at the end of `run`: Every action will run only once, unless you return true. Other that that, it's just lua, kinda self-explanatory.

### Description

There is a bit of work to do to make descriptions work. WTF expects you to format your text id's like this:

```ini
title               = $KEY_name
descr               = $KEY_text
job_descr           = $KEY_about
task_complete_descr = $KEY_finish
```

Where `$KEY` is either of these:
```
igi_task_text_$FOLDER_$FILENAME_$TASKGIVER
igi_task_text_$FOLDER_$FILENAME
```

which, in case of `gamedata/configs/igi_tasks/tasks/MyMod/my_task.json`, corresponds to (notice the folder is lowercase):
```
igi_task_text_mymod_my_task_bar_dolg_general_petrenko_stalker
igi_task_text_mymod_my_task
```

This is, of course, absolutely not how vanilla quest texts are structured. Luckily, description key can be overridden:

```json
"description_key": "bar_dolg_general_petrenko_stalker_task_1",
```

That should take care of the texts. Now, what does `on_job_descr` does again?
```lua
xr_effects.setup_assault_task = function(actor, npc, p)
	...
    local squad_id = cache_assault[task_id].squad_id
    local smart_id = cache_assault[task_id].smart_id
    local squad = squad_id and alife_object(squad_id)
    local smart = smart_id and alife_object(smart_id)
    if squad and smart then
        squad.stay_time = game.get_game_time()
        sim_offline_combat.task_squads[squad_id] = true
        local tbl = {
            smart_id = smart_id,
            squad_id = squad_id,
            is_enemy = cache_assault[task_id].is_enemy,
            scripted = cache_assault[task_id].scripted,
        }
        save_var(db.actor, task_id, tbl)
        
        CreateTimeEvent(0,"setup_assault_task",0,postpone_for_next_frame,task_id, squad_id)
    end
end

function postpone_for_next_frame(task_id, squad_id)
	...
    db.actor:give_talk_message2(news_caption, news_text, news_ico, "iconed_answer_item")
	return true
end
```

Moves stuff around, but, more importantly, shows a message to the player. 

WTF has a default function, which will show this message to the player. It plays nicely with WTF-native entities, but it will absolutely choke on this vanilla-style mess. Let's override it too:

```json
"description": "{show_description = function() xr.effects.setup_assault_task('bar_dolg_general_petrenko_stalker_task_1') end}"
```

With this, we are done.

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": [
        "$ xr_conditions.validate_assault_task(nil, nil, {'bar_dolg_general_petrenko_stalker_task_1',2,1,nil,false,true,nil})"
    ],
    "entities": [
        {
            "CONTROLLER": "{status = function() return task_status_functor.assault_task_status_functor({}, 'bar_dolg_general_petrenko_stalker_task_1') end, quest_target = function() task_functor.assault_task_target_functor('bar_dolg_general_petrenko_stalker_task_1', 'target', {}) end}"
        }
    ],
    "on_complete": "xr_effects.reward_random_money(9500:11000) xr_effects.reward_stash(true) xr_effects.complete_task_inc_goodwill(50:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)",
    "on_fail": "xr_effects.fail_task_dec_goodwill(25:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)",
    "quest_givers": [
        {"Petrenko": true}
    ],
    "actions": [
    {
        "when": "not xr.conditions.task_giver_alive('bar_dolg_general_petrenko_stalker_task_1')",
        "run": "task_manager.get_task_manager():set_task_failed('bar_dolg_general_petrenko_stalker_task_1') or true"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
    "description": "{show_description = function() xr.effects.setup_assault_task('bar_dolg_general_petrenko_stalker_task_1') end}"
}
```

Well... Not really, since it doesn't work. If you really want to run something like this under WTF, you need a few more terrible hacks. I also set Lukash as the task giver to not mess with the original. Here's how a runnable version looks like:

```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": [
        "$ xr_conditions.validate_assault_task(nil, nil, {'bar_dolg_general_petrenko_stalker_task_1','2','1','nil','false','true','nil'})"
    ],
    "entities": [
        {
            "CONTROLLER": "{status = function(tsk) if tsk.stage == 1 then return 'complete' end return task_status_functor.assault_task_status_functor(tsk, 'bar_dolg_general_petrenko_stalker_task_1') end, quest_target = function(tsk) return task_functor.assault_task_target_functor('bar_dolg_general_petrenko_stalker_task_1', 'target', nil, tsk) end}"
        }
    ],
    "on_complete": "(function () xr_effects.reward_random_money(nil, nil, {'9500','11000'}) xr_effects.reward_stash(nil, nil, {'true'}) xr_effects.complete_task_inc_goodwill(nil, nil, {'50', 'dolg'}) end)()",
    "on_fail": "(function () xr_effects.fail_task_dec_goodwill(nil, nil, {'25', 'dolg'}))()",
    "quest_givers": [
        {"Lukash": true}
    ],
    "actions": [
    {
        "when": "not xr_conditions.task_giver_alive(nil, nil, {'bar_dolg_general_petrenko_stalker_task_1'})",
        "run": "task_manager.get_task_manager():set_task_failed('bar_dolg_general_petrenko_stalker_task_1') or true"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
    "DESCRIPTION": "{show_description = function() xr_effects.setup_assault_task(nil, nil, {'bar_dolg_general_petrenko_stalker_task_1'}) end}"
}
```

What a terrible stinking mess. Why the actual fuck did we do it to ourselves?

You'll be surprised, but just naively transferring vanilla quests to WTF brings a few upsides:

1. This task will not cause a CTD anymore. WTF's robust error handling means even if you change any of the functors and they will crash, this crash will be handled gracefully. Unless you fuck up some engine call; then you're still fucked.
2. Users have an option to disable this task via MCM
3. Users have an option to cancel this task via MCM if anything goes wrong
4. You can add your task to other quest givers without pain.

Now, let's also make it not terrible.

## Macros
You may have understood already, but inline lua is a central piece of WTF. Well, guess what?

#### we didn't even start

Notice how the requirement we have is the only lua line starting with `$`. Lines starting with `$` are very special - they will be __evaluated inline__. This means, that if you write

```json
"id": "$ db.actor:id()"
```

WTF will see it as:

```json
"id": 0
```

This also means, that fields `preconditions` and `requirements` are just arrays of booleans. Pretty neat, don't ya think? Transforming macros is a part of a process called `MLG run` (MLG stands for Macros, Linker, Generation).

__Macros may never return nil__. Returning nil is hard error.

Neat, but why macros? Well, it's for

### State management

Let's take a look what `validate_assault_task` does:

```lua
xr_conditions.validate_assault_task = function(actor, npc, p)
	...
	--// Search all smarts
	local targets = ...
	
	--// Cache results
	if is_not_empty(targets) then
		cache_assault[task_id] = {
			squad_id = target_squad,
			smart_id = target_smart,
			is_enemy = def.is_enemy,
			scripted = def.scripted
		}
		
		return true
	end

	return false
end
```

It finds a target for the quest and saves it into some hidden global state. We can do better.

`Entity` is just blob of data, but you know what state is? A blob of data. We savin' everything inside of `entity`.

```json
entities: [
    {
        "CONTROLLER": ...,
        "squad_id": ...,
        "smart_id": ...,
        "is_enemy": true,
        "scripted": false
    }
]
```

How do we get id for a squad? The logic from `tasks_assault` looks about like this:
```lua
function igi_assault.get_squads(def, enemy_faction_list)
    local targets = {}
    for name,v in pairs(SIMBOARD.smarts_by_names) do
        -- if smart is available
        if (simulation_objects.available_by_id[v.id] == true) then
        
            -- if smart is not in blacklisted location
            local smart_level = alife():level_name(gg:vertex(v.m_game_vertex_id):level_id())
            if (not blacklisted_maps[smart_level]) then
            
                -- if smart location is proper to the parameter
                local is_online = v.online
                local is_nearby = string.find(simulation_objects.config:r_value(actor_level, "target_maps", 0, ""), smart_level)
                if ((def.scan == 1) and is_online) -- same level
                or ((def.scan == 2) and (is_online or is_nearby)) -- same + nearby level
                or ((def.scan == 3) and is_nearby) -- nearby levels only
                or ((def.scan == 4) and (not (is_online or is_nearby))) -- far levels only
                or (def.scan == 5) -- anywhere
                then
                    evaluate_smarts_squads(task_id, targets, v, def, enemy_faction_list) 
                end
            end
        end
    end

    local out = {}
	for squad_id in pairs(targets) do
		out[#out+1] = squad_id
	end

    return #out > 0 and out[math.random(#out)]
end
```

I made it shorter. It wasn't really a nice function like this. Whatever, just proves my point. There is more state! `def.scan` is defined in ltx section of this task, except it's just one of unnamed parameters and you need to count to know what it is. It is `2`. Thank me later. Unless I counted it wrong. By the way, `blacklisted_maps` is a `local` in `tasks_assault`. `enemy_faction_list` is defined in `status_functor_params` in task section. Naturally.

We can actually work with that already! See, see?

```json
{
    "CONTROLLER": ...,
    "squad_id": "$ igi_assault.get_squads({scan = 2}, {'killer', 'bandit'})",
    "smart_id": ...,
    "is_enemy": true,
    "scripted": false
}
```

Now we have either `false` or id in the `squad_id` field. How do we get `smart_id`? Somewhere in task spaghetti you can find `if squad.current_target_id == smrt_id...`, which kinda gives us a hint.

```json
"smart_id": "$ alife_object(??).current_target_id"
```

Now we just need to move `squad_id` with some kind of

### Linker
No intro. It looks like this:

```json
"squad_id": "$ igi_assault.get_squads({scan = 2}, {'killer', 'bandit'})",
"smart_id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id"
```

`this` is a special keyword that refers to current entity. It's not valid outside of entities. If you want to refer to some entity field from outside, you need to add `link_id`:

```json
{
    "CONTROLLER": ...,
    "squad_id": "$ igi_assault.get_squads({scan = 2}, {'killer', 'bandit'})",
    "smart_id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "is_enemy": true,
    "scripted": false,
    "link_id": "squad"
}
```

Since there is no hidden state now, we can rewrite the `requirements`:

```json
"requirements": ["$ |squad.squad_id|"],
```

Nice.

### Cute macro stuff

There is still a bit to say about macros and linker. 
1. Other than `this`, there is also a special link_id called `CACHE`, which refers to the whole task table. CACHE has a few values set automatically, most interesting of which are `|CACHE.task_id|` and `|CACHE.task_giver_id|`

2. You can name your macros. Macro name is a prefix before `$`, meaning `1$ true` has the name "1". In fact, the name "" (empty string) is a special macro name which will be evaluated automatically as part of precondition function.

3. Macros with the name "1" will be evaluated automatically after the player accepted the task. Use them to create game objects.

4. You can invoke macro evaluation by calling `igi_generic_task.process_macros(task_id, macro_name)`

### Let's finish with this entity

There's a bit of stuff we can do to both make our entity definition more debuggable and our code more reusable. I'll split `igi_assault.get_squads` into two functions, first of which gives back all suitable smarts, and the second one - all suitable squads. I will also remove random choice of the id. 

```lua
function igi_assault.get_smarts(scan)
    local smarts = {}
    for name,v in pairs(SIMBOARD.smarts_by_names) do
        -- if smart is available
        if (simulation_objects.available_by_id[v.id] == true) then
        
            -- if smart is not in blacklisted location
            local smart_level = alife():level_name(gg:vertex(v.m_game_vertex_id):level_id())
            if (not blacklisted_maps[smart_level]) then
            
                -- if smart location is proper to the parameter
                local is_online = v.online
                local is_nearby = string.find(simulation_objects.config:r_value(actor_level, "target_maps", 0, ""), smart_level)
                if ((scan == 1) and is_online) -- same level
                or ((scan == 2) and (is_online or is_nearby)) -- same + nearby level
                or ((scan == 3) and is_nearby) -- nearby levels only
                or ((scan == 4) and (not (is_online or is_nearby))) -- far levels only
                or (scan == 5) -- anywhere
                then
                    smarts[#smarts+1] = name
                end
            end
        end
    end
    return smarts
end

function get_squads(smarts, enemy_faction_list)
    local targets = {}
    for _, id in pairs(smarts) do
        local smrt = alife_object(id)
        tasks_assault.evaluate_smarts_squads(nil, targets, smrt, {num = 0}, enemy_faction_list)
    end

	local out = {}
	for squad_id in pairs(targets) do
		out[#out+1] = squad_id
	end
    return out
end
```

```json
{
    "CONTROLLER": ...,
    "smart_names": "$ igi_assault.get_smarts(2)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_names|, {killer = true, bandit = true})",
    "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
    "smart_id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "is_enemy": true,
    "scripted": false,
    "link_id": "squad"
}
```

Better? Yes, but you don't understand yet, why. Two reasons:
1. There is a LOT of logging in debug mode of WTF. You will see *exactly* where your task broke just by looking at logs.
2. It just so happens, that "all suitable smarts by distance" is kinda common thing to want, so there is a built-in function in WTF for that. Which means, it transforms to: 

```lua
function igi_assault.get_squads(smarts, enemy_faction_list)
    local targets = {}
    for _, id in pairs(smarts)
        local smrt = alife_object(id)
        evaluate_smarts_squads(task_id, targets, smrt, def, enemy_faction_list)
    end
    return targets
end
```

```json
{
    "CONTROLLER": ...,
    "smart_ids": "$ igi_finder.get_smarts(0, 1)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
    "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
    "smart_id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "is_enemy": true,
    "scripted": false,
    "link_id": "squad"
}
```

Which is quite a bit less code to debug, WITH better logging than before. For free. More than for free; it's as if WTF is giving you money at this point.

## Controller

Look, I won't sugar-coat it. I already implemented assault-type controller. In 2022.

```json
{
    "CONTROLLER": "igi_target_assault.Assault",
    "smart_ids": "$ igi_finder.get_smarts(0, 1)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
    "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
    "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "link_id": "squad"
}
```

Instead, here is a rundown of what a controller is. As I said before, controller is like a overcharged status functor; it holds the logic for your data. You *may* implement any of these functions in controller:

```lua
status(entity) -> igi_subtask.TASK_STATUSES -- status_functor, returns status for entity
quest_target(entity) -> number -- target_functor, only works if status is also implemented
complexity(entity) -> number -- complexity of this entity, (coincidentally) measured in RUB. Default rewarder uses this value.
description(entity) -> {
    targets = {string...},
    locations = {string...},
    factions = {string...}
} -- override values of default description function
test(entity) -> boolean -- test framework not yet stable, ignore
```

WTF comes with these controllers:
```lua
igi_target_assault.Assault -- kill every enemy on a smart
igi_target_escort.Escort -- untested, make squad a companion
igi_target_fetch.Fetch -- collect N items
igi_target_get.Get -- take an item into inventory. Completes right after that.
igi_target_return.Return -- take an item into inventory. Return it to quest giver.
igi_target_shoot.Shoot -- shoot (and hit) an enemy. Killing is optional.
igi_target_visit.Visit -- come close to an object
```

## Callbacks

Of course there are callbacks. What are we even modding?

Ima be honest, chief - callback system didn't receive much love, and I'll need to rehaul it a bit. Still, there are a few useful things. These are the callbacks:

`igi_callbacks.script:`
```lua
local callbacks = {
	on_get_taskdata = {},
	entity_on_get_taskdata = {},

	on_first_run = {},
	entity_on_first_run = {},

	on_task_update = {},
	entity_on_task_update = {},

	on_complete = {},
	entity_on_complete = {},

	on_fail = {},
	entity_on_fail = {},

	on_finish = {},
	entity_on_finish = {},

	on_subtask_status_change = {},
	entity_on_subtask_status_change = {},

	on_before_rewarding = {},
	entity_on_before_rewarding = {},
}
```

Two sets. The ones without `entity_` you can add to your CACHE, like we did with `on_complete`. The ones with `entity_` will be sent to the controller, if it has corresponding function.

## Addendum. What if I want more?

Imagine: you want to assault two smarts instead of one in your task. Where would you even start in vanilla? Changing hidden state? Breaking status functor? My heart shatters at the thought.

Turns out, it's quiet easy in WTF. Just use two entities.

```json
entities: [
{
    "CONTROLLER": "igi_target_assault.Assault",
    "smart_ids": "$ igi_finder.get_smarts(0, 1)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
    "squad_id": "$ #|this.squad_ids| > 1 and |this.squad_ids|[1]",
    "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "link_id": "squad"
},
{
    "CONTROLLER": "igi_target_assault.Assault",
    "squad_id": "$ #|squad.squad_ids| > 1 and |squad.squad_ids|[2]",
    "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
}
]
```

Kinda trivial. What if I want more? One more. Two more.

#### ALL THE SMARTS.

You can manually create entities all you want, but you will never know how many smarts there actually are, so you can't target all smarts.

Unless I've built something for exactly that, that is.

So, let me introduce you to another special entity field: `GEN`. Stands for "generator", as in, "entity generation". Generator functions are actually stupidly easy to write. Here's one:

```lua
function copy(entity)
    local n = entity.amount or 1
    local new_entities = {}
    for _=1, n do
        new_entities[#new_entities+1] = dup_table(entity)
    end
    return new_entities
end
```

There are two built-in generator functions in WTF:


`igi_generate.Amount(n)` - make an entity into n copies of itself


`igi_generate.Split(in, out, amount?)` - take one value from field in, put in field out, repeat until done or until `amount` is reached. Values are taken in random order.

Which means, if you want ALL THE SMARTS, here's what you need:

```json
entities: [
{
    "CONTROLLER": "igi_target_assault.Assault",
    "GEN": "igi_generate.Split('squad_ids', 'squad_id')",
    "smart_ids": "$ igi_finder.get_smarts(0, 1)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
    "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "link_id": "squad"
}
]
```

Or, if you only want 5:
```json
entities: [
{
    "CONTROLLER": "igi_target_assault.Assault",
    "GEN": "igi_generate.Split('squad_ids', 'squad_id', 5)",
    "smart_ids": "$ igi_finder.get_smarts(0, 1)",
    "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
    "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
    "link_id": "squad"
}
]
```

`igi_generate.Split` does not do anything, if there are not enough values to reach `amount`. It's actually kinda nice to use it to pull random items from tables.

### Rewards

So, what are we left with?

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": ["$ |squad.squad_id|"],
    "entities": [
        {
            "CONTROLLER": "igi_target_assault.Assault",
            "smart_ids": "$ igi_finder.get_smarts(0, 1)",
            "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
            "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
            "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
            "link_id": "squad"
        }
    ],
    "on_complete": "xr_effects.reward_random_money(9500:11000) xr_effects.reward_stash(true) xr_effects.complete_task_inc_goodwill(50:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)",
    "on_fail": "xr_effects.fail_task_dec_goodwill(25:dolg) xr_effects.drx_sl_reset_stored_task(bar_dolg_general_petrenko_stalker_task_1)",
    "quest_givers": [
        {"Petrenko": true}
    ],
    "actions": [
    {
        "when": "$ 'not xr_conditions.task_giver_alive(nil, nil, {|CACHE.task_id|})'",
        "run": "$ 'task_manager.get_task_manager():set_task_failed(|CACHE.task_id|) or true'"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
    "description": "{show_description = function() xr.effects.setup_assault_task('bar_dolg_general_petrenko_stalker_task_1') end}"
]
}
```

Looks a bit better. Still, these pesky `on_complete` and `on_fail` are kind of an eyesore. Since WTF manages our state for us now, we don't need these `xr_effects.drx_sl_reset_stored_task`. Let's remove them.

```json
"on_complete": "xr_effects.reward_random_money(9500:11000) xr_effects.reward_stash(true) xr_effects.complete_task_inc_goodwill(50:dolg)",
"on_fail": "xr_effects.fail_task_dec_goodwill(25:dolg)",
```

A bit better, but it's still kinda problematic that we manage rewards in callbacks. A lot of fancy stuff can be done with rewards, so let's make them WTF-native. Field `rewarder` can help us here:

```json
"rewarder": "igi_rewards.Static({money = 10000, goodwill = 50})"
```
Good ol' static rewarder, giving us 10 000 RUB (corrected for inflation) and 50 goodwill. Three good things about rewarders:
1. They know the faction of your task giver, you don't need to type it.
2. They show the rewards in the description.
3. They are influenced by economy settings and WTF's own MCM sliders.

So, that's cool. Actually, you don't even need this. Controller `igi_target_assault.Assault` implements `complexity`, so it will do an okay-ish job at determining the amount of rewards. If you just leave yourself with no rewarder, default rewarder will take care of it all by itself.

Default rewarder is actually stupid easy: it sums up `complexity` from all entities, then pays 80% of it directly as money, and the other 20% as goodwill with the rate of 1 goodwill per 50 points.

Let's just have WTF defaults do their job.

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": ["$ |squad.squad_id|"],
    "entities": [
        {
            "CONTROLLER": "igi_target_assault.Assault",
            "smart_ids": "$ igi_finder.get_smarts(0, 1)",
            "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
            "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
            "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
            "link_id": "squad"
        }
    ],
    "on_complete": "xr_effects.reward_stash(nil, nil, {'true'})",
    "on_fail": "xr_effects.fail_task_dec_goodwill(nil, nil, {'25','dolg'})",
    "quest_givers": [
        {"Petrenko": true}
    ],
    "actions": [
    {
        "when": "$ 'not xr_conditions.task_giver_alive(nil, nil, {|CACHE.task_id|})'",
        "run": "$ 'task_manager.get_task_manager():set_task_failed(|CACHE.task_id|) or true'"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
    "description": "{show_description = function() xr.effects.setup_assault_task('bar_dolg_general_petrenko_stalker_task_1') end}"
]
}
```

What about on_fail, you ask? Nothing. I haven't implemented it yet :(

## Description

Description field is the only eyesore left here. Let's just remove it.

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": ["$ |squad.squad_id|"],
    "entities": [
        {
            "CONTROLLER": "igi_target_assault.Assault",
            "smart_ids": "$ igi_finder.get_smarts(0, 1)",
            "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
            "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
            "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
            "link_id": "squad"
        }
    ],
    "on_complete": "xr_effects.reward_stash(nil, nil, {'true'})",
    "on_fail": "xr_effects.fail_task_dec_goodwill(nil, nil, {'25','dolg'})",
    "quest_givers": [
        {"Petrenko": true}
    ],
    "actions": [
    {
        "when": "$ 'not xr_conditions.task_giver_alive(nil, nil, {|CACHE.task_id|})'",
        "run": "$ 'task_manager.get_task_manager():set_task_failed(|CACHE.task_id|) or true'"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
]
}
```

Great, but now we have no description whatsoever. What do we want to show to the user? The location would be nice, and maybe the faction of the enemy for flavor. Rewards will be taken care of automagically.

In fact, if you have an entity, which field `id` corresponds to a smart terrain, default description function will take that as a location automatically. All you need to do is to add `to_description: true`.

In fact, in the same way, if you have an entity with `id` of a squad, its faction will be added to description. Here, take a look:

`gamedata/configs/igi_tasks/tasks/MyMod/my_task.json:`
```json
{
	"WTF_VERSION": "4.0",
    "icon": "ui_inGame2_Issledovanie_anomaliy",
    "requirements": ["$ |squad.squad_id|"],
    "entities": [
        {
            "CONTROLLER": "igi_target_assault.Assault",
            "smart_ids": "$ igi_finder.get_smarts(0, 1)",
            "squad_ids": "$ igi_assault.get_squads(|this.smart_ids|, {killer = true, bandit = true})",
            "squad_id": "$ #|this.squad_ids| > 0 and |this.squad_ids|[math.random(#|this.squad_ids|)]",
            "id": "$ |this.squad_id| and alife_object(|this.squad_id|).current_target_id",
            "link_id": "squad",
            "to_description": true
        },
        {
            "id": "|squad.squad_id|",
            "to_description": true
        }
    ],
    "on_complete": "xr_effects.reward_stash(nil, nil, {'true'})",
    "on_fail": "xr_effects.fail_task_dec_goodwill(nil, nil, {'25','dolg'})",
    "actions": [
    {
        "when": "$ 'not xr_conditions.task_giver_alive(nil, nil, {|CACHE.task_id|})'",
        "run": "$ 'task_manager.get_task_manager():set_task_failed(|CACHE.task_id|) or true'"
    }
    ],
    "description_key": "bar_dolg_general_petrenko_stalker_task_1",
    "quest_givers": [
        {"Petrenko": true}
    ]
}
```

And that's it. That's a WTF-native quest. We have:
1. State taken care of automatically.
2. Logs and crash handling
2. Task registered in one line instead of the whole ltx section
2. Rewards taken care of automagically
2. Description taken care of automatically
2. And all of that while writing LESS CODE, as either one-liners or small self-contained functions.

Kinda cool if you ask me.

## So, that's it, then?

Yep. Take care!

\- Igi
