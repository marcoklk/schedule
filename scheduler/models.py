from django.db import models

STAFF_TYPE = (
       (1, "pielęgniarka"),
       (2, "pomocniczy"),
       (3, "lekarz"),
       (4, "psycholog"),
       (5, "psychoterapeuta"),
)

EMPLOYEE_TYPE = (
       (1, "wewnętrzny"),
       (2, "zewnętrzny"),
       (3, "kontraktowy"),
)


# pracownik
class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    npwz = models.CharField(max_length=12, blank=True)
    pesel = models.CharField(max_length=11, blank=True)
    staff_type = models.IntegerField(choices=STAFF_TYPE)
    employee_type = models.IntegerField(choices=EMPLOYEE_TYPE)
    begin_work = models.DateField()
    end_work = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        # return u'%s %s' % (self.first_name, self.last_name)

# wymiar etatu (dokładność 4 miejsca po przecinku): od 0 do 1
class PartTime(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    part_time = models.DecimalField(max_digits=5, decimal_places=4)
    begin = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.staff.first_name} {self.staff.last_name}'

# podstawa wymiaru czasu pracy np. dla 8 godzin to 480 minut
class BaseTime(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    base_time = models.DecimalField(max_digits=3, decimal_places=0)
    begin = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.staff.first_name} {self.staff.last_name}'

# jednostka organizacyjna
class Unit(models.Model):
    name = models.CharField(max_length=64)
    description =  models.CharField(max_length=128)
    code = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.name}'

# typy dyżurów
class Shift(models.Model):
    name = models.CharField(max_length=4)
    describe = models.CharField(max_length=128)
    minutes = models.IntegerField()
    shift_begin = models.TimeField()
    shift_end = models.TimeField()

    def __str__(self):
        return f'{self.name}'
        # return u'%s' % (self.name)

class YearSchedule(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=128)
    staff = models.ManyToManyField(Staff)

    def __str__(self):
        return f'{self.year} {self.name}'
        # return u'%d %s' % (self.year, self.name)

#plan pracy na dany dzień dla danego pracownika
class Schedule(models.Model):
    date_day = models.DateField()
    # no_day = models.IntegerField() # wyliczać na podstawie daty, z uwzględnieniem pierwszy dzień kwartału
    plan_day = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='plan_id')
    done_day = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='done_id')
    # part_time = models.ForeignKey(PartTime, on_delete=models.CASCADE)
    # base_time = models.ForeignKey(BaseTime, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    yearschedule = models.ForeignKey(YearSchedule, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff.first_name} {self.staff.last_name}'