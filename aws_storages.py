from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage
from os import environ


class StaticStorage(S3Boto3Storage):
    location = '%s/static' %environ['AWS_FOLDER']
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = '%s/media' %environ['AWS_FOLDER']
    default_acl = 'public-read'
    file_overwrite = False