import os
from .com_settings import BASE_DIR
DEBUG = True


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': "django.db.backends.mysql",
        'NAME': 'dev_admin',
        # 'HOST':'192.168.255.128',
        # 'HOST':'127.0.0.1',
        # 'HOST':'192.168.246.129',
        'HOST':'192.168.246.129',
        'PORT':3306,
        'USER':'root',
        # 'PASSWORD':'root'
        'PASSWORD':'123456'
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

