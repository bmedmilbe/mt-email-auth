import os
import dj_database_url
from .common import *

# --- CORE SETTINGS ---
DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = [".railway.app", ".up.railway.app"]

DJANGO_SETTINGS_MODULE=os.environ["DJANGO_SETTINGS_MODULE"]

# --- CORS & CSRF CONFIGURATION ---
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "https://cmz.st",
    "https://www.cmz.st",
    "https://cecab.st",
    "https://www.cecab.st",
    "https://troca-4apd.vercel.app",
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS + [
    "https://*.railway.app",  
    "https://*.up.railway.app"
]

# Required for POST/PUT requests in production
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

# HTTPS Security Headers
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- DATABASE ---
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600, 
        ssl_require=True
    )
}

# --- AWS STORAGE ---
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_REGION_NAME = "eu-north-1"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_FILE_OVERWRITE = False

# --- EMAIL & DOMAIN ---
DOMAIN = os.environ.get("RAILWAY_STATIC_URL", "www.cmz.st")
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
MOVED = os.environ["MOVED"]

# --- MULTI-SITE EMAIL CONFIGURATION ---
WEBSITES = ["CMZ", "ORMED", "CECAB", "NANEHOUSE"]

CMZ_PASSWORD = os.environ["CMZ_PASSWORD"]
ORDMEDSTP_PASSWORD = os.environ["ORDMEDSTP_PASSWORD"]
CECABSTP_PASSWORD = os.environ["CECABSTP_PASSWORD"]

EMAILS = {
    WEBSITES[0]: {
        "EMAIL": "edmilbe@gmail.com",
        "TITLE": "CMZ",
        "PASSWORD": CMZ_PASSWORD,
        "WEBSITE": "https://camaramz-cc67c4aaa69f.herokuapp.com/",
        "LOGO": "https://www.camaramezochi.st/files/stp/camara2.png",
    },
    WEBSITES[1]: {
        "EMAIL": "ormedstp@gmail.com",
        "TITLE": "ORDMED-STP",
        "PASSWORD": ORDMEDSTP_PASSWORD,
        "WEBSITE": "https://ormedstp.herokuapp.com/",
        "LOGO": "https://ormedstp.herokuapp.com/images/logo-2.png",
    },
    WEBSITES[2]: {
        "EMAIL": "direcaocecab@gmail.com",
        "TITLE": "CECAB-STP",
        "PASSWORD": CECABSTP_PASSWORD,
        "WEBSITE": "https://www.cecab.st/",
        "LOGO": "https://www.cecab.st/images/logo.png",
    },
    WEBSITES[3]: {
        "EMAIL": "edmilbe@gmail.com", 
        "TITLE": "Edmilbe Ramos",
        "PASSWORD": EMAIL_HOST_PASSWORD,
        "WEBSITE": "https://www.edmilbe.pro/",
        "LOGO": "https://edmilbe-fa58f9b99040.herokuapp.com/light/assets/imgs/header/profile.jpg",
    },
}