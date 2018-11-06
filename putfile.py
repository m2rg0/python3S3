#!/usr/bin/env python
import boto3

# Amazon S3

s3 = boto3.resource('s3')

#list all buckets
#for bucket in s3.buckets.all():
#        print(bucket.name)

bucket = s3.Bucket('2x2demo')
#upload a file to S3
try:
    data = open('/Users/mcronin/Documents/07Projects/endpointdemo/text_too.txt', 'rb')
except Exception as error:
    print (error)
try:
    print ("calling put object")
    bucket.put_object(Key='text_too.txt', Body=data)
    print ("done")
except Exception as error:
    print (error)