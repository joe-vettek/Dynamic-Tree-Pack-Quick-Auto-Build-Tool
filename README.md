# Dynamic-Tree-Pack-Quick-Auto-Build-Tool
 Tried to use a python automated construction program to quickly build basic JSON, using the least initial information to help people quickly get a usable data package effect from scratch. 

Note that this version is only applicable to the latest Dynamic Tree version of MC1.16.5 and MC1.18.2, and the applicability of higher versions needs to be verified.

Click [here](https://github.com/DynamicTreesTeam/DynamicTrees) to visit DynamicTrees.

### manual

1. Run `example_ModInfo.py` to generate `treeInfo.json`.
2. Modify `modid` in `begin.py` to the name of your mod.
3. Run `begin.py` and then result will in the `ouput` folder.

### about feature

If  looking for added features, in 1.20.1, or search in their java source code BiomeModifications.addFeature (for FabricMC), data/forge/biome_modifier/xx.json (for Forge)

in forge for 1.18.2 ,check the code use BiomeLoadingEvent

Generally speaking, the features used are listed in the biome json, through place->config->(config/place (config here needs {} plus placement modifier, which is actually equivalent to place)).