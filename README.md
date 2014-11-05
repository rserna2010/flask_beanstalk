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

**2) Initialize your repo** 

* Initialize Your Git Repository by either cloning this repo or intializing a new repo
``` 
git init .
``` 

**3) Configure AWS Elastic Beanstalk** 
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
 * Attach an instance profile (select the intance profile with the appropriate role policy, which can be edited in the IAM section) 
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

**4) Create the App** 
* Run the following command to create and deploy the app which you initialized in step 2
```
eb start
```

* This will take 5-10 mins, sit back, relax, and maybe have a protein shake. Just don't be all bro-ey about it. Done? Awesome, now check the status of your app
```
eb status --verbose
```
 * If built properly it will show Greeen. A URL will be provided for your app, check it out in the browser. 
 
**5) Update your app** 
* Edit your app, and make sure to commit the changes.
```
eb push 
```

**5) Destroy your app** 
```
eb stop # terminate the environment 
eb delete # delete the app
```

**Other Helpful Hints**  
* When deploying a python app, use a requirements.txt file to upload modules (they will be automatically installed when deployed)
* To change the configuration options edit the optionsettings file in the .elasticbeanstalk directory .
 * You can also set environment variables in this file (or in the configuration section of the management console as a key pair)

 



