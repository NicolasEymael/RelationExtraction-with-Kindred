import os
import shutil

foldCount = 10

for fold_index in range(0, foldCount):
    currentSrcFolder = "Dataset/Fold" + str(fold_index)

    srcFiles = os.listdir(currentSrcFolder)
    srcFiles.sort()
    
    currentDestFolder = currentSrcFolder + "_without_relations"

    shutil.rmtree(currentDestFolder, ignore_errors=True)
    os.makedirs(currentDestFolder, exist_ok=True)

    print(str(fold_index))

    for index, fileName in enumerate(srcFiles):
        if (fileName.endswith(".a2") == False):
            fullFileName = os.path.join(currentSrcFolder, fileName)

            if os.path.isfile(fullFileName):
                shutil.copy(fullFileName, currentDestFolder) 
    