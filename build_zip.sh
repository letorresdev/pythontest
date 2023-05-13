#!/bin/bash

PROJECT_NAME=backend

mkdir lambda_temp
dir=./lambda_temp

pip3 install --target=$dir -r requirements/requirements.txt

cp -r app/ $dir/app

cp lambda_entry_point.py $dir/lambda_entry_point.py


(cd $dir && zip ../$PROJECT_NAME -r .) # zip without root dir in archive

rm -r $dir
