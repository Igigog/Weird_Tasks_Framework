locations = {
    "agroprom": {
        "agr_smart_terrain_1_6_army_mechanic_stalker": "MECHANIC",
        "agr_1_6_medic_army_mlr": "MEDIC",
        "agr_smart_terrain_1_6_near_2_military_colonel_kovalski": "KUZNETSOV",
    },
    "bar": {
        "bar_visitors_stalker_mechanic": "MECHANIC",
        "bar_dolg_medic": "MEDIC",
        "bar_visitors_barman_stalker_trader": "BARKEEP",
        "bar_dolg_leader": "VORONIN",
        "bar_dolg_general_petrenko_stalker": "PETRENKO",
        "snitch": "SNITCH",
    },
    "darkscape": {
        "dasc_tech_mlr": "MECHANIC",
    },
    "darkvalley": {
        "val_smart_terrain_7_3_bandit_mechanic_stalker": "MECHANIC",
        "bandit_main_base_medic_mlr": "MEDIC",
        "zat_b7_bandit_boss_sultan": "SULTAN",
        "val_smart_terrain_7_4_bandit_trader_stalker": "OLIVIUS",
    },
    "deadcity": {
        "cit_killers_merc_mechanic_stalker": "MECHANIC",
        "cit_killers_merc_medic_stalker": "MEDIC",
        "cit_killers_merc_trader_stalker": "DUSHMAN",
        "cit_killers_merc_barman_mlr": "ASLAN",
    },
    "escape": {
        "esc_smart_terrain_5_7_loner_mechanic_stalker": "MECHANIC",
        "army_south_mechan_mlr": "MECHANIC",
        "drx_sl_esc_m_trader": "SIDOROVICH",
        "esc_2_12_stalker_wolf": "WOLF",
        "esc_2_12_stalker_nimble": "NIMBLE",
        "esc_3_16_military_trader": "MILITARY TRADER",
        "esc_2_12_stalker_fanat": "FANATIC",
    },
    "garbage": {
        "hunter_gar_trader_task": "BUTCHER",
        "baraholka_trader_night": "TRADER",
    },
    "jupiter": {
        "jup_b217_stalker_tech": "MECHANIC",
        "jup_cont_mech_bandit": "MECHANIC",
        "mechanic_monolith_jup_depo": "MECHANIC",
        "jup_a6_stalker_medik": "MEDIC",
        "drx_sl_jup_a6_freedom_leader": "LOKI",
        "jup_b6_scientist_tech": "TUKAREV",
        "jup_b220_trapper": "TRAPPER",
        "jup_b19_freedom_yar": "YAR",
        "jup_b6_scientist_nuclear_physicist": "HERMANN",
    },
    "marsh": {
        "mar_base_stalker_tech": "MECHANIC",
        "mar_smart_terrain_base_doctor": "MEDIC",
        "mar_smart_terrain_base_stalker_leader_marsh": "COLD",
        "mar_base_owl_stalker_trader": "SPORE",
        "mar_base_stalker_barmen": "LIBRARIAN",
    },
    "military": {
        "mil_smart_terrain_7_7_freedom_mechanic_stalker": "MECHANIC",
        "mil_freedom_medic": "MEDIC",
        "mil_smart_terrain_7_7_freedom_leader_stalker": "LUKASH",
        "mil_smart_terrain_7_10_freedom_trader_stalker": "SKINFLINT",
    },
    "pripyat2": {
        "pri_monolith_monolith_mechanic_stalker": "MECHANIC",
        "merc_pri_a18_mech_mlr": "MECHANIC",
        "mechanic_monolith_kbo": "MECHANIC",
        "pri_monolith_monolith_trader_stalker": "RABBIT",
        "lider_monolith_haron": "HARON",
        "monolith_eidolon": "EIDOLON",
        "merc_pri_grifon_mlr": "GRIFFIN",
    },
    "red_forest": {
        "red_greh_tech": "MECHANIC",
    },
    "truck": {
        "trucks_cemetery_bandit_mechanic": "MECHANIC",
    },
    "yantar": {
        "mechanic_army_yan_mlr": "MECHANIC",
        "yan_stalker_sakharov": "SAKHAROV",
    },
    "zaton": {
        "zat_a2_stalker_mechanic": "MECHANIC",
        "zat_stancia_mech_merc": "MECHANIC",
        "zat_tech_mlr": "MECHANIC",
        "zat_b22_stalker_medic": "MEDIC",
        "zat_a2_stalker_barmen": "BEARD",
        "zat_stancia_trader_merc": "MERC TRADER",
    },
}

icons = {
    "transaction": "ui_inGame2_Sdelka",
    "supply": "ui_inGame2_Osobiy_zakaz",
    "weapon": "ui_inGame2_Neizvestnoe_oruzhie",
    "mutant": "ui_iconsTotal_mutant",
    "heavy": "ui_inGame2_PD_master_boevih_sistem",
    "artifact_world": "ui_inGame2_Kontrakt_s_uchenimi",
    "artifact_stalker": "ui_inGame2_Kontrakt_s_uchenimi",
    "assault_monster_online": "ui_iconsTotal_mutant",
    "assault_stalker_online": "ui_inGame2_PD_Lider",
    "kill_stalker_nearby": "ui_inGame2_Odin_vistrel",
    "fetch_patches": "ui_icons_kill_stalker6",
}

quests = {
    "MECHANIC": [
        "transaction",
        "supply",
        "weapon",
        "mutant",
        "heavy",
    ],
    "MEDIC": [
        "artifact_world",
        "artifact_stalker",
    ],
    "BARKEEP": [
        "assault_monster_online",
        "kill_stalker_nearby",
    ],
    "OLIVIUS": [
        "assault_monster_online",
        "assault_stalker_online",
        "kill_stalker_nearby",
    ],
    "WOLF": [
        "assault_monster_online",
    ],
    "FANATIC": [
        "assault_monster_online",
    ],
    "BUTCHER": [
        "assault_monster_online",
    ],
    "TRAPPER": [
        "assault_monster_online",
        "kill_stalker_nearby",
    ],
    "BEARD": [
        "assault_monster_online",
    ],
    "KUZNETSOV": [
        "assault_stalker_online",
        "kill_stalker_nearby",
        "fetch_patches",
    ],
    "VORONIN": [
        "fetch_patches",
    ],
    "PETRENKO": [
        "assault_stalker_online",
        "kill_stalker_nearby",
    ],
    "SULTAN": [
        "kill_stalker_nearby",
        "fetch_patches",
    ],
    "DUSHMAN": [
        "kill_stalker_nearby",
    ],
    "ASLAN": [
        "kill_stalker_nearby",
        "fetch_patches",
    ],
    "SIDOROVICH": [
        "kill_stalker_nearby",
    ],
    "MILITARY TRADER": [
        "fetch_patches",
    ],
    "RABBIT": [
        "kill_stalker_nearby",
        "assault_stalker_online",
    ],
    "COLD": [
        "fetch_patches",
    ],
    "LUKASH": [
        "fetch_patches",
    ],
    "EIDOLON": [
        "fetch_patches",
    ],
    "HARON": [
        "fetch_patches",
    ],
    "GRIFFIN": [
        "fetch_patches",
    ],
    "MERC TRADER": [
        "fetch_patches",
    ], 
}
