#!/bin/bash
source config
source repo
#TODO: Add environment variables for config path
cd $DIR/testing && git clone $REPO; echo
cat $DIR/inputs | python3 $DIR/testing/*/*.py 
rm -rf $DIR/testing/*
touch $DIR/testing/.gitkeep 
