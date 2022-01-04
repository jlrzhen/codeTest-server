#!/bin/bash
source config
source repo
cd $DIR/testing && git clone $REPO; echo
cat $DIR/inputs | python3 $DIR/testing/*/*.py 
rm -rf $DIR/testing/*
