from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, status, viewsets, filters
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler

from common.pagination import StandardResultsSetPagination
from menu.models import Permission
from user_manage.serializers import UserSerializer, UserRegSerializer, RoleSerializer
from utils.error import ERROR_USER_RALATION
# from .filters import UserFilter
from .models import Role, PermissionRole
from .utils import Captcha
from utils.mixins import *

User = get_user_model()


class GetCodeInfo(APIView):
    """
    获取图片验证码
    """

    def get(self, request):
        cap = Captcha(request)
        code = cap.getVerificationCode()
        print(code)
        return response_success(data={"code": code})


class UserList(ListModelMixin, viewsets.GenericViewSet):
    """
    获取用户列表
    """
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'role__role_name')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return response_success(data=serializer.data)



class ChangeUserState(APIView):

    def put(self, request, pk):
        data = request.data
        obj = User.objects.get(id=pk)
        obj.state = data["state"]
        obj.save()
        return response_success(data="", message="更新成功~")


class ChangeUserRole(APIView):

    def put(self, request, pk, pk1):

        user_obj = User.objects.get(id=pk)
        role_obj = Role.objects.get(id=pk1)
        user_obj.role = role_obj
        user_obj.save()
        return response_success(data="", message='更新角色成功')


class CustomBackend(ModelBackend):
    """
    用户自定义登录验证,在发送请求时将username的值换成电话号码即可：
    ex：
    {
	"username":"15070070520",
	"password":"admin123"
    }
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class CustomResponseObtainJSONWebToken(ObtainJSONWebToken):
    """
    自定义登录失败时返回类型
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"code": ERROR_USER_RALATION.status_code, "message": ERROR_USER_RALATION.message})


class UserRegisterView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin,GenericViewSet):
    # authentication_classes = ()
    # permission_classes = ()
    """
    自定义用户注册
    """
    # serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action=='create':
            return UserRegSerializer
        else:
            return UserSerializer

    def update(self, request,*args, **kwargs):
        # self.dispatch()
        data = request.data
        instance = self.get_object()
        instance.email = data["email"]
        instance.mobile = data["mobile"]
        instance.save()
        return response_success(data="", message="更新成功~~")


class RolePermissionListView(APIView):
    """
    获取角色列表
    第一层为角色信息
    第二层开始为权限信息，权限一共为3层
    第三层没有children属性
    """

    def get(self, request):

        list = []
        roles = Role.objects.all()
        for role in roles:
            role_dict = {}
            permissions_ = role.permissions.all()
            role_dict["id"] = role.id
            role_dict["role_name"] = role.role_name
            role_dict["role_descripte"] = role.role_descripte
            role_dict["children"] = []
            if permissions_:
                permissions = permissions_.filter(level=1).all()
                for permission in permissions:
                    per_dict = self.handler(permission, 1)
                    permissions_2_ = permission.permission_children.all()
                    if permissions_2_:
                        permissions_2 = permissions_2_.filter(level=2).all()
                        for per_2 in permissions_2:
                            per_2_dict = self.handler(per_2, 1)
                            permissions_3_ = per_2.permission_children.all()
                            if permissions_3_:
                                permissions_3 = permissions_3_.filter(level=3).all()
                                for per_3 in permissions_3:
                                    per_3_dict = self.handler(per_3, 0)
                                    per_2_dict["children"].append(per_3_dict)
                            per_dict["children"].append(per_2_dict)
                    role_dict["children"].append(per_dict)
            list.append(role_dict)
        return response_success(data=list)

    def handler(self, obj, flag):
        tmp_dict = {}
        tmp_dict["id"] = obj.id
        tmp_dict["per_name"] = obj.per_name
        tmp_dict["path"] = obj.path
        tmp_dict["permission_id"] = obj.permission.id
        if flag:
            tmp_dict["children"] = []
        else:
            pass
        return tmp_dict

    def delete(self, request, pk,pk1):
        """
        TODO 当有高级别权限时，该高级别权限下一定要有低级别权限，否则该高级别权限页不应该存在
        :param request:
        :param pk: 角色的ID
        :param pk1: 权限的ID
        :return:
        """
        # 1.删除权限外键id为pk1，角色外键为pk
        # 2.获取删除后重新加载角色权限
        PermissionRole.objects.get(role=pk, id=pk1).delete()
        role = Role.objects.get(id=pk)
        permissions_ = role.permissions.all()
        data = []
        if permissions_:
            permissions = permissions_.filter(level=1).all()
            for permission in permissions:
                per_dict = self.handler(permission, 1)
                permissions_2_ = permission.permission_children.all()
                if permissions_2_:
                    permissions_2 = permissions_2_.filter(level=2).all()
                    for per_2 in permissions_2:
                        per_2_dict = self.handler(per_2, 1)
                        permissions_3_ = per_2.permission_children.all()
                        if permissions_3_:
                            permissions_3 = permissions_3_.filter(level=3).all()
                            for per_3 in permissions_3:
                                per_3_dict = self.handler(per_3, 0)
                                per_2_dict["children"].append(per_3_dict)
                        per_dict["children"].append(per_2_dict)
                data.append(per_dict)
        return response_success(data={})


class PermissionDistribution(APIView):
    """
    给角色分配权限
    """
    def post(self, request,pk):
        """
        :param request:
        :param pk:
        :return:
        """
        permission_keys = request.data
        permission_keys_sort = sorted(permission_keys['keys'])
        PermissionRole.objects.filter(role=pk).delete()
        role = Role.objects.get(id=pk)
        level_3 = []
        for key in permission_keys_sort:
            permission = Permission.objects.get(id=key)
            if permission.level == 1:
                PermissionRole.objects.create(per_name=permission.per_name, level=1, role=role, permission=permission)
            elif permission.level == 2:
                parent_id = permission.children.id
                per_role_id = PermissionRole.objects.get(role=pk, permission=parent_id)
                PermissionRole.objects.create(per_name=permission.per_name, level=permission.level, role=role, children=per_role_id, permission=permission)
            else:
                level_3.append(permission.id)
        for i in level_3:
            permission = Permission.objects.get(id=i)
            parent_id = permission.children.id
            per_role_id = PermissionRole.objects.get(role=pk, permission=parent_id)
            PermissionRole.objects.create(per_name=permission.per_name, level=permission.level, role=role,
                                          children=per_role_id, permission=permission)
        return response_success(data={})


class RoleView(ListModelMixin, GenericViewSet):

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TestSentry(APIView):
    authentication_classes = ()
    permission_classes = ()
    """
    测试sentry
    """

    def get(self, request):
        a = [1, 2, 3]
        for i in range(4):
            print(a[i])
        return response_success(data={"code": 1})
