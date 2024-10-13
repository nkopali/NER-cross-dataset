#!/bin/bash
#ENTITIES="NCBI-disease BC5CDR-disease BC5CDR-chem BC4CHEMD JNLPBA BC2GM linnaeus s800"
ENTITIES="BC5CDR-disease NCBI-disease"

MAX_LENGTH=128

for ENTITY in $ENTITIES
do
	echo "***** " $ENTITY " Preprocessing Start *****"
	DATA_DIR=../datasets/NER/$ENTITY

	# Replace tab to space
	cat $DATA_DIR/train.tsv | tr '\t' ' ' > $DATA_DIR/train.txt.tmp
	cat $DATA_DIR/dev.tsv | tr '\t' ' ' > $DATA_DIR/dev.txt.tmp
	cat $DATA_DIR/test.tsv | tr '\t' ' ' > $DATA_DIR/test.txt.tmp
	echo "Replacing Done"

	# Preprocess for BERT-based models
	python3 scripts/preprocess.py $DATA_DIR/train.txt.tmp bert-base-cased $MAX_LENGTH > $DATA_DIR/train.txt
	python3 scripts/preprocess.py $DATA_DIR/dev.txt.tmp bert-base-cased $MAX_LENGTH > $DATA_DIR/dev.txt
	python3 scripts/preprocess.py $DATA_DIR/test.txt.tmp bert-base-cased $MAX_LENGTH > $DATA_DIR/test.txt
	cat $DATA_DIR/train.txt $DATA_DIR/dev.txt $DATA_DIR/test.txt | cut -d " " -f 2 | grep -v "^$"| sort | uniq > $DATA_DIR/labels.txt
	echo "***** " $ENTITY " Preprocessing Done *****"

done
