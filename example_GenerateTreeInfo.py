import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

info = {
}

treeList =['coal', 'gold', 'redstone', 'lapis', 'copper', 'emerald', 'diamond', 'quartz', 'iron']

for t in treeList:
    info[t] = {
        "origin_leave": "minecraft:oak_leaves",
        "origin_leave_model": "block/oak_leaves",
        "origin_leave_texture": "block/oak_leaves",
        "origin_log": "ore_tree:{}_tree_log",
        "origin_log_texture": "ore_tree:blocks/{}_log",
        "origin_log_top_texture": "ore_tree:blocks/{}_log_top",
        "origin_stripped_log":"ore_tree:{}_tree_log",
        "origin_stripped_log_texture": "ore_tree:blocks/{}_log",
        "origin_stripped_log_top_texture":"ore_tree:blocks/{}_log_top",
        "origin_sapling": "ore_tree:{}_tree_sapling",
        "leaves_color": None,
        "family": t,
        "is_common": True,
        "with_stripped":False
    }
    for key in info[t]:
        if type(info[t][key])is not str:
            continue
        info[t][key] = info[t][key].format(t)



print(jt.dictToJson(info))

jt.saveDictAsJson('treeInfo.json', info)
