from django.db import models
from user.models import User
from django_jalali.db import models as jmodels


class Deal(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    value_transaction = models.IntegerField()
    date = jmodels.jDateTimeField(auto_now_add=True, auto_now=False)

    def calculate_wage(self):
        wage = self.value_transaction/10
        return wage

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.user)
