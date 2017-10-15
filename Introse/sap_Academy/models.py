from django.db import models
from django.contrib.auth.models import User

work_position = models.CharField(max_length=50, blank=True)
employee_num = models.IntegerField(blank=True, default=0)
employee_num.contribute_to_class(User, 'employee_num')
work_position.contribute_to_class(User, 'work_position')




class Students(models.Model):
    sap_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.CharField(max_length=128)
    group_number = models.IntegerField(default=1)
    territory = models.CharField(max_length=16)
    country = models.CharField(max_length=16)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    training_program = models.CharField(max_length=128)

    def __str__(self):
        return self.last_name


class Events(models.Model):
    event_id = models.IntegerField(default=0)
    event_name = models.CharField(max_length=256)
    event_date = models.DateField(auto_now=False)
    time_start = models.DateTimeField(auto_now=False)
    time_end = models.DateTimeField(auto_now=False)
    hex_id = models.IntegerField(default=0)
    event_comment = models.CharField(max_length=256)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.event_name


class Grades(models.Model):
    sap_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    attendance = models.BooleanField()
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.sap_id


class Activities(models.Model):
    activity_id = models.IntegerField(default=0)
    activity_name = models.CharField(max_length=64)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    group_number = models.IntegerField(default=1)
    week_number = models.IntegerField(default=1)

    def __str__(self):
        return self.activity_name


class Notes(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=256)
    note_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
