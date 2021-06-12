import json

import time
import datetime

from django.core import serializers
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# 查看所有预约历史记录
from django.views.decorators.csrf import csrf_exempt

from adminWeb.models import SystemConfiguration, EveryDayBookingInfo


def admin_booking_history(request):
    return render(request, './adminWeb/booking_history.html')


# 设置预约信息页面
def admin_setting_booking_info(request):
    system_configurations = SystemConfiguration.objects.filter(Q(configuration_name='allow_booking_date_start') | Q(configuration_name='allow_booking_date_end') | Q(configuration_name='days_showed_at_most_one_time') | Q(configuration_name='maximum_number_per_day'))

    context = {}
    for system_configuration in system_configurations:
        temp = model_to_dict(system_configuration)
        print(temp)
        context[temp['configuration_name']] = temp['configuration_value']

    print(context)
    return render(request, './adminWeb/setting_booking_info.html', context)


# 保存设置预约信息
@csrf_exempt
def admin_save_booking_info(request):
    allow_booking_date_start = request.POST.get('allow_booking_date_start', None)
    if allow_booking_date_start is None or allow_booking_date_start == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递allow_booking_date_start参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    allow_booking_date_end = request.POST.get('allow_booking_date_end', None)
    if allow_booking_date_end is None or allow_booking_date_end == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递allow_booking_date_end参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')

    maximum_number_per_day = request.POST.get('maximum_number_per_day', None)
    if maximum_number_per_day is None or maximum_number_per_day == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递maximum_number_per_day参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')


    # TODO
    # 此处还应该校验截至日期大于等于开始日期


    # 保存设置，不存在则新建
    defaults = dict()
    defaults['configuration_name'] = 'allow_booking_date_start'
    defaults['configuration_value'] = allow_booking_date_start
    result_allow_booking_date_start = SystemConfiguration.objects.update_or_create(defaults=defaults,
                                                                                   configuration_name='allow_booking_date_start')

    defaults = dict()
    defaults['configuration_name'] = 'allow_booking_date_end'
    defaults['configuration_value'] = allow_booking_date_end
    result_allow_booking_date_end = SystemConfiguration.objects.update_or_create(defaults=defaults,
                                                                                 configuration_name='allow_booking_date_end')

    defaults = dict()
    defaults['configuration_name'] = 'maximum_number_per_day'
    defaults['configuration_value'] = maximum_number_per_day
    result_maximum_number_per_day = SystemConfiguration.objects.update_or_create(defaults=defaults,
                                                                                 configuration_name='maximum_number_per_day')

    print(result_allow_booking_date_start)
    print(result_allow_booking_date_end)
    print(result_maximum_number_per_day)

    # update_or_create返回值为元组: (object, created)，
    # object为新建或者更新的对象，
    # created为一个布尔值，表示是新建还是更新，True为新建，False为更新
    context = {}
    context['result_allow_booking_date_start'] = json.dumps(result_allow_booking_date_start[1])
    context['result_allow_booking_date_end'] = json.dumps(result_allow_booking_date_end[1])
    context['result_maximum_number_per_day'] = json.dumps(result_maximum_number_per_day[1])


    # 根据设置生成可预约的日期 start

    # 计算中间有多少个日期
    date_start = time.strptime(allow_booking_date_start,"%Y-%m-%d")
    date_end = time.strptime(allow_booking_date_end,"%Y-%m-%d")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    begin_date = datetime.datetime(date_start[0], date_start[1], date_start[2])
    end_date = datetime.datetime(date_end[0], date_end[1], date_end[2])


    for i in range((end_date - begin_date).days + 1):
        day_start = begin_date + datetime.timedelta(days=i)
        day_end = begin_date + datetime.timedelta(days=i, hours=23, minutes=59, seconds=59, milliseconds=999, microseconds=999)
        print(str(day_start))
        print(str(day_end))

        # 存在则更新，不存在则新建

        defaults = dict()
        defaults['datetime_start'] = day_start
        defaults['datetime_end'] = day_end
        defaults['maximum_number'] = maximum_number_per_day
        # TODO
        # 此处有一个业务BUG，若是之前已经有人预约了，则remain_number因该是maximum_number_per_day-已经预约的人数
        defaults['remain_number'] = maximum_number_per_day

        EveryDayBookingInfo.objects.update_or_create(defaults=defaults, datetime_start=day_start, datetime_end=day_end)

    # 根据设置生成可预约的日期 end

    print(context)

    return_json = {}
    return_json['code'] = 0
    return_json['msg'] = '修改成功'
    return_json['data']= context

    return HttpResponse(json.dumps(return_json), content_type='application/json')

# 设置展示信息页面
def admin_setting_display_info(request):
    system_configurations = SystemConfiguration.objects.filter(Q(configuration_name='days_showed_at_most_one_time'))

    context = {}
    for system_configuration in system_configurations:
        temp = model_to_dict(system_configuration)
        print(temp)
        context[temp['configuration_name']] = temp['configuration_value']

    print(context)
    return render(request, './adminWeb/setting_display_info.html', context)


# 保存设置展示信息
@csrf_exempt
def admin_save_display_info(request):

    days_showed_at_most_one_time = request.POST.get('days_showed_at_most_one_time', None)
    if days_showed_at_most_one_time is None or days_showed_at_most_one_time == '':
        return_json = {}
        return_json['code'] = 1
        return_json['msg'] = '必须传递days_showed_at_most_one_time参数'
        return_json['data'] = {}

        return HttpResponse(json.dumps(return_json), content_type='application/json')




    defaults = dict()
    defaults['configuration_name'] = 'days_showed_at_most_one_time'
    defaults['configuration_value'] = days_showed_at_most_one_time
    result_days_showed_at_most_one_time = SystemConfiguration.objects.update_or_create(defaults=defaults,
                                                                                       configuration_name='days_showed_at_most_one_time')


    print(result_days_showed_at_most_one_time)

    # update_or_create返回值为元组: (object, created)，
    # object为新建或者更新的对象，
    # created为一个布尔值，表示是新建还是更新，True为新建，False为更新
    context = {}
    context['result_days_showed_at_most_one_time'] = json.dumps(result_days_showed_at_most_one_time[1])

    print(context)

    return_json = {}
    return_json['code'] = 0
    return_json['msg'] = '修改成功'
    return_json['data'] = context

    return HttpResponse(json.dumps(return_json), content_type='application/json')

# 查看所有可预约的日期
def admin_valid_dates(request):
    results = EveryDayBookingInfo.objects.all().order_by('datetime_start')

    dates = []
    for date in results:
        temp = model_to_dict(date)
        print(temp)
        dates.append(temp)

    context = {}
    context['dates'] = dates
    print(context)
    return render(request, './adminWeb/valid_dates.html', context)
