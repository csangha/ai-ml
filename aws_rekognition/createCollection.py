#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import sys


def create_collection(collection_id):

    client=boto3.client('rekognition')

    #Create a collection
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main(argv):
    collection_id=argv[1]
    print("Collection Name: ", collection_id)
    create_collection(collection_id)

if len(sys.argv) < 2:
    print("Please pass the collection name")
else:
    print('Collection Names: ', str(sys.argv))
    if __name__ == "__main__":
        main(sys.argv)    

