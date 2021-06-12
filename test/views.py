import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from test.models import TestUser


def index(request):
    return render(request, './test/index.html')

# 加法页面
def add(request):
    return render(request, './test/add.html')

# 执行加法
def doadd(request):
    a = request.POST['a']
    b = request.POST['b']
    a = int(a)
    b = int(b)
    result = a + b
    # return HttpResponse(str(result))
    context = {}
    context['a'] = a
    context['b'] = b
    context['result'] = result
    return render(request, './test/add_result.html', context)

# 增加用户页面
def testUser(request):
    return render(request, './test/testUser.html')

# 执行增加用户
def testAddUser(request):

    name = request.POST['name']
    level = request.POST['level']
    createTime = datetime.datetime.now()

    user = TestUser.objects.create(name=name, level=level, createTime=createTime)

    context = {}
    context['msg'] = '用户新增成功'
    context['数据库中的id'] = user.id
    return HttpResponse(str(context))

# 数据库查询
def testQueryUser(request):

    total = TestUser.objects.count() # 查询所有数据的总量
    total_condition = TestUser.objects.filter(level=2).count() # 查询符合条件的数据总量
    all_user = TestUser.objects.all() # 查询得到所有用户，使用 all() 方法来查询所有内容。可用索引下标取出模型类的对象。
    all_user_condition = TestUser.objects.filter(level=2) # 查询得到指定条件的所有用户
    all_user_by_order = TestUser.objects.filter(level=2).order_by('createTime') # 按创建时间从小到大排序，-createTime表示从大到小
    a_user_by_id = TestUser.objects.filter(pk=3)  #pk=3 的意思是主键 primary key=3，相当于 id=3。因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。
    just_show_some_fields = TestUser.objects.filter(pk=3).values("pk", "name")  # 只显示id和name者两个字段
    print(just_show_some_fields)

    context = {}
    context['total'] = total # 查询所有数据的总量
    context['total_condition'] = total_condition # 查询符合条件的数据总量
    context['all_user'] = serializers.serialize("json", all_user) # 查询得到所有用户，使用 all() 方法来查询所有内容。可用索引下标取出模型类的对象。
    context['all_user_condition'] = serializers.serialize("json", all_user_condition) # 查询得到指定条件的所有用户
    context['all_user_by_order'] = serializers.serialize("json", all_user_by_order) # 按创建时间从小到大排序，-createTime表示从大到小
    context['a_user_by_id'] = serializers.serialize("json", a_user_by_id)  #pk=3 的意思是主键 primary key=3，相当于 id=3。因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。

    #objects.values()返回django.db.models.query.QuerySet对象，需要将ValuesQuerySet对象需要先转换成list
    context['just_show_some_fields'] = json.dumps(list(just_show_some_fields))  # 只显示id和name者两个字段

    return JsonResponse(context)

# 数据库修改
def testUpdateUser(request):

    # 查询出指定的用户
    userid=request.GET.get('userid', None)
    if userid is None:
        return HttpResponse("必须传递userid参数")

    # 修改前
    before_update = TestUser.objects.filter(pk=userid)  #pk=3 的意思是主键 primary key=3，相当于 id=3。因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。
    context = {}
    context['before_update'] = serializers.serialize("json", before_update)

    # 将该用户的level修改为10，返回值：整数，受影响的行数
    result = TestUser.objects.filter(pk=userid).update(level=10)

    # 修改后
    after_update = TestUser.objects.filter(pk=userid)  #pk=3 的意思是主键 primary key=3，相当于 id=3。因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。

    context['after_update'] = serializers.serialize("json", after_update)
    context['the_number_of_rows_affected'] = result

    return JsonResponse(context)

# 数据库删除
def testDeleteUser(request):

    # 将该用户的level修改为10，返回值：整数，受影响的行数
    result = TestUser.objects.filter(pk__in=[2,3]).delete()

    context = {}
    context['msg'] = "删除成功"
    context['the_number_of_rows_affected'] = result

    return JsonResponse(context)

# 测试cookie页面
def testCookie(request):
    return render(request, './test/testCookie.html')

# 执行测试cookie
def testOperateCookie(request):

    type = request.GET.get('type', None)

    if type == 'set':
        rep = redirect("/testcookie")
        rep.set_cookie("is_login", True)
        return rep

    elif type == 'get':
        context = {}
        context['is_login'] = request.COOKIES.get('is_login')
        return JsonResponse(context)

    elif type == 'delete':
        rep = redirect("/testcookie")
        rep.delete_cookie("is_login")
        return rep

    else:
        return HttpResponse("参数不足")

# 执行测试Session
def testOperateSession(request):

    type = request.GET.get('type', None)

    if type == 'set':
        request.session["is_login"] = True
        request.session["username"] = 'Jeff'

        # 得到所有session项
        context = request.session.items()
        return HttpResponse(context)

    elif type == 'get':
        context = {}
        context['is_login'] = request.session.get('is_login')
        context['username'] = request.session.get('username')
        return JsonResponse(context)

    elif type == 'delete':
        del request.session["is_login"]

        # 得到所有session项
        context = request.session.items()
        return HttpResponse(context)

    elif type == 'flush':
        request.session.flush()

        # 得到所有session项
        context = request.session.items()
        return HttpResponse(context)

    else:
        return HttpResponse("参数不足")