from django.db import models


# 系统配置表
class SystemConfiguration(models.Model):
    id = models.AutoField(primary_key=True)  # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增。id无需在save中创建，数据表自动添加
    configuration_name = models.CharField(max_length=50)
    configuration_value = models.CharField(max_length=50)

    class Meta:
        db_table = 'SystemConfiguration'


# 可预约日期表
class EveryDayBookingInfo(models.Model):
    id = models.AutoField(primary_key=True)  # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增。id无需在save中创建，数据表自动添加
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    maximum_number = models.IntegerField(default=0)
    remain_number = models.IntegerField(default=0)

    class Meta:
        db_table = 'EveryDayBookingInfo'


# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)  # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增。id无需在save中创建，数据表自动添加
    username = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    identity_authentication_type = models.IntegerField(default=0)
    wechat_open_id = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)
    user_role = models.IntegerField(default=1)

    NO_AUTHENTICATION = 0
    FACE_AUTHENTICATION = 1
    PAYMENT_AUTHENTICATION = 2

    ORDINARY_USER = 1
    TICKET_INSPECTOR = 2
    SYSTEM_ADMINISTRATOR = 3

    class Meta:
        db_table = 'User'


# 预约记录表
class BookingRecord(models.Model):
    id = models.AutoField(primary_key=True)  # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增。id无需在save中创建，数据表自动添加
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    datetime_id = models.IntegerField()
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    submit_datetime = models.DateTimeField()
    is_main_order = models.IntegerField(default=1)
    main_order_id = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    processed_datetime = models.DateTimeField(null=True)

    MAIN_ORDER = 1
    SIDE_ORDER = 0

    STATUS_CANCELLED = 0
    STATUS_VALID = 1
    STATUS_CHECKED = 2

    class Meta:
        db_table = 'BookingRecord'
