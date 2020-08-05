Lambda function codes in Python used to list AWS EC2 instances and store the output as a text file on an Amazon S3 bucket

If you execute the Lambda function without modifying the execution role and attached required AWS IAM policies, your Lambda function will probably throw the following error after you save and test your function:An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation


To attach a policy, you need to switch to the Amazon IAM service. But before you launch AWS IAM service, note the name of the executive role you have created or selected in your Lambda function page.
Then launch the IAM Management Console. On the console, select Roles and filter your execution role of the AWS Lambda function you have recently created.
On the Permissions tab, it is possible to Attach policies
I attached the AmazonEC2ReadOnlyAccess policy which provides required permissions to reach to EC2 service and query all EC2 instances and describe each EC2 instance.

If your requirement is to list EC2 instances according to their states like listing all running or active AWS EC2 instances, or listing all stopped instances, etc you can modify the filters.
AWS Lambda developers can see that during filters declaration, I provided instance-state-name as a filter criterion but passed “*” to display all instance states excluding none of the instances actually.
You can refer to AWS documentation for a list of instance states.
Possible EC2 instance states: pending, running, shutting-down, terminated, stopping, stopped
Simply replace * with running to get the list of EC2 instances which are running at the Lambda function execution time
After the EC2 instance list is fetched and converted into a string with JSON.DUMPS() method, we can place this list into a text file and put it on an AWS S3 bucket.
In order to create or modify a text file on an Amazon S3 bucket, Lambda programmers can use “object().put()” in a boto3 library.
Of course, AWS developer should grant required permissions to write to related Amazon S3 buckets.

Otherwise, an error similar to followings might occur:
An error occurred (AllAccessDisabled) when calling the PutObject operation: All access to this object has been disabled or Read-only file system error
