#!/usr/bin/env python
#import sys
import boto3

client = boto3.client('s3')
#for key in sys.argv[1:]:

try:
    client.delete_object(Bucket='2x2demo', Key="/home/mcronin/test.txt")
    print("done")
except Exception as error:
    print (error)
