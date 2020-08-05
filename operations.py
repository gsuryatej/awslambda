# This Code will get the list of "Running" instances and create the .txt file object in s3 bucket and terminate the running instances.
import json
import boto3

ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')

def lambda_handler(event, context):

    filters = [
    {
    'Name': 'instance-state-name',
    'Values': ['running']
    }
    ]

    instances = ec2.instances.filter(Filters = filters)
    RunningInstances = []
    for instance in instances:
        RunningInstances.append(instance.id)
    ec2.instances.filter(InstanceIds=RunningInstances).terminate()
    instanceList = json.dumps(RunningInstances)
    s3.Object('lambda-s3eventtrigger','instanceList1.txt').put(Body = instanceList)
    return {
    "statusCode": 200,
    "body": instanceList
    }