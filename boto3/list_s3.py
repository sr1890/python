import boto3

aws_mag_con=boto3.session.Session(profile_name='root')

s3_con = aws_mag_con.resource('s3')

for each_s3 in s3_con.buckets.all():
    print(each_s3.name)