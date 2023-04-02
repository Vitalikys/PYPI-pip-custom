from aws_service.ec2_service import Ec2Service
from aws_service.s3_service import S3Service
from aws_service.cloudwatch_service import CloudwatchService

my_s3 = S3Service()
my_s3.create_new_bucket(bucket_name='my_new_bucket_from_pypi', region='us‑east‑1') #(N. Virginia)
# my_s3.put_file( file_name='file_1', bucket='my_new_bucket', object_name='custom-name')
# my_s3.check_exist()

