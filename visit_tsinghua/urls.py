"""visit_tsinghua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test.views import *
from userWeb.views import *
from adminWeb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path("add", add),
    path("doadd", doadd),
    path("testuser", testUser),
    path("testadduser", testAddUser),
    path("testqueryuser", testQueryUser),
    path("testupdateuser", testUpdateUser),
    path("testdeleteuser", testDeleteUser),
    path("testcookie", testCookie),
    path("testoperatecookie", testOperateCookie),
    path("testoperatesession", testOperateSession),

    path("userweb/index", user_index),
    path("userweb/sign", user_sign),
    path("userweb/booking", user_booking),
    path("userweb/save_user_info", save_user_info),
    path("userweb/save_booking", save_booking),
    path("userweb/my_booking_history", my_booking_history),
    path("userweb/logout", user_logout),

    path("adminweb/bookinghistory", admin_booking_history),
    path("adminweb/settingbookinginfo", admin_setting_booking_info),
    path("adminweb/save_booking_info", admin_save_booking_info),
    path("adminweb/settingdisplayinfo", admin_setting_display_info),
    path("adminweb/save_display_info", admin_save_display_info),
    path("adminweb/validdates", admin_valid_dates),

]
