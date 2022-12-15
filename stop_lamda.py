import boto3
region = "ap-south-1"
instances = ["i-04e3aa879d6d01047"]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print("stopped your instances: " + str(instances))