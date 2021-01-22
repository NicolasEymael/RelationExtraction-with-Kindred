import kindred
import argparse
import os
import time
import sys

start_time = time.time()

foldCount = 10

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Use annotated sentences to build a Kindred classifer and apply to unannotated sentences')
	parser.add_argument('--fold',required=True,type=str,help='Fold to predict')
	args = parser.parse_args()

	outputPath = "Dataset/resultsFold" + args.fold
	sys.stdout = open(outputPath + "_metrics.txt", 'w+')

	print("Building file paths...")
	trainPaths = list()
	for fold_index in range(0, foldCount):
		if str(fold_index) != args.fold:
			trainPaths.append("Dataset/Fold" + str(fold_index) + "/")
	goldPath = "Dataset/Fold" + args.fold + "/"

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