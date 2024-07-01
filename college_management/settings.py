import os
from django.http import JsonResponse
import json
from pathlib import Path
from decouple import config, Csv, AutoConfig

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ensure the environment variables are loaded
config = AutoConfig(search_path=BASE_DIR)

# Directly define the service account JSON content with properly escaped newline characters
SERVICE_ACCOUNT_JSON = '''
{
  "type": "service_account",
  "project_id": "collegemanagement-427410",
  "private_key_id": "1c5c8766d36658c0898244f0a6c519132bbca17c",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC00XBJ+rVTp6Dk\\naQDl+VC8syHvcVmBfN8L4YwJGePdO1DkXduKZIcAsjvRAPQ4RVKDFAEaFW1K3xlI\\nc8ByhAzV3vFQj19wJmjXx86tKxQ/FlCz/rFz3islM65BM9YloWptoLnqaxuH6pVb\\nOhHlrzgpnDfG/dC+SBXIjgiyEi0Fd/4E777TxPNk79GlW9CW5Xd8BKe001VcXRHj\\nqB0o2V+JEqmEx5CI9ZxxgRuIHdnMomMYnG2T6PZndXD55BsnNzob2uBZUT4TvW7e\\nlB8vEnb3vsbkWZ83i9XHKd8G/TAh6AQcYTImuO+0ggQLHm96uMzf9mR28Auc3a7J\\nc6Glxa0hAgMBAAECggEACm7LJnmWB22fQDk5brYj4moI2zfpt37s9P0z3JKR2IHu\\nTj7cG/AQ716un4XekXXufNb6o/ajMl63prvcWWnPvnH5RRyrSl1CT1udS9XgeoNf\\nGgOSruIdZdga2x2SjY6dWsCbTts/NhMNlbs+rRyfBkeX2vNqHTsrhpbWCZri3h3P\\n91rRlpSG05L55DpbiOyb8qgMsEP/aV0SY5j7u7XADLdRENv3XVQ1iXa0l7bZ0p1h\\nYHxH1tUeRXqC+Wev50c9qcx7/SmaPv/iMM3mlnWy2vyOtTJEnbtVkCQ4jnu9Hg2K\\n3DpS4kJFfaFq7hrQu2V+8g5WdZOdaeNh5wX9Lub0wQKBgQDvbSxJQ/70t589KKKD\\nbM4J+7t1EWl4N/7rDeaBa0cwu192kbfCtyY0tNqr7/XTkxtmCKx6MzCXyKkO+zNp\\njUgbIuXsHFRsG/uKgigO5+G5Mkkf6DwujVRYMnADdgD0Q58z51II4exhqtU5VSbb\\nw8kLpfLHzJ6tGoGNFlrR9RYG+wKBgQDBVa3pXvnNvrRoT01bYpbq18F6pp3hSuEl\\ntNnYcaU+4oEpAhENdglYAd6InYUTqmqN/yAhvs4MqWWgjmWuyGPGFBKH/FaWK21S\\nFJAICg9Ay0bHXNDzX3ptRyfBv0XUTMXc58zIu5qQNfrtC4Nj/l5DyNJKb91DPJ5+\\nJtPsPqsRkwKBgQDgPGxEtgUbprnhqqQB2K5jlTss2kDgUflSpbMjtJh5IJO41aK4\\nH5YNuPAwJc4i+FypxCfdTwIMteb32/Z7vdExcQ7LgoDiu5ZrU5k21J+INntcAcIT\\ni1PaQmq8IxGjs41wLA6duRINKtUGHCUHoCcz3Jkz3QUjdHau76fhidu2bwKBgGAI\\n2Ux1GwzyT9cInVppjKG27qqoHQCOG2yJezSirvyfspzWI/ZVzapjs1CVPkdYfXlv\\nY1yf1OZBNvQcB7JcZAM+cT4PQEtz4ufEww7bQFxlHRFmr3xUzxF9KOh6xIsCX76t\\nffGwDsTXq38YGvoOnnB5Tswe6P+/GtN7IgXV00/1AoGAYgq0qHKrGblc6UFQuofT\\nL4VMHH1HXTXnzSN60xMqiwH9BUtY/n49ntbwY0aUVFcb48lRKoEtQIYhitwu0sYl\\ndOyydnLwRrL/NISN5+gjWMGH2ZKhkIIs4hP+s/5oKvQ5VE9PggiWEYSRSz04Rp7k\\nlQkr7NsqSDhs6nZkB6gFasA=\\n-----END PRIVATE KEY-----\\n",
  "client_email": "theplacementcellsrcc@collegemanagement-427410.iam.gserviceaccount.com",
  "client_id": "112720430311695231753",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/theplacementcellsrcc%40collegemanagement-427410.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
'''

service_account_info = json.loads(SERVICE_ACCOUNT_JSON)
SHEET_ID = '1I5-Yre2sUJq-8j2aKZkjsKxtc-9LMcdhxWvu-OzhwO8'
RANGE_NAME = 'Sheet1!A:Z'

# Print environment variables to debug
print("SERVICE_ACCOUNT_JSON in settings:", service_account_info)
print("SHEET_ID in settings:", SHEET_ID)
print("RANGE_NAME in settings:", RANGE_NAME)

# Add service_account_info to the Django settings
SETTINGS_EXPORT = {
    'SERVICE_ACCOUNT_INFO': service_account_info,
    'SHEET_ID': SHEET_ID,
    'RANGE_NAME': RANGE_NAME,
}

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
]

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

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='student_database'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default='sakshamd26'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'students/static/students'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
