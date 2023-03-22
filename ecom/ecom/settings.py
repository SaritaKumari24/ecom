from pathlib import Path
from django.contrib.messages import constants as msg

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t-#1s2@(fd@w29gkr^1mhxdo^%l%)9i50h*)2_nj8ff$fzu8c9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "shop",
    "crispy_forms",
    "crispy_tailwind",
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "template"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"
STATICFILES_DIRS =[BASE_DIR / "static"]


# paytm gateway details 

PAYTM_COMPANY_NAME = "Ecom"   # For representation purposes 
PAYTM_INDUSTRY_TYPE_ID = "PROD"     # For staging environment
PAYTM_CHANNEL_ID = "WEB"
PAYTM_MERCHANT_KEY = "H1J3@E1#NsG!vsSy"
PAYTM_MERCHANT_ID = "Orbmou57491502380880"
PAYTM_CALLBACK_URL = "http://localhost:8000/response/" # Hardcode
PAYTM_WEBSITE = "DEFAULT"
PAYTM_PAYMENT_GATEWAY_URL = "https://securegw.paytm.in/order/process"
PAYTM_TRANSACTION_STATUS_URL = "https://securegw.paytm.in/order/status"

#message alert 
MESSAGE_TAGS  = {
    #msg.DEBUG : "alert alert-info",
    #msg.ERROR : "alert alert-danger",
    #msg.SUCCESS : "alert alert-success",
    #msg.WARNING : "alert alert-warning",
    
     msg.DEBUG : "bg-sky-200 text-white px-3 rounded py-1",
     msg.ERROR : "bg-rose-200 text-white px-3 rounded py-1",
     msg.SUCCESS: "bg-green-200 text-white px-3 rounded py-1",
     msg.WARNING: "bg-yellow-200 text-white px-3 rounded py-1",
     
}