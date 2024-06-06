import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

info = {
}

modid = 'natures_spirit'
treeList = ['aspen', 'blue_wisteria', 'cedar', 'cypress', 'fir',
            'ghaf', 'joshua', 'larch', 'mahogany', 'olive',
            'orange_maple', 'palo_verde', 'pink_wisteria',
            'purple_wisteria', 'red_maple', 'redwood',
            'saxaul', 'sugi', 'white_wisteria', 'willow',
            'yellow_larch', 'yellow_maple']

is_common_map = []
# treeList.extend(['flowering_jacaranda','flowering_redbud','budding_jacaranda','budding_redbud'])

for t in treeList:
    branch_t = t.split("_")[-1]

    info[t] = {
        "origin_leave": f"{modid}:{t}_leaves",
        "origin_leave_model": f"{modid}:block/{t}_leaves",
        "origin_leave_texture": f"{modid}:block/{t}_leaves",
        "origin_log": f"{modid}:{branch_t}_log",
        "origin_log_texture": f"{modid}:block/{branch_t}_log",
        "origin_log_top_texture": f"{modid}:block/{branch_t}_log_top",
        "origin_stripped_log": f"{modid}:stripped_{branch_t}_log",
        "origin_stripped_log_texture": f"{modid}:block/stripped_{branch_t}_log",
        "origin_stripped_log_top_texture": f"{modid}:block/stripped_{branch_t}_log_top",
        "origin_sapling": f"{modid}:{t}_sapling",
        "leaves_color": None,
        "family": branch_t,
        "is_common": branch_t not in is_common_map,
        "with_stripped": True,
        "has_root": False
    }
    is_common_map.append(branch_t)

print(jt.dictToJson(info))

jt.saveDictAsJson('treeInfo.json', info)
