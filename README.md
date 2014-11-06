flask_elastic_beanstalk_example
===============

**1) Set up Elastic Beanstalk Command Line Interface** 

* pip install awsebcli
*  Yes, it's that easy. 
 
* Ensure eb is now setup
  ``` 
  eb --help
  ``` 
* NOTE: If you previously had installed the EB command line tool via a zip file, be sure to delete that unzipped file 

**2) Configure AWS Elastic Beanstalk** 
* CD into the parent directory of your app and configure elastic beanstalk 

  ``` 
   eb init –p Python
  ``` 

  or to select a more specfic configuration

  ``` 
  eb init
  ```  

* Given the second option EB will ask for the following information to deploy the app
 * Service region (select 1, for us-east-1)
 * Select an application to use (you can create a new one, or a previously used one stored in AWS EB)
 * Select an Application Name
 * Select a Platform (in this case Python)
 * Select a platform version
 * Set up SSH for your instances
 

**3) Create the App** 
* Run the following command to create and deploy the app which you initialized in step 2
  ```
  eb create flask-beanstalk-env
  ```

* This will take 5-10 mins, sit back, relax, and maybe have a protein shake. Just don't be all bro-ey about it. Done? Awesome, now check the status of your app
  ```
  eb status --verbose
  ```
  
 * If built properly it will show Greeen. A URL will be provided for your app, check it out in the browser. 
 ```
  eb open
  ```

**4) Update your app** 
* Edit your app, and deploy the changes
 
  ```
  eb deploy 
  ```

**5) Destroy your app** 
 
  ```
  eb terminate
  
  ```

**Other Helpful Hints** 
* You need to ensure you have the proper permissions to use SQS. Be sure to attach an instance profile (select the intance profile with the appropriate role policy, which can be edited in the IAM section) 
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
* When deploying a python app, use a requirements.txt file to upload modules (they will be automatically installed when deployed)
* To change the configuration options edit the optionsettings file in the .elasticbeanstalk directory .
 * You can also set environment variables in this file (or in the configuration section of the management console as a key pair)
