#!/bin/bash

set -e
GUID="$1"

echo '#### AWS CONFIG ####'
mkdir -p ~/.aws
cp $AWS_CREDS ~/.aws/credentials
sed 's|region = us-west-2|region = eu-north-1|' -i ~/.aws/config

tests_count=30
echo "Number of GUI test scripts: $tests_count"

git clone https://$username:$password@github.com/mayadata-io/oep-e2e-aws.git
cd oep-e2e-aws/stages/16-selenium-grid/templates
cat selenium-grid-config.yml

aws cloudformation create-stack --stack-name ${GUID} --template-body file://selenium-grid-config.yml --parameters ParameterKey=NumberOfChromeNodes,ParameterValue=$tests_count ParameterKey=ClusterName,ParameterValue=${GUID} ParameterKey=LogName,ParameterValue=${GUID}