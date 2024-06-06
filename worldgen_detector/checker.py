import json
import os

from utilSimple import JsonTool as jt
from utilSimple import FileGetter as fg

p1 = 'cache/worldgen/biome'
p2 = 'cache/worldgen/placed_feature'
p3 = 'cache/worldgen/configured_feature'
treeList = ['aspen', 'cedar', 'cypress', 'fir',
            {'blue_wisteria': "wisteria"}, {'purple_wisteria': "wisteria"},
            {'pink_wisteria': "wisteria"}, {'white_wisteria': "wisteria"},
            {'orange_maple': "maple"}, {'red_maple': "maple"}, {'yellow_maple': "maple"},
            {'larch': "larch"}, {'yellow_larch': "larch"},
            'ghaf', 'joshua', 'mahogany', 'olive',
            'palo_verde', 'redwood',
            'saxaul', 'sugi', 'willow',
            ]


def get_json(js_path):
    if os.path.exists(js_path):
        return jt.readJsonFile(js_path)
    else:
        return None


def get_config(id):
    return get_json(f"{p3}/{id.split(':')[-1]}.json")


def get_place(id):
    return get_json(f"{p2}/{id.split(':')[-1]}.json")


out = []
for i in os.listdir(p1):
    try:
        biome = jt.readJsonFile(f"{p1}/{i}")
        biome_id = "natures_spirit:" + i.split(".")[0]
        ss = {
            "select": {"name": biome_id},
            "apply": {
                "species": {
                    "random": {
                    }
                },
                "density": [1],
                "chance": 1.0,
                "forestness": 1.0
            }
        }
        any = False
        if biome.get("features") is not None:
            features = []
            for j in biome["features"]:
                features.extend(j)
            for t in treeList:
                branch_t=''
                if type(t) != str:
                    keyname = list(t.keys())[0]
                    f = keyname
                    branch_t = t[f]
                else:
                    f = t
                if f"natures_spirit:{f}_placed" in features or f"natures_spirit:{branch_t}_placed" in features:
                    any = True
                    ss["apply"]["species"]["random"][f"dtnatures_spirit:{f}"] = 1

        if any:
            out.append(ss)

    except Exception as e:

        pass
print(jt.dictToJson(out))
