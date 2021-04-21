AUTHOR = "Igigog"
PREFIX = "docs"

fs = frozenset
factions = {
    "Loner",
    "Army",
    "Duty",
    "Freedom",
    "Bandit",
    "Mercenary",
    "Fanatic",
    "Ecolog",
    "ClearSky",
    "Monolith",
    "Renegade",
    "Greh",
    "UNISG",
}

npc = {
	# Agroprom
	"agr_smart_terrain_1_6_army_mechanic_stalker": {"Mechanic", "Agroprom", "Army"},
	"agr_1_6_medic_army_mlr": {"Medic", "Agroprom", "Army"},
	"agr_smart_terrain_1_6_near_2_military_colonel_kovalski": {"Leader", "Agroprom", "Army", "Kuznetsov"},
	# Bar
	"bar_visitors_stalker_mechanic": {"Mechanic", "Bar", "Duty"},
	"bar_dolg_medic": {"Medic", "Bar", "Duty"},
	"bar_visitors_barman_stalker_trader": {"Barman", "Trader", "Loner", "Bar", "Barkeep"},
	"bar_dolg_leader": {"Trader", "Bar", "Duty", "Voronin"},
	"bar_dolg_general_petrenko_stalker": {"Leader", "Bar", "Duty", "Petrenko"},
	"snitch": {"Bar", "Loner", "Snitch"},
	# Darkscape
	"dasc_tech_mlr": {"Mechanic", "Darkscape", "Loner"},
	# Dark Valley
	"val_smart_terrain_7_3_bandit_mechanic_stalker": {"Mechanic", "DarkValley", "Bandit"},
	"bandit_main_base_medic_mlr": {"Medic", "DarkValley", "Bandit"},
	"zat_b7_bandit_boss_sultan": {"Leader", "DarkValley", "Bandit", "Sultan"},
	"val_smart_terrain_7_4_bandit_trader_stalker": {"Trader", "DarkValley", "Bandit", "Olivius"},
	# Dead City
	"cit_killers_merc_mechanic_stalker": {"Mechanic", "DeadCity", "Mercenary"},
	"cit_killers_merc_medic_stalker": {"Medic", "DeadCity", "Mercenary"},
	"cit_killers_merc_trader_stalker": {"Leader", "Trader", "DeadCity", "Mercenary", "Dushman"},
	"cit_killers_merc_barman_mlr": {"Barman", "Trader", "DeadCity", "Mercenary", "Aslan"},
	# Escape
	"esc_smart_terrain_5_7_loner_mechanic_stalker": {"Mechanic", "Escape", "Loner"},
	"army_south_mechan_mlr": {"Mechanic", "Escape", "Army"},
	"esc_m_trader": {"Trader", "Leader", "Escape", "Loner", "Sidorovich"},
	"esc_2_12_stalker_wolf": {"TaskGiver", "Loner", "Escape", "Wolf"},
	"esc_2_12_stalker_nimble": {"Trader", "Loner", "Escape", "Nimble"},
	"esc_3_16_military_trader": {"Trader", "Army", "Escape"},
	"esc_2_12_stalker_fanat": {"TaskGiver", "Loner", "Escape", "Fanatic"},
	# Garbage
	"hunter_gar_trader": {"Hunter", "Loner", "Garbage", "Butcher"},
	"baraholka_trader": {"Trader", "Loner", "Garbage"},
	"baraholka_trader_night": {"Trader", "Loner", "Garbage", "NightTrader"},
	# Jupiter
	"jup_b217_stalker_tech": {"Mechanic", "Loner", "Jupiter"},
	"jup_cont_mech_bandit": {"Mechanic", "Bandit", "Jupiter"},
	"mechanic_monolith_jup_depo": {"Mechanic", "Monolith", "Jupiter"},
	"jup_a6_stalker_medik": {"Medic", "Loner", "Jupiter"},
	"drx_sl_jup_a6_freedom_leader": {"Leader", "Freedom", "Jupiter", "Loki"},
	"jup_b6_scientist_tech": {"Mechanic", "Ecolog", "Jupiter", "Tukarev"},
	"jup_b220_trapper": {"Hunter", "Loner", "Jupiter", "Trapper"},
	"jup_b19_freedom_yar": {"TaskGiver", "Freedom", "Jupiter", "Yar"},
	"jup_b6_scientist_nuclear_physicist": {"Leader", "Ecolog", "Jupiter", "Hermann"},
	# Marsh
	"mar_base_stalker_tech": {"Mechanic", "ClearSky", "Marsh"},
	"mar_smart_terrain_base_doctor": {"Medic", "ClearSky", "Marsh"},
	"mar_smart_terrain_base_stalker_leader_marsh": {"Leader", "ClearSky", "Marsh", "Cold"},
	"mar_base_owl_stalker_trader": {"Trader", "ClearSky", "Marsh", "Spore"},
	"mar_base_stalker_barmen": {"Barman", "Trader", "ClearSky", "Marsh", "Librarian"},
	# Army Warehouses
	"mil_smart_terrain_7_7_freedom_mechanic_stalker": {"Mechanic", "Freedom", "AW"},
	"mil_freedom_medic": {"Medic", "Freedom", "AW"},
	"mil_smart_terrain_7_7_freedom_leader_stalker": {"Leader", "Freedom", "AW", "Lukash"},
	"mil_smart_terrain_7_10_freedom_trader_stalker": {"Trader", "Freedom", "AW", "Skinflint"},
	# Pripyat 2
	"pri_monolith_monolith_mechanic_stalker": {"Mechanic", "Monolith", "Pripyat2"},
	"merc_pri_a18_mech_mlr": {"Mechanic", "Mercenary", "Pripyat2"},
	"mechanic_monolith_kbo": {"Mechanic", "Monolith", "Pripyat2"},
	"pri_monolith_monolith_trader_stalker": {"Trader", "Monolith", "Pripyat2", "Rabbit"},
	"lider_monolith_haron": {"Leader", "Monolith", "Pripyat2", "Haron"},
	"monolith_eidolon": {"TaskGiver", "Monolith", "Pripyat2", "Eidolon"},
	"merc_pri_grifon_mlr": {"Leader", "Mercenary", "Pripyat2", "Griffin"},
	# Red Forest
	"red_greh_tech": {"Mechanic", "Greh", "RedForest"},
	# Truck Cemetery
	"trucks_cemetery_bandit_mechanic": {"Mechanic", "Bandit", "TruckCemetery"},
	# Yantar
	"mechanic_army_yan_mlr": {"Mechanic", "Army", "Yantar"},
	"yan_stalker_sakharov": {"Leader", "Ecolog", "Yantar", "Sakharov"},
	# Zaton
	"zat_a2_stalker_mechanic": {"Mechanic", "Loner", "Zaton"},
	"zat_stancia_mech_merc": {"Mechanic", "Mercenary", "Zaton"},
	"zat_tech_mlr": {"Mechanic", "Loner", "Zaton"},
	"zat_b22_stalker_medic": {"Medic", "Loner", "Zaton"},
	"zat_a2_stalker_barmen": {"Barman", "Trader", "Leader", "Loner", "Zaton", "Beard"},
	"zat_stancia_trader_merc": {"Trader", "Mercenary", "Zaton"},
}

