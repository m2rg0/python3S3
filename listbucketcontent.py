#!/usr/bin/env python
import boto3

# Amazon S3

s3 = boto3.resource('s3')

# Set bucket name
bucket = s3.Bucket('2x2demo')
print (bucket.name)
print ()

# This works too:
# List contents of Bucket
#for object in bucket.objects.all():
#    print(object)

#This works:
for file in bucket.objects.all():
    print (file.key, file.storage_class, file.last_modified)
    print()


