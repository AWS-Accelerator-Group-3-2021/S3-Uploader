import boto3
import os
import config

session = boto3.Session(
    profile_name='default',
    region_name=config.region_name
)

s3 = session.client('s3')

class S3:
    ## Uploading a file to S3
    @staticmethod
    def upload_file(file_name, s3FilePath):
        try:
            s3.upload_file(file_name, config.upload_file_bucket_name, s3FilePath)
            print('Uploaded file: ' + str(file_name))
            return True
        except:
            print("Error uploading file: ", file_name)
            return False
    
    ## Deleting a file from S3
    @staticmethod
    def delete_file(s3FilePath):
        try:
            s3.delete_object(Bucket=config.upload_file_bucket_name, Key=s3FilePath)
            print('Deleted file: ' + str(s3FilePath))
            return True
        except:
            print("Error deleting file: ", s3FilePath)
            return False