#!/bin/bash

echo \#1 directory based backup
./dailysync2.py 
tree data/

echo \#2 clear the data/prod_backup folder 
rm -rf data/prod_backup/*
tree data/


echo \#3 file based backup 
./dailysync2.py 
./dailysync.py 
tree data/

date 