from uploader import *
## THIS IS A USAGE SAMPLE FILE
### OTHER CODE GOES HERE

## PART WHERE A FILE IS TO BE UPLOADED TO S3
for file in os.listdir(os.path.join(os.getcwd(), 'myfolder')):
    S3.upload_file(os.path.join(os.getcwd(), 'myfolder', file), 'myfolder/{}'.format(file))

## PART WHERE A FILE IS TO BE DELETED FROM S3
for file in os.listdir(os.path.join(os.getcwd(), 'myfolder')):
    S3.delete_file('myfolder/{}'.format(file))

## REQUIREMENTS FOR USAGE:
## .aws/credentials file in home directory
## config.py containing the following:
## upload_file_bucket_name = 'S3 BUCKET NAME HERE'
## region_name = 'REGION NAME HERE'