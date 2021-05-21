#!/bin/bash

. dev.config

`aws configure set aws_access_key_id "$AWS_ACCESS_KEY" --profile flask-app`
`aws configure set aws_secret_access_key "$AWS_SECRET_KEY" --profile flask-app`

BUCKETS=`aws s3api list-buckets --profile flask-app --query 'Buckets[*].Name' --output text | tr " " "\n"`
for BUCKET in $BUCKETS
do
    {
        SIZE=`aws s3 ls s3://$BUCKET  --profile flask-app --recursive | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024}'`
        printf '%s:%s MB\n' $BUCKET $SIZE
    }
done