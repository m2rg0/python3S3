#!/usr/bin/env python
import boto3

# Amazon S3

s3 = boto3.resource('s3')

# Set bucket name
bucket = s3.Bucket('2x2demo')
print (bucket.name)
print ()

# This works:
# List contents of Bucket
#for object in bucket.objects.all():
#    print(object)

#This works:
for file in bucket.objects.all():
    print (file.key, file.storage_class, file.last_modified)
    print()

#does not work
#for object in bucket.objects.all():
#    yoke = object.Object()
#    print(yoke.key, yoke.storage_class, yoke.last_modified, yoke.version_id, yoke.metadata)
#    print()
