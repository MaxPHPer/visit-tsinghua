from django.db import models


class TestUser(models.Model):
    id = models.AutoField(primary_key=True) # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增。id无需在save中创建，数据表自动添加
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1) # 用户等级，默认1
    createTime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'TestUser' # 数据表名称