warfare_factions = {
	"stalker": {"Loner"},
	"bandit": {"Bandit"},
	"csky": {"ClearSky"},
	"dolg": {"Duty"},
	"freedom": {"Freedom"},
	"killer": {"Mercenary"},
	"army": {"Army"},
	"ecolog": {"Ecolog"},
	"monolith": {"Monolith"},
	"renegade": {"Renegade"},
	"greh": {"Greh"},
	"isg": {"UNISG"},
}
warfare_npc_types = {
	"mechanic": {"Mechanic"},
	"trader": {"Trader"},
    "medic": {"Medic"},
    "barman": {"Barman"},
}

locations = { 
    "agroprom": {
        "agr_smart_terrain_1_6_army_mechanic_stalker",
        "agr_1_6_medic_army_mlr",
        "agr_smart_terrain_1_6_near_2_military_colonel_kovalski",
    },
    "bar": {
        "bar_visitors_stalker_mechanic",
        "bar_dolg_medic",
        "bar_visitors_barman_stalker_trader",
        "bar_dolg_leader",
        "bar_dolg_general_petrenko_stalker",
        "snitch",
    },
    "darkscape": {
        "dasc_tech_mlr",
    },
    "darkvalley": {
        "val_smart_terrain_7_3_bandit_mechanic_stalker",
        "bandit_main_base_medic_mlr",
        "zat_b7_bandit_boss_sultan",
        "val_smart_terrain_7_4_bandit_trader_stalker",
    },
    "deadcity": {
        "cit_killers_merc_mechanic_stalker",
        "cit_killers_merc_medic_stalker",
        "cit_killers_merc_trader_stalker",
        "cit_killers_merc_barman_mlr",
    },
    "escape": {
        "esc_smart_terrain_5_7_loner_mechanic_stalker",
        "army_south_mechan_mlr",
        "drx_sl_esc_m_trader",
        "esc_2_12_stalker_wolf",
        "esc_2_12_stalker_nimble",
        "esc_3_16_military_trader",
        "esc_2_12_stalker_fanat",
    },
    "garbage": {
        "hunter_gar_trader",
        "baraholka_trader_night",
        "baraholka_trader",
    },
    "jupiter": {
        "jup_b217_stalker_tech",
        "jup_cont_mech_bandit",
        "mechanic_monolith_jup_depo",
        "jup_a6_stalker_medik",
        "drx_sl_jup_a6_freedom_leader",
        "jup_b6_scientist_tech",
        "jup_b220_trapper",
        "jup_b19_freedom_yar",
        "jup_b6_scientist_nuclear_physicist",
    },
    "marsh": {
        "mar_base_stalker_tech",
        "mar_smart_terrain_base_doctor",
        "mar_smart_terrain_base_stalker_leader_marsh",
        "mar_base_owl_stalker_trader",
        "mar_base_stalker_barmen",
    },
    "military": {
        "mil_smart_terrain_7_7_freedom_mechanic_stalker",
        "mil_freedom_medic",
        "mil_smart_terrain_7_7_freedom_leader_stalker",
        "mil_smart_terrain_7_10_freedom_trader_stalker",
    },
    "pripyat2": {
        "pri_monolith_monolith_mechanic_stalker",
        "merc_pri_a18_mech_mlr",
        "mechanic_monolith_kbo",
        "pri_monolith_monolith_trader_stalker",
        "lider_monolith_haron",
        "monolith_eidolon",
        "merc_pri_grifon_mlr",
    },
    "red_forest": {
        "red_greh_tech",
    },
    "truck": {
        "trucks_cemetery_bandit_mechanic",
    },
    "yantar": {
        "mechanic_army_yan_mlr",
        "yan_stalker_sakharov",
    },
    "zaton": {
        "zat_a2_stalker_mechanic",
        "zat_stancia_mech_merc",
        "zat_tech_mlr",
        "zat_b22_stalker_medic",
        "zat_a2_stalker_barmen",
        "zat_stancia_trader_merc",
    },
}

icons = {
    "docs_advanced": "ui_inGame2_Sdelka",
}

quests = {
    fs(["Lukash"]): [
        "docs_advanced",
    ]
}