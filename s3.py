import boto3

# AWS Pricing (adjust for different regions if needed)
STORAGE_COST_PER_GB = 0.023  # Example for us-east-1
PUT_REQUEST_COST = 0.005 / 1000
GET_REQUEST_COST = 0.0004 / 1000
DATA_TRANSFER_COST_PER_GB = 0.09  # Example for first 10 TB

# S3 Client
s3 = boto3.client('s3')

# Define bucket name
BUCKET_NAME = "your-bucket-name"

def get_storage_size():
    """Get total storage size of an S3 bucket in GB"""
    total_size = 0
    paginator = s3.get_paginator('list_objects_v2')
    
    for page in paginator.paginate(Bucket=BUCKET_NAME):
        if "Contents" in page:
            for obj in page["Contents"]:
                total_size += obj["Size"]
    
    return total_size / (1024 ** 3)  # Convert bytes to GB

def estimate_s3_cost(storage_gb, put_requests=100000, get_requests=500000, data_transfer_gb=50):
    """Estimate S3 Standard storage cost"""
    storage_cost = storage_gb * STORAGE_COST_PER_GB
    put_cost = put_requests * PUT_REQUEST_COST
    get_cost = get_requests * GET_REQUEST_COST
    data_transfer_cost = data_transfer_gb * DATA_TRANSFER_COST_PER_GB

    total_cost = storage_cost + put_cost + get_cost + data_transfer_cost
    return {
        "Storage Cost": round(storage_cost, 2),
        "PUT Request Cost": round(put_cost, 2),
        "GET Request Cost": round(get_cost, 2),
        "Data Transfer Cost": round(data_transfer_cost, 2),
        "Total Monthly Cost": round(total_cost, 2)
    }

if __name__ == "__main__":
    storage_gb = get_storage_size()
    cost_estimation = estimate_s3_cost(storage_gb)

    print(f"📦 S3 Bucket: {BUCKET_NAME}")
    print(f"Total Storage: {storage_gb:.2f} GB")
    print(f"💰 Estimated Monthly Cost Breakdown:")
    for key, value in cost_estimation.items():
        print(f"{key}: ${value}")
