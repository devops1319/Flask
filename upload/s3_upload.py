'''import boto3
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAYOTRUKBAV6ESOUUN',
aws_secret_access_key='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'
)
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
result = s3.meta.client.put_object(Body='Text Contents', Bucket='sedataset', Key='filename.txt')
res = result.get('ResponseMetadata')
print(res)
if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')'''

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAYOTRUKBAV6ESOUUN'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')
