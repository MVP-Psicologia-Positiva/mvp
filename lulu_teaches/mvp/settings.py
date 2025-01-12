from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str,'DEFAULT'),
    DATABASE_URL=(str,'DEFAULT'),
    ENVIRONMENT=(str,'DEFAULT'),
    DB_NAME=(str,'DEFAULT'),
    DB_USER=(str,'DEFAULT'),
    DB_PASSWORD=(str,'DEFAULT'),
    DB_HOST=(str,'DEFAULT'),
    DB_PORT=(str,'5432'),
)
environ.Env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
DB_PASSWORD = env('DB_PASSWORD')
DATABASE_URL = env('DATABASE_URL')
ENVIRONMENT=env('ENVIRONMENT')
DB_NAME=env('DB_NAME')
DB_USER=env('DB_USER')
DB_HOST=env('DB_HOST')
DB_PORT=env('DB_PORT')

ALLOWED_HOSTS = [
    'https://img-lulu-mvp-988538575854.us-central1.run.app/',
    'https://img-lulu-mvp-988538575854.europe-west10.run.app',
    'https://lulu-teaches-988538575854.europe-west3.run.app',
    '127.0.0.1',
    'localhost',           
    '0.0.0.0'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',

    'lulu_teacher.apps.LuluTeacherConfig',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'rest_framework',
    'frontend.apps.FrontendConfig'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware"
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ROOT_URLCONF = 'mvp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/templates')],
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

WSGI_APPLICATION = 'mvp.wsgi.application'

# Database

DATABASES = {
    'default': env.db('DATABASE_URL')
}

if env.str('ENVIRONMENT') == 'production':
    
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'), 
        'PORT': env('DB_PORT', default='5432'), 
    }
else:

    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db-lulu-mvp',
        'USER': 'myuser',
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT':'5432'
    }


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

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/app/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


