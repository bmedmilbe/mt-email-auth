import os
import dj_database_url
from .common import *

# DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

# EMAIL_HOST = os.environ["EMAIL_HOST"]
# EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
# EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
# EMAIL_PORT = os.environ["EMAIL_PORT"]  # 25
# EMAIL_USE_TLS = os.environ["EMAIL_USE_TLS"]

DEBUG = False
ALLOWED_HOSTS = ["camaramzapi-6cf2b687304f.herokuapp.com"]
DJANGO_SETTINGS_MODULE = os.environ["DJANGO_SETTINGS_MODULE"]


# If this is used, then not need to use `CORS_ALLOW_ALL_ORIGINS = True`
CORS_ALLOWED_ORIGINS = [
    "http://camaramz.com",
    "http://camaramz.herokuapp.com",
    "https://camaramz.com",
    "https://camaramz.herokuapp.com",
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    "https://localhost",
    "https://127.0.0.1:3000",
    "https://127.0.0.1",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    "http://camaramz.com",
    "http://camaramz.herokuapp.com",
    "https://camaramz.com",
    "https://camaramz.herokuapp.com",
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    "https://localhost",
    "https://127.0.0.1:3000",
    "https://127.0.0.1",
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True


DATABASES = {"default": dj_database_url.config()}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]
MOVED = os.environ["MOVED"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DOMAIN = "camaramz-cc67c4aaa69f.herokuapp.com"

# ALLOWED_HOSTS = ["camaramz.herokuapp.com"]



EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "edmilbe@gmail.com"
EMAIL_HOST_PASSWORD = "vpawkftfpryiqaly"
EMAIL_PORT = 587  # 25
EMAIL_USE_TLS = True


# https://www.totaljobs.com/job/warehouse-operative/proman-job101381919?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic

# AWS_ACCESS_KEY_ID = 'AKIA2QHYRZDKXSR7F2KK'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'bm-edmilbe-bucket'
# # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # storages.backends.s3boto3.S3Boto3Storage
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)



AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
