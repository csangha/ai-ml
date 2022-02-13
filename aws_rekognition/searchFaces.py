#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import sys
import boto3

if len(sys.argv) < 3: 
    print("Please provide all arguments like bucket name, image name")
else:
    if __name__ == "__main__":

        bucket=sys.argv[1]
        fileName=sys.argv[2]
        threshold = 95 
        maxFaces=20

        client=boto3.client('rekognition')

        # Get list of all collections and then traverse through each one of them to find out the potential match

        response=client.list_collections(MaxResults=100)
        done=False
        matchFound = False

        while done==False:

            collections=response['CollectionIds']

            for collection in collections:
                personName = collection
                print("\n\nsearching in ", personName )

                responseFace=client.search_faces_by_image(CollectionId=personName,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                faceMatches=responseFace['FaceMatches']
                if len(faceMatches) > 0 : 
                    print ("**************\n\n\nFound match with ", personName)
                    matchFound = True
                    
                
                for match in faceMatches:
                    print ('FaceId:' + match['Face']['FaceId'])
                    print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                
            if 'NextToken' in response:
                nextToken=response['NextToken']
                response=client.list_collections(NextToken=nextToken,MaxResults=max_results)
            else:
                done=True

        if matchFound == False : 
            print ("The face did not match with any person in the database")

