from rest_framework.serializers import ModelSerializer

from goods.models import GoodsCategory


class GoodsCategorySerializer2(ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer1(ModelSerializer):

    children = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer(ModelSerializer):

    children = GoodsCategorySerializer1(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"