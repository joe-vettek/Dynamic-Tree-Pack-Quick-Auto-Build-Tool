treeList = ["pomegranate", "cherry", "tangerine", "lime", "citron", "pomelo", "orange", "lemon", "grapefruit",
            "redlove"]
treeListyy = ["石榴", "樱桃", "橘子", "酸橙", "香橼", "柚子", "甜橙", "柠檬", "西柚", "红心果"]
for i, t in enumerate(treeList):
    #     code='''public static final LazyGet<Block> {0}_LEAVES = LazyGet.of(() -> RegisterFinderUtil.getBlock(DTFruitfulFun.rl("{1}_leaves")));
    # public static final LazyGet<Block> {0} = LazyGet.of(() -> RegisterFinderUtil.getBlock(DTFruitfulFun.rl("{1}")));
    # public static final LazyGet<Block> {0}_SAPLING = LazyGet.of(() -> RegisterFinderUtil.getBlock(DTFruitfulFun.rl("{1}_sapling")));
    # public static final LazyGet<Block> {0}_BRANCH = LazyGet.of(() -> RegisterFinderUtil.getBlock(DTFruitfulFun.rl("{1}_branch")));
    # public static final LazyGet<Item> {0}_SEED = LazyGet.of(() -> RegisterFinderUtil.getItem(DTFruitfulFun.rl("{1}_seed")));
    # '''
    cc = ''' add(ModConstants.{0}_SAPLING.get(), "{1} Sapling");
add(ModConstants.{0}_BRANCH.get(), "{1} Tree");
add(ModConstants.{0}_SEED.get(), "{1} Seed");
addSpecie("{2}","{1} Fruit");
'''
    cc = ''' add(ModConstants.{0}_SAPLING.get(), "{1}树苗");
add(ModConstants.{0}_BRANCH.get(), "{1}树");
add(ModConstants.{0}_SEED.get(), "{1}种子");
addSpecie("{2}","{1}树");
    '''
    allu = ''.join([i.upper() for i in t])
    allc = t[0].upper() + t[1:]
    print(cc.format(allu, treeListyy[i], t))
