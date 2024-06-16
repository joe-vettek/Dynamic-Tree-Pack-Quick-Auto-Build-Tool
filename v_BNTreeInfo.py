import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg

info = {

}

# print([i[len('betterend')+1:-len('_sapling')] for i in betterend.blocks.list() if i.endswith('sapling')])

modid = 'bloomingnature'
# too much problem
treeList = ['aspen', 'baobab', 'chestnut', 'ebony', 'fir', 'larch', 'swamp_cypress', 'swamp_oak']

is_common_map = []
# treeList.extend(['flowering_jacaranda','flowering_redbud','budding_jacaranda','budding_redbud'])

for t in treeList:
    if type(t) == str:
        branch_t = t
    else:
        keyname = list(t.keys())[0]
        branch_t = t[keyname]
        t = keyname

    info[t] = {
        "origin_leave": f"{modid}:{t}_leaves",
        "origin_leave_model": f"{modid}:block/{t}_leaves",
        "origin_leave_texture": f"{modid}:block/{t}_leaves",
        "origin_log": f"{modid}:{branch_t}_log",
        "origin_log_texture": f"{modid}:block/{branch_t}_log_side",
        "origin_log_top_texture": f"{modid}:block/{branch_t}_log_top",
        "origin_stripped_log": f"{modid}:stripped_{branch_t}_log",
        "origin_stripped_log_texture": f"{modid}:block/stripped_{branch_t}_log_side",
        "origin_stripped_log_top_texture": f"{modid}:block/stripped_{branch_t}_log_top",
        "origin_sapling": f"{modid}:{t}_sapling",
        "leaves_color": None,
        "family": branch_t,
        "is_common": branch_t not in is_common_map,
        "with_stripped": True,
        "has_root": True
    }
    is_common_map.append(branch_t)

print(jt.dictToJson(info))


jt.saveDictAsJson('treeInfo.json', info)

jt.saveDictAsJson('modInfo.json', {
    'modid': modid,
    'dtmodid': f'dt{modid}'
})
