import inspect
import os.path

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

modid = "natures_spirit"

info = {
}

base_path = r"temp\blocks"

soiltypeList = {
    "dirt_like": {"grass_blocks": [], "dirt": [], "silt": [], "podzol": [], "farmland": []},
    "gravel_like": {"gravels": []},
    "sand_like": {"sand": []},
    "fungus_like": {"myceliums": []}
}

for s in soiltypeList:
    for tag in soiltypeList[s]:
        path = f"{base_path}/{tag}.json"
        if os.path.exists(path):
            for d in jt.readJsonFile(path)["values"]:
                if d.startswith(modid):
                    soiltypeList[s][tag].append(d)


def get_soil_category(soils):
    RESULT = []
    for ty in soiltypeList:
        for tag in soiltypeList[ty]:
            if soils in soiltypeList[ty][tag]:
                RESULT.append(ty)
    return RESULT


def get_substitute_soil(soils):
    for ty in soiltypeList:
        for tag in soiltypeList[ty]:
            if tag == "farmland" and soils in soiltypeList[ty][tag]:
                return "dirt"
    return None


for like in soiltypeList:
    for s in soiltypeList[like]:
        s_list = soiltypeList[like][s]
        for block in soiltypeList[like][s]:
            info[block.split(":")[-1]] = {
                "origin_soil": "{}:{}",
                "origin_soil_model": "{}:block/{}",
                "soil_category": get_soil_category(block)
            }
            if get_substitute_soil(block) is not None:
                info[block]["substitute_soil"]=get_substitute_soil(block)

for s in info.keys():
    for key in info[s].keys():
        if type(info[s][key]) is not str:
            continue
        info[s][key] = info[s][key].format(modid, s)

# print(jt.dictToJson(info))

jt.saveDictAsJson('soilInfo.json', info)
