import inspect

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg




info = {
}

base_path=r"temp\blocks"
grass=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"grass_blocks.json"))["values"]if not d.startswith('minecraft')]

dirts=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"dirt.json"))["values"]if not d.startswith('minecraft')]
dirts=[ d for d in dirts if not d in grass]

gravels=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"gravel.json"))["values"]if not d.startswith('minecraft')]
sands=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"sand.json"))["values"]if not d.startswith('minecraft')]
silts=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"silt.json"))["values"]if not d.startswith('minecraft')]
podzol=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"podzol.json"))["values"]if not d.startswith('minecraft')]
farmland=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"farmland.json"))["values"] if not d.startswith('minecraft')]
myceliums=[ d[8:]  for d in jt.readJsonFile(fg.join(base_path,"farmland.json"))["values"] if not d.startswith('minecraft')]

soiltypeList =[grass, dirts, gravels, sands, silts, podzol, farmland, myceliums]

def get_soil_category(soils):
    if soils==grass or soils==dirts or soils==farmland or soils==podzol:
        return [ "dirt_like" ]
    if soils==gravels :
        return [ "gravel_like" ]
    if soils==sands :
        return [ "sand_like" ]
    if soils==myceliums :
        return [ "dirt_like", "fungus_like" ]
    return []

def get_substitute_soil(soils):
    if soils==farmland :
        return "dirt"
    return None

for s_list in soiltypeList:
    for s in s_list:
        info[s] = {
            "origin_soil": "rankine:{}",
            "origin_soil_model": "rankine:block/{}",
            "soil_category": get_soil_category(s_list),
            "substitute_soil": get_substitute_soil(s_list)
        }

        for key in info[s]:
            if type(info[s][key])is not str:
                continue
            info[s][key] = info[s][key].format(s)



# print(jt.dictToJson(info))

jt.saveDictAsJson('soilInfo.json', info)
