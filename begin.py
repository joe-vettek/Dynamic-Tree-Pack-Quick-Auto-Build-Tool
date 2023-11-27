import os.path
import shutil

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
from utilSimple.FileGetter import join, createDir


modid = 'dtrankine'


def addToTag(templatePath, outputPath, id):
    if not os.path.exists(outputPath):
        fg.mycopyfile(templatePath, outputPath)
        tempJson = jt.readJsonFile(outputPath)
        tempJson["values"] = []
    else:
        tempJson = jt.readJsonFile(outputPath)
    if not id in tempJson["values"]:
        tempJson["values"].append(id)
        jt.saveDictAsJson(outputPath, tempJson)



info = jt.readJsonFile('treeInfo.json')
# print(jt.readJsonFile('cache/assets/dtpvz/models/block/saplings/nut.json'))
templateName = 'nut'
templateModName = 'dtpvz'

shutil.rmtree('output')
createDir('output')
for tree in info:
    # build family
    treepackDir = join(fg.getOutputDirPath(), join('trees', modid))
    createDir(treepackDir)

    treeFamiliesPath = join(treepackDir, 'families')
    createDir(treeFamiliesPath)
    is_common=info[tree].get("is_common") is None or info[tree]["is_common"]
    has_family=info[tree].get("family") is not None
    if is_common:
        treeFamilies = jt.readJsonFile(
            join(join(join(fg.getCacheDirPath(), join('trees', templateModName)), 'families'), templateName + ".json"))
        treeFamilies["common_leaves"] = "{}:{}".format(modid, tree )
        treeFamilies["common_species"] = "{}:{}".format(modid, tree)
        treeFamilies["primitive_log"] = info[tree]["origin_log"]
        if info[tree]["with_stripped"]:
            treeFamilies["primitive_stripped_log"] = info[tree]["origin_stripped_log"]
        else:
            treeFamilies["generate_stripped_branch"] = False
        jt.saveDictAsJson(join(treeFamiliesPath, tree if not has_family else info[tree]["family"] + ".json"), treeFamilies)

    jo_codePath = join(treepackDir, 'jo_codes')
    createDir(jo_codePath)
    jo_codes = fg.getAllTextInFile(
        join(join(join(fg.getCacheDirPath(), join('trees', templateModName)), 'jo_codes'), templateName + ".txt"))
    fg.saveText(join(jo_codePath, tree + ".txt"), jo_codes)

    treeleaves_propertiesPath = join(treepackDir, 'leaves_properties')
    createDir(treeleaves_propertiesPath)
    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('trees', templateModName)), 'leaves_properties'),
             templateName + ".json"))
    # treeFamilies["type"] = "{}:{}".format(modid, tree)
    treeFamilies["primitive_leaves"] = info[tree]["origin_leave"]
    if info[tree].get("leaves_color") is not None:
        treeFamilies["color"] = info[tree]["leaves_color"]
    # if  "@" in treeFamilies["color"] :
    #     treeFamilies.pop("color")
    jt.saveDictAsJson(join(treeleaves_propertiesPath, tree + ".json"), treeFamilies)

    treespeciesPath = join(treepackDir, 'species')
    createDir(treespeciesPath)
    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('trees', templateModName)), 'species'), templateName + ".json"))
    treeFamilies["family"] = "{}:{}".format(modid, tree) if info[tree]["family"] is None else modid+":"+info[tree]["family"]
    treeFamilies["leaves_properties"] = "{}:{}".format(modid, tree)
    treeFamilies["primitive_sapling"] = info[tree]["origin_sapling"]
    treeFamilies["always_show_on_waila"] =not is_common
    jt.saveDictAsJson(join(treespeciesPath, tree + ".json"), treeFamilies)

    treeWorldGenPath = join(treepackDir, 'world_gen')
    createDir(treeWorldGenPath)

    # deal asset
    assetDir = join(fg.getOutputDirPath(), join('assets', modid))
    createDir(assetDir)

    blockstatesPath = join(assetDir, 'blockstates')
    createDir(blockstatesPath)
    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'blockstates'),
             templateName + "_branch.json"))
    treeFamilies["variants"][""]["model"] = "{}:block/{}_branch".format(modid, tree if not has_family else info[tree]["family"])
    jt.saveDictAsJson(join(blockstatesPath,tree if not has_family else info[tree]["family"]   + "_branch.json"), treeFamilies)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'blockstates'),
             templateName + "_leaves.json"))
    treeFamilies["variants"][""]["model"] = info[tree]["origin_leave_model"]
    jt.saveDictAsJson(join(blockstatesPath, tree + "_leaves.json"), treeFamilies)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'blockstates'),
             templateName + "_sapling.json"))
    treeFamilies["variants"][""]["model"] = "{}:block/saplings/{}".format(modid, tree)
    jt.saveDictAsJson(join(blockstatesPath, tree + "_sapling.json"), treeFamilies)

    if info[tree]["with_stripped"]:
        treeFamilies = jt.readJsonFile(
            join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'blockstates'),
                 "stripped_{}_branch.json".format(templateName)))
        treeFamilies["variants"][""]["model"] = "{}:block/stripped_{}_branch".format(modid, tree if not has_family else info[tree]["family"])
        jt.saveDictAsJson(join(blockstatesPath, "stripped_{}_branch.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    langPath = join(assetDir, 'lang')
    createDir(langPath)

    modelsPath = join(assetDir, 'models')

    blockModelPath = join(modelsPath, "block")
    saplingModelPath = join(blockModelPath, "saplings")
    itemModelPath = join(modelsPath, "item")
    createDir(saplingModelPath)
    createDir(itemModelPath)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'models/block/saplings'),
             "{}.json".format(templateName)))
    treeFamilies["textures"]["particle"] = info[tree]["origin_leave_texture"]
    treeFamilies["textures"]["log"] = info[tree]["origin_log_texture"]
    treeFamilies["textures"]["leaves"] = info[tree]["origin_leave_texture"]
    jt.saveDictAsJson(join(saplingModelPath, "{}.json".format(tree)), treeFamilies)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'models/block'),
             "{}_branch.json".format(templateName)))
    treeFamilies["textures"]["bark"] = info[tree]["origin_log_texture"]
    treeFamilies["textures"]["rings"] = info[tree]["origin_log_top_texture"]
    jt.saveDictAsJson(join(blockModelPath, "{}_branch.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    if info[tree]["with_stripped"]:
        treeFamilies = jt.readJsonFile(
            join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'models/block'),
                 "stripped_{}_branch.json".format(templateName)))
        treeFamilies["textures"]["bark"] = info[tree]["origin_stripped_log_texture"]
        treeFamilies["textures"]["rings"] = info[tree]["origin_stripped_log_top_texture"]
        jt.saveDictAsJson(join(blockModelPath, "stripped_{}_branch.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'models/item'),
             "{}_branch.json".format(templateName)))
    treeFamilies["textures"]["bark"] = info[tree]["origin_log_texture"]
    treeFamilies["textures"]["rings"] = info[tree]["origin_log_top_texture"]
    jt.saveDictAsJson(join(itemModelPath, "{}_branch.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    treeFamilies = jt.readJsonFile(
        join(join(join(fg.getCacheDirPath(), join('assets', templateModName)), 'models/item'),
             "{}_seed.json".format(templateName)))
    treeFamilies["textures"]["layer0"] = "{}:item/{}_seed".format(modid, tree)
    jt.saveDictAsJson(join(itemModelPath, "{}_seed.json".format(tree)), treeFamilies)

    shaderPath = join(assetDir, 'shaders')
    createDir(shaderPath)

    itemTexturesPath = join(assetDir, 'textures/item')
    createDir(itemTexturesPath)

    # loot
    dataDir = join(fg.getOutputDirPath(), join('data', modid))
    createDir(dataDir)

    lootBlockPath = join(dataDir, 'loot_tables/blocks')
    createDir(lootBlockPath)
    treeFamilies = fg.getAllTextInFile(
        join(join(join(fg.getCacheDirPath(), join('data', templateModName)), 'loot_tables/blocks'),
             "{}_leaves.json".format(templateName)))
    treeFamilies = treeFamilies.replace("pvz:{}_leaves".format(templateName), info[tree]["origin_leave"])
    fg.saveText(join(lootBlockPath, "{}_leaves.json".format(tree)), treeFamilies)

    lootTreeBranchesPath = join(dataDir, 'loot_tables/trees/branches')
    createDir(lootTreeBranchesPath)
    treeFamilies = fg.getAllTextInFile(
        join(join(join(fg.getCacheDirPath(), join('data', templateModName)), 'loot_tables/trees/branches'),
             "{}.json".format(templateName)))
    treeFamilies = treeFamilies.replace("minecraft:oak_log", info[tree]["origin_log"])
    fg.saveText(join(lootTreeBranchesPath, "{}.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    if info[tree]["with_stripped"]:
        treeFamilies = fg.getAllTextInFile(
            join(join(join(fg.getCacheDirPath(), join('data', templateModName)), 'loot_tables/trees/branches'),
                 "stripped_{}.json".format(templateName)))
        treeFamilies = treeFamilies.replace("minecraft:stripped_oak_log", info[tree]["origin_stripped_log"])
        fg.saveText(join(lootTreeBranchesPath, "stripped_{}.json".format(tree if not has_family else info[tree]["family"])), treeFamilies)

    lootTreeLeavesPath = join(dataDir, 'loot_tables/trees/leaves')
    createDir(lootTreeLeavesPath)
    treeFamilies = fg.getAllTextInFile(
        join(join(join(fg.getCacheDirPath(), join('data', templateModName)), 'loot_tables/trees/leaves'),
             "{}.json".format(templateName)))
    fg.saveText(join(lootTreeLeavesPath, "{}.json".format(tree)), treeFamilies)

    lootTreeVoluntaryPath = join(dataDir, 'loot_tables/trees/voluntary')
    createDir(lootTreeVoluntaryPath)
    treeFamilies = fg.getAllTextInFile(
        join(join(join(fg.getCacheDirPath(), join('data', templateModName)), 'loot_tables/trees/voluntary'),
             "{}.json".format(templateName)))
    treeFamilies = treeFamilies.replace("{}:{}_seed".format(templateModName, templateName),
                                        "{}:{}_seed".format(modid, tree))
    fg.saveText(join(lootTreeVoluntaryPath, "{}.json".format(tree)), treeFamilies)

    dataDTDir = join(fg.getOutputDirPath(), join('data', 'dynamictrees'))
    createDir(dataDTDir)

    tagBlockPath = join(dataDTDir, 'tags/blocks')
    createDir(tagBlockPath)

    tagItemPath = join(dataDTDir, 'tags/items')
    createDir(tagItemPath)

    addToTag(join(join(fg.getCacheDirPath(), join('data', "dynamictrees")), 'tags/blocks/branches_that_burn.json')
             , join(tagBlockPath, "branches_that_burn.json"), "{}:{}_branch".format(modid, tree if not has_family else info[tree]["family"]))

    addToTag(join(join(fg.getCacheDirPath(), join('data', "dynamictrees")), 'tags/blocks/leaves.json')
             , join(tagBlockPath, "leaves.json"), "{}:{}_leaves".format(modid, tree))

    addToTag(join(join(fg.getCacheDirPath(), join('data', "dynamictrees")), 'tags/blocks/saplings.json')
             , join(tagBlockPath, "saplings.json"), "{}:{}_sapling".format(modid, tree))

    if info[tree]["with_stripped"]:
        addToTag(
            join(join(fg.getCacheDirPath(), join('data', "dynamictrees")), 'tags/blocks/stripped_branches_that_burn.json')
            , join(tagBlockPath, "stripped_branches_that_burn.json"), "{}:stripped_{}_branch".format(modid, tree if not has_family else info[tree]["family"]))

    addToTag(join(join(fg.getCacheDirPath(), join('data', "dynamictrees")), 'tags/items/seeds.json')
             , join(tagItemPath, "seeds.json"), "{}:{}_seed".format(modid, tree))
