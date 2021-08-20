"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# __file__: settings.py
# os.path.abspath(__file__) : /Users/meihao/Desktop/code/demo/demo/settings.py
# os.path.dirname():    /Users/meihao/Desktop/code/demo/demo
# os.path.dirname():    /Users/meihao/Desktop/code/demo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fs+w)ukcpl5bj-jk3lz&%**#hd!bw24sj8!e*-wo5b1*nc9l33'

# 开启调试模式: true
# 如果把调试模式关闭, 需要设置 ALLOWED_HOSTS
DEBUG = True

# ALLOWED_HOSTS是白名单.
ALLOWED_HOSTS = ["127.0.0.1"]
# ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'users.apps.UsersConfig',
    'requresp.apps.RequrespConfig',
    'db2_test',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'sql_test',
        'PASSWORD':'mysql',
        'PORT':3306,
        'HOST':'127.0.0.1',
        'USER':'wangjun',
        # 'CONN_MAX_AGE':15,  #在视图函数请求之前和请求之后才检查
        # "POOL_OPTIONS":{
        #     "POOL_SIZE":2,
        #     "MAX_OVERFLOW":1
        # }
    },
    'db2':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql_test2',
        'PASSWORD':'mysql',
        'PORT':3306,
        'HOST':'127.0.0.1',
        'USER':'root',
    }
}
DATABASE_ROUTERS = ['demo.database_router.DatabaseAppsRouter']



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# 把语言设置为中文
LANGUAGE_CODE = 'zh-hans'

# 时区
TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # /Users/meihao/Desktop/code/demo/static_files
    os.path.join(BASE_DIR, 'static_files')
]
