import boto3

#aws_mag_console=boto3.session.Session(profile_name='root')

aws_mag_console=boto3.session.Session()


iam_con_res = aws_mag_console.resource(service_name='iam', region_name='us-east-1')
ec2_con_res = aws_mag_console.resource(service_name='ec2', region_name='us-east-1')
s3_con_res = aws_mag_console.resource(service_name='s3', region_name='us-east-1')

'''
# List all
for each_item in iam_con_res.users.all():
	print(each_item.user_name)
'''
'''
for each_s3 in s3_con_res.buckets.all():
	print(each_s3.name)
'''

for each_ec2 in ec2_con_res.instances.all():
	print(each_ec2.instance_id)
	



