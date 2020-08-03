import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

ALLOWED_HOSTS = ["*"]
APPEND_SLASH=False

# Quick-start development settingss - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+p@6^55xm1&pu+g&7hv8r&&^rzg80m8&_m*d6!ry=e^(h(6rwv'

# 将Django默认用户表改为SysUser
AUTH_USER_MODEL = 'user_manage.SysUser'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user_manage',
    # 'oauth2_provider',  # 使用oauth2鉴权登录
    'corsheaders',
    'menu',
    'rest_framework_swagger',
    'goods'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 配合CORS_ORIGIN_ALLOW_ALL = True
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'adminDemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'adminDemo.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# APPEND_SLASH=False

# rest_framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication', # Oauth2认证
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # JWT认证
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'apps.common.pagination.StandardResultsSetPagination'
    # 'EXCEPTION_HANDLER':'utils.exception_handlers.custom_exception_handler'  # restframework 统一异常处理器，但是捕捉不到404异常， 是否可以重写CommonMiddleware中间件统一返回Response类型有待完善
}

# 自定义验证类
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'user_manage.views.CustomBackend',
]

import datetime
#有效期限
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=300),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',                       #JWT跟前端保持一致，比如“token”这里设置成JWT
    'JWT_RESPONSE_PAYLOAD_HANDLER':'utils.jwt_response_payload_handler.jwt_response_payload_handler'
}

# OAUTH2_PROVIDER = {
#     # this is the list of available scopes
#     'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
# }

# 引入sentry作为系统监控
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="http://19f9320561e1418cadefe269b12650e7@192.168.154.130:9000/3",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

STATIC_URL = '/static/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 手机号匹配规则
REGEX_MOBILE = r'^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
# 邮箱匹配规则
REGEX_EMAIL = r'^[A-Za-z0-9.]+@[A-Za-z0-9.]+.com$'