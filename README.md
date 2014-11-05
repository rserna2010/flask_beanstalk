flask_elastic_beanstalk_example
===============

Setting up Elastic Beanstalk 

1) Setup Eb command line interface
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
 
* boom all done
