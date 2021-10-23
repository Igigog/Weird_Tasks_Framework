return {
	['task_name'] = '',
	['task_id'] = 'mil_smart_terrain_7_7_freedom_mechanic_stalker_task_gt_supply',
	['task_giver_id'] = 20234,
	['status'] = 'completed',
	['group_counter'] = {
		['location'] = 1,
		['item'] = 1,
		['squad'] = 1
	},
	['online_activities'] = {
 
	},
	['target'] = {
		['$item_1_1$'] = {
			['order'] = 1,
			['where'] = 17175,
			['id'] = 1640,
			['status'] = 'ready_to_finish',
			['where_link'] = '$location_1_1$',
			['target'] = 'return',
			['reward'] = {
				['failed'] = {
					['goodwill'] = {
						['factions'] = {
							[1] = 'freedom'
						},
						['value'] = -75
					},
					['money'] = 0
				},
				['completed'] = {
					['goodwill'] = {
						['factions'] = {
							[1] = 'freedom'
						},
						['value'] = 20
					},
					['money'] = 1875
				}
			},
			['to_create'] = true,
			['group_id'] = 1,
			['entity_type'] = 'item',
			['section_name'] = 'gt_package_ammunition',
			['mark'] = 'treasure_unique'
		},
		['$item_1_2$'] = {
			['order'] = 1,
			['where'] = 17175,
			['id'] = 1641,
			['status'] = 'completed',
			['where_link'] = '$location_1_1$',
			['target'] = 'return',
			['reward'] = {
				['failed'] = {
					['goodwill'] = {
						['factions'] = {
							[1] = 'freedom'
						},
						['value'] = -75
					},
					['money'] = 0
				},
				['completed'] = {
					['money'] = 1875,
					['goodwill'] = {
						['freedom'] = 20
					}
				}
			},
			['to_create'] = true,
			['group_id'] = 1,
			['entity_type'] = 'item',
			['section_name'] = 'gt_package_ammunition',
			['mark'] = 'treasure_unique'
		},
		['$squad_1_2$'] = {
			['order'] = 1,
			['group_id'] = 1,
			['to_create'] = true,
			['status'] = 'running',
			['where_link'] = '$location_1_1$',
			['id'] = 1997,
			['faction'] = 'army',
			['where'] = 17175,
			['entity_type'] = 'squad',
			['section_name'] = 'gt_stalker_guard_army',
			['typ'] = 'squad'
		},
		['$location_1_1$'] = {
			['order'] = 1,
			['where'] = '1,1',
			['id'] = 17175,
			['status'] = 'completed',
			['target'] = 'assault',
			['ara_to_kill'] = {
				[1647] = true,
				[1998] = true,
				[1966] = true,
				[1668] = true,
				[1973] = true,
				[1970] = true,
				[1663] = true
			},
			['reward'] = {
				['failed'] = {
					['goodwill'] = {
						['factions'] = {
							[1] = 'freedom'
						},
						['value'] = -25
					},
					['money'] = 0
				},
				['completed'] = {
					['money'] = 3000,
					['goodwill'] = {
						['freedom'] = 25
					}
				}
			},
			['entity_type'] = 'location',
			['squads'] = {
				[1] = 1642,
				[2] = 1997
			},
			['group_id'] = 1,
			['smarts'] = {
				[1] = 17175
			}
		},
		['$squad_1_1$'] = {
			['order'] = 1,
			['group_id'] = 1,
			['to_create'] = true,
			['status'] = 'running',
			['where_link'] = '$location_1_1$',
			['id'] = 1642,
			['faction'] = 'army',
			['where'] = 17175,
			['entity_type'] = 'squad',
			['section_name'] = 'gt_stalker_guard_army',
			['typ'] = 'squad'
		}
	},
	['reward'] = {
		['money'] = 4875,
		['goodwill'] = {
			['freedom'] = 45
		}
	},
	['activities'] = {
 
	},
	['subtasks'] = {
		['ready_to_finish'] = {
			['priorities'] = {
				[1] = 1
			},
			['payloads'] = {
				[1] = '$item_1_1$'
			}
		},
		['completed'] = {
			['priorities'] = {
				[1] = 1,
				[2] = 1
			},
			['payloads'] = {
				[1] = '$location_1_1$',
				[2] = '$item_1_2$'
			}
		},
		['disabled'] = {
			['priorities'] = {
 
			},
			['payloads'] = {
 
			}
		},
		['failed'] = {
			['priorities'] = {
 
			},
			['payloads'] = {
 
			}
		},
		['running'] = {
			['priorities'] = {
 
			},
			['payloads'] = {
 
			}
		},
		['cancelled'] = {
			['priorities'] = {
 
			},
			['payloads'] = {
 
			}
		}
	},
	['objects'] = {
 
	},
	['current_target_id'] = 20234,
	['description'] = '?????: ????? ?????\n ???????????: ???????\n '
}