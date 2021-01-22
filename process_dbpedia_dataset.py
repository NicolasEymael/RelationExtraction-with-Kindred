from itertools import islice
import re
import shutil
import os

folderName = "Dataset/DBpediaData"

shutil.rmtree(folderName, ignore_errors=True)

os.makedirs(folderName, exist_ok=True)

with open("Dataset/DBpediaRelations-PT-0.2.txt", 'r') as reader:
  n = 11
  i = 0

  while True:
    next_n_lines = list(islice(reader, n))
    if not next_n_lines:
      break

    sentence = next_n_lines[1][11:].rstrip()
    entity1 = next_n_lines[5][10:].rstrip()
    type1 = next_n_lines[6][8:].rstrip()
    entity2 = next_n_lines[7][10:].rstrip()
    type2 = next_n_lines[8][8:].rstrip()
    relation = next_n_lines[9][11:].rstrip()

    if sentence.find(entity1) != -1 and sentence.find(entity2) != -1:
      entity1StartIndex = sentence.index(entity1)
      entity1EndIndex = sentence.index(entity1) + len(entity1)
      entity2StartIndex = sentence.index(entity2)
      entity2EndIndex = sentence.index(entity2) + len(entity2)

      with open(folderName + "/" + str(i).zfill(6) + ".txt", 'w+') as sentenceWriter:
        sentenceWriter.write(sentence)

      with open(folderName + "/" + str(i).zfill(6) + ".a1", 'w+') as entityWriter:
        entityWriter.write("T1\t" + type1 + " " + str(entity1StartIndex) + " " + str(entity1EndIndex) + "\t" + entity1)
        entityWriter.write("\n")
        entityWriter.write("T2\t" + type2 + " " + str(entity2StartIndex) + " " + str(entity2EndIndex) + "\t" + entity2)

      with open(folderName + "/" + str(i).zfill(6) + ".a2", 'w+') as relationWriter:
        relationWriter.write("R1\t" + relation + " arg1:T2 arg2:T1")

      i = i + 1
    