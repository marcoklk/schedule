"""schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from scheduler.views import AddStaffView, AddUnitView, AddShiftView, LoginView, LogoutView, GrafikView, ListUnitsView, \
    ListShiftView, ListStaffView, AddPartTimeView, AddBaseTimeView, EditUnitView, EditStaffView, AddYearScheduleView, \
    ListYearSchedulesView, FillYearScheduleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GrafikView.as_view(), name="grafik"),
    path('add_staff/', AddStaffView.as_view(), name="add-staff"),
    path('add_unit/', AddUnitView.as_view(), name="add-unit"),
    path('add_shifts/', AddShiftView.as_view(), name="add-shifts"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list_units/', ListUnitsView.as_view(), name='list-units'),
    path('list_shifts/', ListShiftView.as_view(), name='list-shifts'),
    path('list_staff/', ListStaffView.as_view(), name='list-staff'),
    path('parttime/', AddPartTimeView.as_view(), name='parttime'),
    path('basetime/', AddBaseTimeView.as_view(), name='basetime'),
    path('edit_unit/<int:pk>/', EditUnitView.as_view(), name='edit-unit'),
    path('edit_staff/<int:pk>/', EditStaffView.as_view(), name='edit-staff'),
    path('add_yearschedule/', AddYearScheduleView.as_view(), name='add-yearschedule'),
    path('list_yearschedules/', ListYearSchedulesView.as_view(), name='list-yearschedules'),
    path('fill_yearschedule/<int:pk>', FillYearScheduleView.as_view(), name='fill-yearschedule_pk'),
    path('fill_yearschedule/', FillYearScheduleView.as_view(), name='fill-yearschedule'),
]
