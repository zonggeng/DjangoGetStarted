from django.db import models


# 继承于django.db.models.Model
class UserMessage(models.Model):
    # 设置最大长度，verbose_name在后台显示字段会用到
    # name = models.CharField(max_length=20, verbose_name=u'用户名')
    # null=True,blank=True指明字段可以为空
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言信息')
    object_id = models.CharField(max_length=50, primary_key=True, verbose_name="主键", default="")

    class Meta:
        verbose_name = u'用户留言信息'
        # verbose_name_plural：复数信息，便于人阅读。否则会在后台显示用户留言信息s
        verbose_name_plural = u"用户留言信息"
        # ordering指定默认排序字段,如：就会以object_id倒序
        ordering = '-object_id'
