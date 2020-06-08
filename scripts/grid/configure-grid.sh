#!/bin/bash

set -e
GUID="$1"
REGION="$2"

if [ $REGION = "eu-north-1" ];then
	echo '#### AWS CONFIG ####'
	mkdir -p ~/.aws
	cp $AWS_CREDS ~/.aws/credentials
	sed 's|region = us-west-2|region = '${REGION}'|' -i ~/.aws/config
fi
# tests_count=`find . -type f -name '*_test.py' -exec grep -e 'def test_' '{}' \; | wc -l`
tests_count=30
echo "Number of GUI test scripts: $tests_count"

cat selenium-grid-config.yml

aws cloudformation create-stack --stack-name ${GUID} --template-body file://selenium-grid-config.yml --parameters ParameterKey=NumberOfChromeNodes,ParameterValue=$tests_count ParameterKey=ClusterName,ParameterValue=${GUID} ParameterKey=LogName,ParameterValue=${GUID}
