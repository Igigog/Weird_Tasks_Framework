--_IGI_DEBUG = false
local CACHE = require("for_tests.CACHE")

local TASK_STATUSES = igi_subtask.TASK_STATUSES
--print_table(CACHE)
igi_subtask.change_subtasks_status(CACHE, TASK_STATUSES.COMPLETED, TASK_STATUSES.READY_TO_FINISH)
--print_table(CACHE)
igi_subtask.change_subtasks_status(CACHE, TASK_STATUSES.READY_TO_FINISH, TASK_STATUSES.COMPLETED)
--print_table(CACHE)