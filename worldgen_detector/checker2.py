import json
import os
import sys
import traceback

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
            'saxaul', 'sugi', 'willow', 'coconut'
            ]

txt_info = []

t_mod_id = 'dtnatures_spirit'
treeList2 = ["acacia", "birch", "cherry", "dark_oak", "jungle", "mangrove", "oak", "spruce"]


def get_tree_by_leave(fes, leave):
    for t in treeList:
        branch_t = ''
        if type(t) != str:
            keyname = list(t.keys())[0]
            f = keyname
            branch_t = t[f]
        else:
            f = t
        if leave == f"natures_spirit:{f}_leaves":
            return f"{t_mod_id}:{f}"
    if leave == "natures_spirit:wisteria_leaves":
        return [f"{t_mod_id}:{z}" for z in ['blue_wisteria', 'purple_wisteria', 'pink_wisteria', 'white_wisteria']]

    for t in treeList2:
        if leave == f"minecraft:{t}_leaves":
            return f"dynamictrees:{t}"

    global txt_info
    txt_info.append(f"Not found leave in {fes},{leave}\n")
    return None


def get_json(js_path):
    if os.path.exists(js_path):
        return jt.readJsonFile(js_path)
    else:
        return None


def has_key(obj, key):
    return obj is not None and obj.get(key) is not None


def check_value(obj, key, value):
    return obj is not None and obj.get(key) == value


def get_config(id):
    try:
        return get_json(f"{p3}/{id.split(':')[-1]}.json")
    except:
        return {}


def get_place(id):
    try:
        return get_json(f"{p2}/{id.split(':')[-1]}.json")
    except:
        return {}


def find_tree_in_place(id):
    configure_feature = get_place(id)
    if has_key(configure_feature, "feature"):
        return find_tree_in_config(configure_feature["feature"])
    else:
        return []


# to_get_config
def check_place_or_config(input_obj):
    if type(input_obj) == str:
        place_feature = get_place(input_obj)
        if place_feature:
            return get_place(input_obj)["feature"], 1
    else:
        if input_obj.get("feature") is not None and type(input_obj.get("feature")) == str:
            return input_obj["feature"], 2
    return None


def find_tree_in_config(id):
    configure_feature = get_config(id)
    result = []
    if has_key(configure_feature, "type") and \
            (configure_feature["type"] == "minecraft:random_selector"
             or configure_feature["type"] == "minecraft:simple_random_selector"):
        fes112 = []
        get_item = None
        if configure_feature["type"] == "minecraft:random_selector":
            get_item = check_place_or_config(configure_feature["config"]["default"])
        if get_item:
            fes112.append(get_item[0])
        for i in configure_feature["config"]["features"]:
            if configure_feature["type"] == "minecraft:random_selector":
                get_item = check_place_or_config(i["feature"])
                if get_item:
                    fes112.append(get_item[0])
            else:
                get_item = check_place_or_config(i)
                if get_item:
                    fes112.append(get_item[0])
        # now we get a config feature list
        fes112 = list(set(fes112))

        for fes in fes112:
            js_fes = get_config(fes)
            if check_value(js_fes, "type", "minecraft:tree"):
                # print()
                tree = get_tree_by_leave(fes, js_fes["config"]["foliage_provider"]["state"]["Name"])
                if tree:
                    if type(tree) == str:
                        result.append(tree)
                    else:
                        result.extend(tree)
            else:
                # print(fes,jt.dictToJsonNoOpen(js_fes))
                global txt_info
                txt_info += f"{fes},{jt.dictToJsonNoOpen(js_fes)}\n"

    return result


out = []
count = 0
for i in os.listdir(p1):
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
        for fea in features:
            res = find_tree_in_place(fea)
            if len(res) > 0:
                any = True
                for r in res:
                    ss["apply"]["species"]["random"][r] = 1
    if any:
        out.append(ss)
    if len(txt_info) > count:
        txt_info.insert(count, f"# {biome_id}\n")
        txt_info.append("\n")
    count = len(txt_info)
with open("cache/warnings.log", "w") as f:
    f.write(''.join(txt_info))

print(jt.dictToJsonNoOpen(out))
