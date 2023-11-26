import utilSimple.JsonTool as jt


info = {}

treeList = [ "maplegreen", "mapleorange", "maplered", "mapleyellow", "sakura", "ume"]

colorMap={
    "redlove": "116777215"
}

for t in treeList:
    info[t] = {
        "origin_leave": "sakura:{}leaves{}",
        "origin_leave_model": "sakura:block/{}leaves{}",
        "origin_leave_texture": "sakura:block/{}leaves{}",
        "origin_log": "sakura:{}_log{}",
        "origin_log_texture": "sakura:block/{}_log",
        "origin_log_top_texture": "sakura:block/{}_log_top",
        "origin_stripped_log": "sakura:stripped_{}_log",
        "origin_stripped_log_texture": "sakura:block/stripped_{}_log",
        "origin_stripped_log_top_texture": "sakura:block/stripped_{}_log_top",
        "origin_sapling": "sakura:{}_sapling{}",
        "leaves_color": colorMap.get(t) if colorMap.get(t) is not None else None,
        "family": ("maple" if "maple" in t else t),
        "is_common": True if not "maple" in t else (True if "green" in t else False)
    }
    for key in info[t]:
        if type(info[t][key])is not str:
            continue
        isMaple = "maple" in t
        mapleType= "" if not isMaple else "_"+t.replace("maple","")
        woodName = "maple" if isMaple else t
        reg1=t if not isMaple else "maple"
        info[t][key] = info[t][key].format( reg1 if not "log" in key else woodName,mapleType)



print(jt.dictToJson(info))

jt.saveDictAsJson('treeInfo.json', info)
