import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Make sure ALLOWED_HOSTS is defined only once
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'college-management-qn9m.onrender.com',  # Add your Render domain here
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)&29*7d1q$xxpib8v7-0_nkm)bkaw(b(g4i98%q0q#86z#&6=1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your apps
    'students',  # Add this line
    'channels',

]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'college_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'students/templates')],
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

WSGI_APPLICATION = 'college_management.wsgi.application'
ASGI_APPLICATION = 'college_management.asgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('VETTING_DB_NAME', default='vetting2024'),
        'USER': config('VETTING_DB_USER', default='saksham'),
        'PASSWORD': config('VETTING_DB_PASSWORD', default='iOtY90r5ObTEArqn6u4rTA'),
        'HOST': config('VETTING_DB_HOST', default='cvvettingportal-5744.7s5.aws-ap-south-1.cockroachlabs.cloud'),
        'PORT': config('VETTING_DB_PORT', default='26257'),
        'OPTIONS': {
            'options': '-c search_path=vetting_2425,public'
    },
},
    'vetting_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('VETTING_DB_NAME', default='vetting2024'),
        'USER': config('VETTING_DB_USER', default='saksham'),
        'PASSWORD': config('VETTING_DB_PASSWORD', default='iOtY90r5ObTEArqn6u4rTA'),
        'HOST': config('VETTING_DB_HOST', default='cvvettingportal-5744.7s5.aws-ap-south-1.cockroachlabs.cloud'),
        'PORT': config('VETTING_DB_PORT', default='26257'),
        'OPTIONS': {
            'options': '-c search_path=vetting_2425,public'
    },
}
}

DATABASE_ROUTERS = ['college_management.routers.Vetting2425Router']


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'  # or your desired timezone
USE_TZ = True
USE_I18N = True

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'students/static/students'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'