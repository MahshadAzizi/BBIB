from django.contrib import admin
from user.models import User
from deal.models import Deal
from .forms import AddUserForm


class AddUserAdmin(admin.ModelAdmin):
    form = AddUserForm
    list_display = ('username', 'password', 'branch_code', 'national_code')


admin.site.register(User, AddUserAdmin)
admin.site.register(Deal)
