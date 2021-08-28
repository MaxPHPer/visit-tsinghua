import datetime
import json

from django.core import serializers
from django.db import transaction
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from adminWeb.models import User, EveryDayBookingInfo, SystemConfiguration, BookingRecord


# 用户端首页
def user_index(request):
    return render(request, './userWeb/index.html')


# 用户注册页
def user_sign(request):

    context = {}
    # 表示来自哪个页面，默认登陆成功后跳转预约页
    context['from_page'] = request.GET.get('from', 'booking')
    return render(request, './userWeb/sign.html', context)


# 用户预约页
def user_booking(request):
    context = {}

    # 判断当前用户是否登陆
    is_login = request.session.get('is_login')
    if is_login:
        context['is_login'] = True
        context['username'] = request.session.get('username')
        # TODO
        # 为了信息安全，将身份证1100000000000000000789变成110*******789
        context['id_card'] = request.session.get('id_card')
    else:
        context['is_login'] = False

    # 查出所有可预约的日期
    system_configuration = SystemConfiguration.objects.filter(configuration_name='days_showed_at_most_one_time').first()
    days_showed_at_most_one_time = int(system_configuration.configuration_value) - 1
    # print(system_configuration.configuration_value)
    # 获取当前时间
    now = datetime.datetime.now()
    # 获取今天零点
    today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                     microseconds=now.microsecond)
    last_day = today + datetime.timedelta(days=days_showed_at_most_one_time, hours=23, minutes=59, seconds=59,
                                          milliseconds=999, microseconds=999)
    # print(today)
    # print(last_day)
    results = EveryDayBookingInfo.objects.filter(datetime_start__range=(today, last_day)).order_by('datetime_start')

    dates = []
    for date in results:
        temp = model_to_dict(date)
        temp['weekday'] = temp['datetime_start'].strftime('%A')
        print(temp)
        dates.append(temp)

    # TODO
    # 未设置的日期在数据库中没有记录，所以，为了美观，可以考虑补齐不存在的日期

    context['dates'] = dates
    print(len(dates))

    # 前端4个一行，不足4个则补足
    if len(dates) % 4 == 0:
        context['need_to_add_blank_grids'] = 0
    else:
        context['need_to_add_blank_grids'] = 4 - len(dates) % 4

    # 因为前端模板for循环只能循环列表，所以用range生成
    context['blank_range'] = range(4 - len(dates) % 4)

    print(context)

    return render(request, './userWeb/booking.html', context)


# 保存用户信息
@csrf_exempt
def save_user_info(request):
    # TODO
    # 此处省略了身份认证的代码

    username = request.POST.get('username', None)
    if username is None or username == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递username参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    id_card = request.POST.get('id_card', None)
    if id_card is None or id_card == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递id_card参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    defaults = dict()
    defaults['username'] = username
    defaults['id_card'] = id_card
    # 可自主开发更新用户的其它信息
    # defaults['identity_authentication_type'] = 1
    result = User.objects.update_or_create(defaults=defaults, id_card=id_card)

    print(result)

    context = {}
    context['result'] = json.dumps(result[1])

    # 查询出该用户的详细信息
    user = User.objects.filter(id_card=id_card).first()

    # print(user.id)
    # print(user.username)
    # print(user.id_card)
    # 可以将必要的信息写入到session中，方便其他功能使用
    if user:
        request.session["is_login"] = True
        request.session["id_card"] = user.id_card
        request.session["user_id"] = user.id
        request.session["username"] = user.username

    print(context)

    return_json = {}
    return_json['code'] = 0
    return_json['msg'] = '保存成功'
    return_json['data'] = context

    return HttpResponse(json.dumps(return_json), content_type='application/json')


# 保存用户的预约信息
@csrf_exempt
def save_booking(request):
    # 校验是否已经登陆
    if request.session.get('is_login') is None:
        return_json = {}
        return_json['code'] = 2
        return_json['msg'] = '必须先实名登陆'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    selected_date_id = request.POST.get('selected_date_id', None)
    if selected_date_id is None or selected_date_id == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递selected_date_id参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    # 查询出该时间段的详情
    date = EveryDayBookingInfo.objects.filter(id=selected_date_id).first()
    selected_date = model_to_dict(date)
    print(selected_date)

    # TODO
    # 此处省略了校验该用户是否重复预约，同学们可以自己补充

    # 若该时间段没有被预约完，则扣减1
    update_result = EveryDayBookingInfo.objects.filter(id=selected_date_id).update(remain_number=(selected_date['remain_number']-1))

    # 将预约记录保存到数据库中
    add_result = BookingRecord.objects.create(user_id=request.session.get('user_id'),
                                          username=request.session.get('username'), datetime_id=selected_date['id'],
                                          datetime_start=selected_date['datetime_start'],
                                          datetime_end=selected_date['datetime_end'],
                                          submit_datetime=datetime.datetime.now(), is_main_order=1, main_order_id=0,
                                          status=1)
    result = {}
    result['update_result'] = update_result
    result['add_result'] = add_result.id

    # TODO
    # 此处省略了处理同行人的代码

    return_json = {}
    return_json['code'] = 0
    return_json['msg'] = '保存成功'
    return_json['data'] = result
    return HttpResponse(json.dumps(return_json), content_type='application/json')


# 用户端我的预约
def my_booking_history(request):

    # 校验是否已经登陆
    if request.session.get('is_login') is None:
        return_json = {}
        return_json['code'] = 2
        return_json['msg'] = '必须先实名登陆'
        return_json['data'] = {}

        return redirect("/userweb/sign?from=mybookinghistory")

    results = BookingRecord.objects.filter(user_id=request.session.get('user_id')).order_by('-submit_datetime')

    booking_records = []
    for booking_record in results:
        temp = model_to_dict(booking_record)
        print(temp)
        booking_records.append(temp)

    context = {}
    context['booking_records'] = booking_records
    print(context)
    return render(request, './userWeb/my_booking_history.html', context)


# 用户端登出
def user_logout(request):
    request.session.flush()
    return render(request, './userWeb/index.html')
