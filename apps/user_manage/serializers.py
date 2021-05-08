import re

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from adminDemo.settings import REGEX_MOBILE
from user_manage.models import SysUser, Role, PermissionRole

User = get_user_model()


class PermissionRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRole
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):

    # children = PermissionRoleSerializer

    class Meta:
        model = Role
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    """
    用于查看用户信息
    """
    class Meta:
        model = SysUser
        fields = ('id','username', 'email', "mobile", "role", "is_active", "state")


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册
    在序列化类中重新声明的字段需要在Meta的fields中列出

    """
    username = serializers.CharField(label="用户名", required=True, help_text="用户名", allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')])

    # 输入密码的时候不显示明文
    password = serializers.CharField(style={'input_type': 'password'}, label=True, write_only=True)

    # 已使用信号量实现
    # def create(self, validated_data):
    #     """
    #     重写create方法，将password加密保存
    #     :param validated_data:
    #     :return:
    #     """
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate(self, attrs):
        # attrs["mobile"] = attrs["username"] # 当username符合手机号码匹配规则时，将用户名赋值给电话号码
        if re.match(REGEX_MOBILE, attrs["username"]):
            attrs["mobile"] = attrs["username"]
        return attrs

    class Meta:
        model = User
        fields = ('username', 'mobile', 'email', 'password')