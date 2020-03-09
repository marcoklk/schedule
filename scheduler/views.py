from datetime import timedelta, date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Permission, AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, resolve, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from scheduler.forms import *
from scheduler.models import *


class GrafikView( LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'grafik.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html',
                      {'form': form, 'submit_value': "Zaloguj", "title": "Logowanie"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                path = request.GET.get("next")
                print('Scieżka', path)
                if path is not None:
                    return redirect(path)
                return redirect('/')
            else:
                return HttpResponse("Błędny login lub hasło")
        return HttpResponse("Błąd walidacji danych")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login')


class AddStaffView(View):
    def get(self, request):
        form = AddStaffForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie pracownika"})

    def post(self, request):
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list_staff/', {'form': form})
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie pracownika"})

class AddUnitView(View):
    def get(self, request):
        form = AddUnitForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie jednostki organizacyjnej"})

    def post(self, request):
        form = AddUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list_units/', {'form': form})
            # return render(request, 'grafik/grafik.html')
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie jednostki organizacyjnej"})

class AddShiftView(View):
    def get(self, request):
        form = AddShiftForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie rodzaju dyżuru"})

    def post(self, request):
        form = AddShiftForm(request.POST)
        if form.is_valid():
            form.save()
            path = request.GET.get("next")
            print('Scieżka', path)
            if path is not None:
                return redirect(path)
            return redirect('list-shifts')
            # return HttpResponse("Dodano dyżur")
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie rodzaju dyżuru"})



class AddPartTimeView(View):
    def get(self, request):
        form = AddPartTimeForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie wymiaru etatu"})

    def post(self, request):
        form = AddPartTimeForm(request.POST)
        if form.is_valid():
            form.save()
            path = request.GET.get("next")
            print('Scieżka', path)
            if path is not None:
                return redirect(path)
            return redirect('/')
            # return HttpResponse("Dodano pracownika")
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie wymiaru etatu"})


class AddBaseTimeView(View):
    def get(self, request):
        form = AddBaseTimeForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie normy czasu pracy"})

    def post(self, request):
        form = AddBaseTimeForm(request.POST)
        if form.is_valid():
            form.save()
            path = request.GET.get("next")
            print('Scieżka', path)
            if path is not None:
                return redirect(path)
            return redirect('/')
            # return HttpResponse("Dodano pracownika")
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie normy czasu pracy"})


class AddYearScheduleView(View):
    def get(self, request):
        form = AddYearScheduleForm()
        return render(request, 'form.html',
                      {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie nowego grafiku"})

    def post(self, request):
        form = AddYearScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            path = request.GET.get("next")
            print('Scieżka', path)
            if path is not None:
                return redirect(path)
            return redirect('list-yearschedules')
        else:
            return render(request, 'form.html',
                          {'form': form, 'submit_value': "Dodaj", "title": "Dodawanie nowego grafiku"})


class EditStaffView(View):
    def get(self,request, pk):
        form = AddStaffForm(instance=Staff.objects.get(pk=pk))
        return render(request, 'form.html', {'form': form, 'submit_value': "Zatwierdź", 'title': "Edycja personelu"})

    def post(self, request, pk):
        form = AddStaffForm(request.POST,instance=Staff.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('/list_staff', {'form':form})
        else:
            return render(request, 'form.html', {'form': form, 'submit_value':"Zatwierdź",'title': "Edycja personelu"})


class EditUnitView(View):
    def get(self,request, pk):
        form = AddUnitForm(instance=Unit.objects.get(pk=pk))
        return render(request, 'form.html', {'form': form, 'submit_value': "Zatwierdź", 'title': "Edycja jednostki organizacyjnej"})

    def post(self, request, pk):
        form = AddUnitForm(request.POST,instance=Unit.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('/list_units', {'form':form})
        else:
            return render(request, 'form.html', {'form': form,'submit_value': "Zatwierdź", 'title': "Edycja jednostki organizacyjnej"})


class FillYearScheduleView(View):
    def get(self,request, pk):
        form = FillScheduleForm()
        yearschedule = YearSchedule.objects.get(pk=pk)
        staff = yearschedule.staff.all()
        year = yearschedule.year
        days = []
        day = date(year,1,1)
        while day < date(year+1,1,1):
            days.append(day)
            day += timedelta(days=1)
        schedules = Schedule.objects.filter(yearschedule=yearschedule)
        # print(schedules)
        schedules_by_staff = {}
        for employee in staff:
            schedules_by_staff[employee] = {}
            for day in days:
                schedules_by_staff[employee][day] = schedules.filter(date_day= day, staff=employee).first()
        # print(schedules_by_staff)
        return render(request, 'fill_yearschedule.html', {'form': form, 'yearschedule': yearschedule,
                                 'days': days, 'staff':staff, 'schedules_by_staff': schedules_by_staff})

    def post(self, request, pk):
        form = FillScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fill_yearschedule', {'pk':pk})
        else:
            return redirect('/fill_yearschedule', {'pk':pk})


class ListUnitsView(ListView):
    model = Unit
    template_name = 'list_units.html'


class ListShiftView(ListView):
    model = Shift
    template_name = 'list_shifts.html'


class ListStaffView(ListView):
    model = Staff
    template_name = 'list_staff.html'


class ListYearSchedulesView(ListView):
    model = YearSchedule
    template_name = 'list_yearschedules.html'


class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('list-staff')

class UnitDeleteView(DeleteView):
    model = Unit
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('list-units')

class ShiftDeleteView(DeleteView):
    model = Unit
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('list-shifts')

class YearScheduleDeleteView(DeleteView):
    model = YearSchedule
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('list-yearschedules')