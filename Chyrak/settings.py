"""
Django settings for Chyrak project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-09f8h!z_(^1nd0mzsxa(1i92ymw-$7kac!^+6-iv_)_h^775l#'

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
    'main.apps.MainConfig',
    'registration.apps.RegistrationConfig',
    'person.apps.PersonConfig',
    'search.apps.SearchConfig',
    'list_of_person.apps.ListOfPersonConfig',

    #registration apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitter',

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

ROOT_URLCONF = 'Chyrak.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'Chyrak.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    '/var/www/static/',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    #'social.backends.twitter.TwitterOAuth',
]

# AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'webmaster@localhost'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USERNAME_REQUIRED = False

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'afaricanistan@gmail.com'
EMAIL_HOST_PASSWORD = 'afarica0101'
EMAIL_PORT = 587

SOCIALACCOUNT_PROVIDERS = {
    'google': {

        'APP': {
            'client_id': '559980417286-sq6dqavakgpa5ove53ejp6ufv7542e80.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'facebook':
           {'METHOD': 'oauth2',
            'SCOPE': ['email','public_profile', 'user_friends'],
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
            'FIELDS': [
                'id',
                'email',
                'name',
                'first_name',
                'last_name',
                'verified',
                'locale',
                'timezone',
                'link',
                'gender',
                'updated_time'],
            'EXCHANGE_TOKEN': True,
            'LOCALE_FUNC': lambda request: 'kr_KR',
            'VERIFIED_EMAIL': False,
            'VERSION': 'v2.4'}
}

#Google
#559980417286-sq6dqavakgpa5ove53ejp6ufv7542e80.apps.googleusercontent.com
#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

#Facebook
#597464698959892

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'login'


