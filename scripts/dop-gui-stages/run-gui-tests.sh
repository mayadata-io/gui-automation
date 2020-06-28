#!/bin/bash

set -e
GROUP="$1"
GUID="$2"
URL="$3"
THREADS="$4"
REGION="$5"

#echo '#### AWS CONFIG ####'
#if [[ $GUID == *"e2e-aws"* ]]; then
#	mkdir -p ~/.aws
#	cp $AWS_CREDS ~/.aws/credentials
#fi
#echo '#### Output AWS Selenium Grid stack ####'
#output=`aws cloudformation describe-stacks --stack-name $GUID --region $REGION --query Stacks[].Outputs[].OutputValue | sed -r 's/"+//g'`
#grid=`echo $output | awk {'print $2'}`
#echo 'Selenium Grid: ' $grid

######################
##   Running test  ##
######################
python3.7 -m pip install -r requirements.txt
#Running tests with apropriate marker
#python3.7 -m pytest -m $GROUP --url $URL --environment remote --hub $grid -v --tests-per-worker $THREADS --reruns 1 --html=./results/report.html

# Test grid connection
echo '#### curl http://106.51.78.18:6030 ####'
CURL_EXT=`curl http://106.51.78.18:6030`
echo $CURL_EXT

echo '#### curl http://10.66.2.5:4444 ####'
CURL_INT=`curl http://10.66.2.5:4444`
echo $CURL_CURL_INT

python3.7 -m pytest -m $GROUP --url $URL --environment remote -v --tests-per-worker $THREADS --reruns 1 --html=./results/report.html