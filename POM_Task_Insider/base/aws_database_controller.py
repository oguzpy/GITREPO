import boto3

class S3Uploader:
    @staticmethod
    def connect_to_s3():
        s3 = boto3.resource(
            's3',
            region_name="eu-north-1",
            aws_access_key_id="AKIA6GBMFXFZO2JE3SLM",
            aws_secret_access_key="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"
        )

        return s3

    @staticmethod
    def upload_image_to_s3(image_file, bucket_name, object_name):
        bucket_name = 'oguz-bootcamp'
        region_name = 'eu-north-1'
        access_key_id = 'AKIA6GBMFXFZO2JE3SLM',
        secret_access_key = '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'

        s3 = S3Uploader.connect_to_s3()
        s3.Bucket(bucket_name).upload_file(image_file, object_name, ExtraArgs={'ContentType': 'image/jpeg'})


# Usage:
image_file = '/Users/oguzcelik/PycharmProjects/insiderbootcampproject-oguzpy/base/oguz_test.png'
bucket_name = 'bootcamp-oguz'
object_name = 'images/oguz_test.png'

# S3Uploader.upload_image_to_s3(image_file, bucket_name, object_name)
