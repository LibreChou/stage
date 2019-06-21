#!/bin/bash

PREDICTION_DIR='results/'
GROUND_TRUTH_DIR='JPEGImages/'
CLASS_PATH='classes.json'
OUT_PATH='mAP.txt'
IOU_THRESH=0.5

python3 mean_average_precision.py $PREDICTION_DIR $GROUND_TRUTH_DIR $CLASS_PATH $OUT_PATH $IOU_THRESH
