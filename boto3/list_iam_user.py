import boto3

aws_mag_console = boto3.session.Session(profile_name="root")
iam_cons = aws_mag_console.resource('iam')

for each_user in iam_cons.users.all():
    print(each_user.name)