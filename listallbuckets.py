#!/usr/bin/env python
import boto3

# Amazon S3

s3 = boto3.resource('s3')

#list all buckets
for bucket in s3.buckets.all():
        print(bucket.name)
        print()
