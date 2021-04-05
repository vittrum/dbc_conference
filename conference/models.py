from django.db import models

# Create your models here.
from thesis.models import Thesis
from users.models import User


class Conference(models.Model):
    name = models.CharField(max_length=256)
    theme = models.CharField(max_length=256, default='Scientific conference')
    place = models.CharField(max_length=100)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'conferences'

    def __str__(self):
        return self.name


class Schedule(models.Model):
    day = models.DateField()
    begin_time = models.TimeField()
    end_time = models.TimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)

    class Meta:
        db_table = 'schedules'

    def __str__(self):
        return f'{self.thesis} on {self.day} at {self.begin_time}'


class UserConference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=False)
    role = models.CharField(max_length=12, default='observer')

    class Meta:
        db_table = 'users_conferences'

    def __str__(self):
        return self.user.name + ' on ' + self.conference.name