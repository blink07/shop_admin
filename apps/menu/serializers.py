from rest_framework.serializers import ModelSerializer, Serializer

from menu.models import Menu, Permission


class MenuSerializer2(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer(ModelSerializer):

    sub_cat = MenuSerializer2(many=True)
    # sub_cat = Menu.objects.filter(parent=)

    class Meta:
        model = Menu
        fields = "__all__"

    # def _validated_data(self, data):
    #
    #     # return Menu.objects.get()
    #     print("data:>>>>>>>>>>>>>>>>",data)
    #
    #     return True

    # def create(self, validated_data):
    #     # validated_data.pop("sub_cat")
    #     # parent = Menu.objects.get(id=validated_data["parent"])
    #     return Menu(**validated_data)
    

class PermissionSerializer3(ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"


class PermissionSerializer2(ModelSerializer):
    sub_cat = PermissionSerializer3(many=True)
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionSerializer(ModelSerializer):
    sub_cat = PermissionSerializer2(many=True)

    class Meta:
        model = Permission
        fields = "__all__"
