import boto3


ec2 = boto3.client('ec2')

pricesUSE1a = ec2.describe_spot_price_history(AvailabilityZone='us-east-1a')
pricesUSE1b = ec2.describe_spot_price_history(AvailabilityZone='us-east-1b')
pricesUSE1c = ec2.describe_spot_price_history(AvailabilityZone='us-east-1c')
pricesUSE1d = ec2.describe_spot_price_history(AvailabilityZone='us-east-1d')
pricesUSE1e = ec2.describe_spot_price_history(AvailabilityZone='us-east-1e')

for instance in ec2.instances.all():
    print(
         "Id: {0}\nType:".format(
         instance.id, instance.instance_type
         )
     )

print(pricesUSE1a, pricesUSE1b, pricesUSE1c, pricesUSE1d, pricesUSE1e)


