import json
import os
import sys
import traceback

from utilSimple import JsonTool as jt
from utilSimple import FileGetter as fg

modid = 'bloomingnature'
p_base = f'data/{modid}/forge/biome_modifier'
p1 = f'data/{modid}/worldgen/biome'
p2 = f'data/{modid}/worldgen/placed_feature'
p3 = f'data/{modid}/worldgen/configured_feature'
treeList = ['aspen', 'baobab', 'chestnut', 'ebony', 'fir', {'larch': "larch"}, 'swamp_cypress', 'swamp_oak', 'fan_palm']

txt_info = []

t_mod_id = 'dtbloomingnature'

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
        if leave == f"{modid}:{f}_leaves":
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
        return find_tree_in_config(configure_feature["feature"], id)
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


def deal_with_output_error(id, feature):
    global txt_info
    if type(feature) == str:
        txt_info += f"Not in {id} found {feature} \n"
    else:
        if has_key(feature, "feature") and type(feature["feature"]) == str:
            txt_info += f"Not in {id} found {jt.dictToJsonNoOpen(feature)}\n"


def find_tree_in_config(id, id2):
    configure_feature = get_config(id)
    result = []
    # print(id,jt.dictToJsonNoOpen(configure_feature))
    global txt_info
    if has_key(configure_feature, "type") and \
            (configure_feature["type"] == "minecraft:random_selector"
             or configure_feature["type"] == "minecraft:simple_random_selector"):
        fes112 = []
        get_item = None
        if configure_feature["type"] == "minecraft:random_selector":
            get_item = check_place_or_config(configure_feature["config"]["default"])
        if get_item:
            fes112.append(get_item[0])
        elif has_key(configure_feature["config"], "default"):
            deal_with_output_error(id, configure_feature["config"]["default"])
        for i in configure_feature["config"]["features"]:
            if configure_feature["type"] == "minecraft:random_selector":
                get_item = check_place_or_config(i["feature"])
                if get_item:
                    fes112.append(get_item[0])
                else:
                    deal_with_output_error(id, i)
            else:
                get_item = check_place_or_config(i)
                if get_item:
                    fes112.append(get_item[0])
                else:
                    deal_with_output_error(id, i)
        # now we get a config feature list
        fes112 = list(set(fes112))

        for fes in fes112:
            js_fes = get_config(fes)
            if check_value(js_fes, "type", "minecraft:tree"):
                tree=None
                if has_key(js_fes["config"]["foliage_provider"],"state"):
                    tree = get_tree_by_leave(fes, js_fes["config"]["foliage_provider"]["state"]["Name"])
                else:
                    txt_info += f"{fes},{jt.dictToJsonNoOpen(js_fes)}\n"
                if tree:
                    if type(tree) == str:
                        result.append(tree)
                    else:
                        result.extend(tree)
            else:
                # print(fes,jt.dictToJsonNoOpen(js_fes))
                txt_info += f"{fes},{jt.dictToJsonNoOpen(js_fes)}\n"

        # txt_info += f"{id2} {jt.dictToJsonNoOpen(configure_feature['config'])}\n"
    return result


out = []
count = 0
if os.path.exists(p1):
    for i in os.listdir(p1):
        # print(i)
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
        # if any:
        if True:
            out.append(ss)
        if len(txt_info) > count:
            txt_info.insert(count, f"# {biome_id}\n")
            txt_info.append("\n")
        count = len(txt_info)

if os.path.exists(p_base):
    for i in os.listdir(p_base):
        # print(i)
        biome = jt.readJsonFile(f"{p_base}/{i}")
        if not check_value(biome,'type','forge:add_features'):
            continue

        biome_id = biome["biomes"]
        ss = {
            "select": {"name": biome_id},
            "apply": {
                "species": {
                    "method": "splice_before",
                    "random": {
                        "...": 10
                    }
                }
            }
        }
        any = False
        if biome.get("features") is not None:
            features = biome.get("features")
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
