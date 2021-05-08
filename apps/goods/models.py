from datetime import datetime

from django.db import models

# Create your models here.


class GoodsCategory(models.Model):
    """
    商品类别表
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    cate_name = models.CharField('类别名称',max_length=100, blank=False, null=False)
    category_type = models.SmallIntegerField('商品分类级别', choices=CATEGORY_TYPE,blank=False, null=False)
    parent_category = models.ForeignKey('self',on_delete=models.CASCADE, related_name='children', blank=True, null=True, help_text='父级类目')
    is_active = models.BooleanField(default=True)
    add_time = models.DateTimeField(default=datetime.now(), help_text='添加时间')

    class Meta:

        db_table = 'goods_category'
        verbose_name = "商品分类表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cate_name


class Goods(models.Model):
    """
    商品表
    """

    name = models.CharField('商品名称',max_length=100, blank=False, null=False)
    goods_sn = models.CharField('商品唯一编号', max_length=50, blank=False, null=False)
    click_num = models.IntegerField("点击数", default=0)
    sold_num = models.IntegerField("商品销售量", default=0)
    fav_num = models.IntegerField("收藏数", default=0)
    goods_num = models.IntegerField("库存数", default=0)
    market_price = models.DecimalField("市场价格", default=0, decimal_places=3,max_digits=11)
    shop_price = models.DecimalField("本店价格", default=0, decimal_places=3,max_digits=11)
    descripte = models.CharField('商品描述', max_length=255, blank=True, null=True)
    goods_front_image = models.CharField(max_length=40, null=True, blank=True, verbose_name="封面图")
    is_hot = models.BooleanField("是否热销", default=False, help_text='是否热销')
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name