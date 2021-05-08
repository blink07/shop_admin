from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

#
# """
# restframework注册信号量时，需在apps.py文件中导入信号量(下面两种方法都需要导入)，同时__init__文件也许导入config配置
# """
#

@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        password = instance.password
        #instance相当于user
        instance.set_password(password)
        instance.save()