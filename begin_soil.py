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



info = jt.readJsonFile('soilInfo.json')
# print(jt.readJsonFile('cache/assets/dtpvz/models/block/saplings/nut.json'))
templateName = 'sand'
templateModName = 'dtpvz'

shutil.rmtree('output')
createDir('output')
for soil in info:
    # build family
    treepackDir = join(fg.getOutputDirPath(), join('trees', modid))
    createDir(treepackDir)

    treeFamiliesPath = join(treepackDir, 'soil_properties')
    createDir(treeFamiliesPath)
    substitute_soil=info[soil].get("substitute_soil")
    soilJson = jt.readJsonFile(
        join(join(join(fg.getTemplateDirPath(), join('trees', templateModName)), 'soil_properties'), templateName + ".json"))
    soilJson["primitive_soil"] = info[soil]["origin_soil"]
    soilJson["acceptable_soils"] = info[soil]["soil_category"]
    if substitute_soil is not None:
        soilJson["substitute_soil"] = substitute_soil
    else:
        jt.saveDictAsJson(join(treeFamiliesPath, soil +".json"), soilJson)

    assetDir = join(fg.getOutputDirPath(), join('assets', modid))
    createDir(assetDir)

    if substitute_soil is None:
        blockstatesPath = join(assetDir, 'blockstates')
        createDir(blockstatesPath)
        soilJson = jt.readJsonFile(
            join(join(join(fg.getTemplateDirPath(), join('assets', templateModName)), 'blockstates'),
                 "rooty_{}.json".format(templateName)))
        soilJson["multipart"][0]["apply"]["model"] = info[soil]["origin_soil_model"]
        jt.saveDictAsJson(join(blockstatesPath,"rooty_{}.json".format(soil)), soilJson)



