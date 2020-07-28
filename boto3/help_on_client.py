import boto3

aws_mag_con = boto3.session.Session(profile_name='root')

iam_con_cli = aws_mag_con.client(service_name='iam', region_name='us-east-1')
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='us-east-1')
s3_con_cli = aws_mag_con.client(service_name='s3', region_name='us-east-1')

'''
#List all users in aws using client object
response = iam_con_cli.list_users()
for each_item in response['Users']:
	print(each_item['UserName'])
'''
'''
# List all ec2 instance ids
response = ec2_con_cli.describe_instances()
for each_item in response['Reservations']:
	for each_instances in each_item['Instances']:
		print(each_instances['InstanceId'])
		print('-------------------------')
'''
# List all S3 objects
response = s3_con_cli.list_buckets()
for s3_list in response['Buckets']:
	print(s3_list['Name'])