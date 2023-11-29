import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

info = {
}

treeList =['eastern_hemlock', 'black_walnut', 'cork_oak', 'juniper', 'sharinga', 'western_hemlock', 'coconut_palm', 'magnolia', 'honey_locust', 'red_birch', 'maple', 'weeping_willow', 'erythrina', 'pinyon_pine', 'yellow_birch', 'cedar', 'balsam_fir', 'black_birch', 'cinnamon']


for t in treeList:
    info[t] = {
        "origin_leave": "rankine:{}_leaves",
        "origin_leave_model": "rankine:block/{}_leavesage0",
        "origin_leave_texture": "rankine:block/{}_leaves",
        "origin_log": "rankine:{}_log",
        "origin_log_texture": "rankine:block/{}_log",
        "origin_log_top_texture": "rankine:block/{}_log_top",
        "origin_stripped_log":"rankine:stripped_{}_log",
        "origin_stripped_log_texture": "rankine:block/stripped_{}_log",
        "origin_stripped_log_top_texture":"rankine:block/stripped_{}_log_top",
        "origin_sapling": "rankine:{}_sapling",
        "leaves_color": None,
        "family": t,
        "is_common": True,
        "with_stripped":True,
        "has_root":False if t not in "coconut_palm" else True
    }
    for key in info[t]:
        if type(info[t][key])is not str:
            continue
        info[t][key] = info[t][key].format( t)



print(jt.dictToJson(info))

jt.saveDictAsJson('treeInfo.json', info)
