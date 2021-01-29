import kindred
import argparse
import os
import time
import sys

start_time = time.time()

foldCount = 10

if __name__ == '__main__':

	datasetPath = "Dataset/DBpediaData"

	mainCorpus = kindred.load('standoff', datasetPath)

	i = 0

	for trainCorpus,goldCorpus in mainCorpus.nfold_split(foldCount):

		classifier = kindred.RelationClassifier(model='pt')
		classifier.train(trainCorpus)

		testCorpus = goldCorpus.clone()
		testCorpus.removeRelations()

		classifier.predict(testCorpus)

		outputDir = "Results/"
		if not os.path.isdir(outputDir):
			os.makedirs(outputDir)
		outputFile = outputDir + "metrics" + str(i) + ".txt"
		sys.stdout = open(outputFile, "w+")

		kindred.evaluate(goldCorpus, testCorpus, metric='all', display=True)

		i = i + 1

		print("--- %s seconds ---" % (time.time() - start_time))