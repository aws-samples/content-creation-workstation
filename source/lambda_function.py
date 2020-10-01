from crhelper import CfnResource
import boto3
import datetime

helper = CfnResource()

@helper.create
@helper.update
def get_ami(event, _):
    client = boto3.client('ec2')
    
    product_id = get_productid(event)
    print('Got ProductID: %s' % product_id)
    response = client.describe_images(
    Filters=[

        {
            'Name': 'product-code',
            'Values': [product_id]
        },
        {
            'Name': 'product-code.type',
            'Values': ['marketplace']
        }
    ]
    # ImageIds=[
    #     'ami-03dc6d7f59e5f1765'],
    
    )
    #rint(response)
    images = response['Images']
    latest_creation_date = datetime.datetime.min
    id = ''
    for image in images: 
        
        date_time_str = image['CreationDate'] 
        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        print ('This image has AMI name: %s  and the image-id is: %s. It was created on: %s' % (image['Name'], image['ImageId'], image['CreationDate'])) 
        print ('Proudct ID: %s' % image['ProductCodes'])
        print ('Owner is %s' % image['OwnerId'])
        if date_time_obj >= latest_creation_date:
            latest_creation_date = date_time_obj
            id = image['ImageId']
    
    print('Latest AMI ID: %s' % id) 
    print('Latest Creation Date: %s' % latest_creation_date)
    helper.Data['AMIID'] = id


def get_productid(event):
    productids = {'linux': 'ai7s3sm9muv8bw9y12z9t6o8i', 'windows': '4af6zv023dsu3c28day09b2a9'} 
    os_type = event['ResourceProperties']['OSType']
    return productids.get(os_type)
    
@helper.delete
def no_op(_, __):
    pass

def handler(event, context):
    #get_ami(event,context)
    helper(event, context)