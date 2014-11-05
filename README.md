flask_elastic_beanstalk_example
===============

**1) Set up Elastic Beanstalk Command Line Interface** 

* Downloand http://aws.amazon.com/code/6752709412171743
* Unzip the downloaded file (zip file is self-contained and no installation is required)
* create a file containing your access key ID and secret access key (I just named my aws_creds)

File should look like :
``` 
AWSAccessKeyId=Write your AWS access ID
AWSSecretKey=Write your AWS secret key
```

*  set the AWS_CREDENTIAL_FILE environment variable so that the AWS Elastic Beanstalk CLI tools can find your information.
``` 
export AWS_CREDENTIAL_FILE=<the file created above>
``` 
 
* Ensure eb is now setup
``` 
eb --version
``` 

**2) Deploy your first app** 

* Initialize Your Git Repository by either cloning this repo or intializing a new repo
``` 
git init .
``` 
 
* CD into the parent directory of your app and configure elastic beanstalk 
``` 
eb init
```  
* Next EB will ask for the following information to deploy the app
 * AWS access key ID (hit enter if you followed above steps) 
 * AWS secret key (hit enter if you followed above steps) 
 * Service region (select 1, for east-us-1)
 * Application name (will default to name of directory unless changed)
 * Environment name (will default tp name of directory-env unless changed)
 * Select an Environment Tier (1 is Webserver, 2 is Worker)
 * Select a solution stack (36 is 64bit Amazon Linux 2014.09 v1.0.9 running Python 2.7 used in this app) 
 * Select environment type (LoadBalanced vs SingleInstance)
 * Create an Amazon Relational Database Database Instance (defaults to msyql if yes is selected) 
   *For more info on Amazon RDS http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python.rds.html 
 * Attach an instance profile (select the intance profile with the appropriate role policy) 
   * This app requires SQS:GetQueueURL, SQS:GetQueueAttributes, SQS:SendMessage 
   ``` 
   {
            "Sid": "QueueAccess",
            "Action": [
                "sqs:GetQueueURL",
                "sqs:GetQueueAttributes",
                "sqs:SendMessage"
            ],
            "Effect": "Allow",
            "Resource": "*"
   },
   ``` 

