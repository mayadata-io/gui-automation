#!/bin/bash

set -e
GUID="$1"
URL="$2"
REGION="$3"

echo '#### AWS CONFIG ####'
mkdir -p ~/.aws
cp $AWS_CREDS ~/.aws/credentials
sed 's|region = us-west-2|region = '${REGION}'|' -i ~/.aws/config

output=`aws cloudformation describe-stacks --stack-name $GUID --query Stacks[].Outputs[].OutputValue | sed -r 's/"+//g'`
grid=`echo $output | awk {'print $2'}`

cd ../..
######################
##   Running test  ##
######################
python3.7 -m pip install -r requirements.txt
#Running tests with dashboard marker
python3.7 -m pytest -m dashboard --url $URL --environment remote --hub $grid -v -n 5 --reruns 1 --html=./results/report.html