"""
Django settings for pigshop project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

#import django_heroku
import smtplib
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#%h)^nfj46cflt7%r6u#^*a_rng&*fmr^(nx+d2i5lc1zyjw_8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['piggimart.herokuapp.com',
                 'piggimart.com', 'www.piggimart.com']

STRIPE_PUB_KEY = 'pk_test_51LLCFxIhfxZGpACagCmBvIKG77uffGGGpdMIFEYP8undZtWXPF3kLzTogOtMXAkp5pyyvrRcUFnlAIYNmYtdQv1k001Kj3FWnQ'
STRIPE_SECRET_KEY = 'sk_test_51LLCFxIhfxZGpACat3ECpZAeehGVGdADb0AxZ8uVT1fiUAULEEh9Fb4Yu1fWXogBbieCHYFdsrcKfr4lnaKtuxhn00DsmOEEjM'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chiagoziemleonard@gmail.com'
EMAIL_HOST_PASSWORD = 'fnzkckwmiruyiyny'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = 'Piggimart <noreply@piggimart.com>'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'apps.cart',
    'apps.core',
    'apps.order',
    'apps.vendor',
    'apps.product',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pigshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'pigshop.wsgi.application'


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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_heroku.settings(locals())
