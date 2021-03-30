from django.db import models

# Create your models here.
from dbc_conference.users.models import User


class Thesis(models.Model):
    name = models.CharField(max_length=100)
    short_info = models.CharField(max_length=300)
    is_approved = models.BooleanField(blank=True, null=True, default=None)
    draft = models.BooleanField(default=True)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'thesises'

    def __str__(self):
        return f'{self.name} by {self.user}'


class ThesisReview(models.Model):
    status = models.IntegerField() # add choices
    comment = models.CharField(max_length=300, default='no comment added')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)

    class Meta:
        db_table = 'thesises_reviews'

    def __str__(self):
        return f'{self.user}\'s review of {self.thesis}'