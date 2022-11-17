# ETL Pipeline using Cloudformation

In this project, I will set up AWS infrastructure using the `AWS cloudformation` service. As well as setting up docker containers using a docker compose to productionalise the code for use at scale.

## Using Cloud Formation

Once the `YML` file has been written describing your desired architecture run the following code in the terminal (assuming that you have the AWS CLI)

```sh
$ aws cloudformation create-stack --stack-name \
cloudformation-example \
--template-body aws_resource_config.yml \
--parameters ParameterKey=AvailabilityZone, \
ParameterValue=us-east-1a \
ParameterKey=EnvironmentType,ParameterValue=dev \
ParameterKey=KeyPairName,ParameterValue=jenna \
ParameterKey=DBPassword,ParameterValue=Abcd1234
```

Or alternatively you can use Boto3 (AWS SDK for python), in which case the implementation is much more programatic. Navigate to the `aws_resources/ETL_config.py` file and edit the perameters to your liking, then simply run the file.


