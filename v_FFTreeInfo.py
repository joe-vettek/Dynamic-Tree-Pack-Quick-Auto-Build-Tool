import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

info = {
}

modid='fruitfulfun'
treeList =['pomegranate']

# treeList.extend(['flowering_jacaranda','flowering_redbud','budding_jacaranda','budding_redbud'])

for t in treeList:
    info[t] = {
        "origin_leave": "{}:{}_leaves",
        "origin_leave_model": "{}:block/{}_leaves",
        "origin_leave_texture": "{}:block/{}_leaves",
        "origin_log": "{}:citrus_log",
        "origin_log_texture": "{}:block/citrus_log",
        "origin_log_top_texture": "{}:block/citrus_log_top",
        "origin_stripped_log":"{}:stripped_citrus_log",
        "origin_stripped_log_texture": "{}:block/stripped_citrus_log",
        "origin_stripped_log_top_texture":"{}:block/stripped_citrus_log_top",
        "origin_sapling": "{}:{}_sapling",
        "leaves_color": None,
        "family": t,
        "is_common": True,
        "with_stripped":True,
        "has_root":False
    }
    for key in info[t]:
        if type(info[t][key])is not str:
            continue
        info[t][key] = info[t][key].format( modid,t)



print(jt.dictToJson(info))

jt.saveDictAsJson('treeInfo.json', info)
