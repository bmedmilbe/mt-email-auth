import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ["SECRET_KEY"]
STRIPE_SK = os.environ["STRIPE_SK"]
PRICE_PARCEL_BY_KG = os.environ["PRICE_PARCEL_BY_KG"]
PRICE_FLIGTH_BY_KG = os.environ["PRICE_FLIGTH_BY_KG"]
DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = os.environ["EMAIL_PORT"]  # 25
EMAIL_USE_TLS = os.environ["EMAIL_USE_TLS"]

DEBUG = False
ALLOWED_HOSTS = ["camaramzapi.herokuapp.com"]
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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["camaramz.herokuapp.com"]


AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME'] 
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME

