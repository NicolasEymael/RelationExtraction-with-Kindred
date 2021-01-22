import os
import shutil

foldCount = 10
sentencesPerFolder = 9193

srcFolderName = "Dataset/DBpediaData"
srcFiles = os.listdir(srcFolderName)
srcFiles.sort()

for fold_index in range(0, foldCount):
    destFolderName = "Dataset/Fold" + str(fold_index)
    shutil.rmtree(destFolderName, ignore_errors=True)
    os.makedirs(destFolderName, exist_ok=True)

    firstFile = fold_index * sentencesPerFolder * 3
    lastFile = ((fold_index + 1) * sentencesPerFolder * 3) + 3

    print(str(fold_index) + "\t start = " + str(fold_index * sentencesPerFolder) + "\t end = " + str((fold_index + 1) * sentencesPerFolder))

    if (fold_index != 0):
        firstFile = firstFile + 3
    for file_index in range(firstFile, lastFile):
        fileName = srcFiles[file_index]
        fullFileName = os.path.join(srcFolderName, fileName)

        if os.path.isfile(fullFileName):
            shutil.copy(fullFileName, destFolderName) 
    