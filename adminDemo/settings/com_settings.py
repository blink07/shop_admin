import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
from datetime import datetime as d

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
    'channels',
    'dashboard',
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
    'goods',
    'drf_yasg',
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
    # 'apps.middlewares.exception_middlewares.ExceptionMiddleware',
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

# WSGI_APPLICATION = 'adminDemo.wsgi.application'
ASGI_APPLICATION = 'adminDemo.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('192.168.154.134', 6379)],
        },
    },
}

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
    'EXCEPTION_HANDLER':'utils.exception_handlers.custom_exception_handler'  # restframework 统一异常处理器，但是捕捉不到404异常， 是否可以重写CommonMiddleware中间件统一返回Response类型有待完善
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

# Django日志
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
if not os.path.exists(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)
LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        # 默认的
        # 'default': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
        #     'filename': os.path.join(BASE_LOG_DIR, "{}.log".format(datetime.now().date())),  # 日志文件
        #     'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
        #     'backupCount': -1,  # 最多备份几个
        #     'formatter': 'simple',
        #     'encoding': 'utf-8',
        # },

        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "admin.log"),  # 日志文件
            'when': 'midnight',
            'interval': 1,
            'backupCount': -1,  # 最多备份几个
            'atTime': d.now().time().replace(0, 0, 0),   # 每天0时0分0秒进行翻转
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
       # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'console'],  # 上线之后可以把'console'移除
            'level': 'INFO',
            'propagate': True,  # 向不向更高级别的logger传递
        },
    },
}


# swagger
# swagger 地址需要过滤，不能按统一格式返回
SWAGGER_URL = ["/swagger/", "/redoc/", "/swagger.json", "/swagger.yaml"]