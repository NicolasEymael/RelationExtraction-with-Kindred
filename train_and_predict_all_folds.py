import kindred
import argparse
import os
import time
import sys

start_time = time.time()

foldCount = 10

if __name__ == '__main__':

	for currentFoldIndexToPredict in range(0, foldCount):
		
		outputPath = "Dataset/resultsFold" + str(currentFoldIndexToPredict)
		sys.stdout = open(outputPath + "_metrics.txt", 'w+')

		print("Building file paths...")
		trainPaths = list()
		for fold_index in range(0, foldCount):
			if fold_index != currentFoldIndexToPredict:
				trainPaths.append("Dataset/Fold" + str(fold_index) + "/")
		goldPath = "Dataset/Fold" + str(currentFoldIndexToPredict) + "/"

		print("Loading corpora...")
		trainCorpora = list()
		for path in trainPaths:
			trainCorpora.append(kindred.load('standoff',path))
		goldCorpus = kindred.load('standoff', goldPath)
		predictionCorpus = goldCorpus.clone()
		predictionCorpus.removeRelations()

		print("Building classifier...")
		classifier = kindred.RelationClassifier(model='pt')
		for corpus in trainCorpora:
			classifier.train(corpus)

		print("Applying classifier...")
		classifier.predict(predictionCorpus)

		print("Calculating metrics...")
		metrics = kindred.evaluate(goldCorpus, predictionCorpus, metric='all', display=True)

		if not os.path.isdir(outputPath):
			os.makedirs(outputPath)

		print("Saving results to directory...")
		kindred.save(predictionCorpus,'standoff',outputPath)

		print("--- %s seconds ---" % (time.time() - start_time))