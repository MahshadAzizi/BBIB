from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from .forms import DealForm
from deal.models import Deal
from .serializers import DealSerializer
from rest_framework import status, permissions
from rest_framework import generics
from user.models import User


class DealView(LoginRequiredMixin, FormView):
    form_class = DealForm
    template_name = 'deal/deal.html'
    success_url = 'Result'

    def form_valid(self, form):
        national_code = form.cleaned_data['national_code']
        branch_code = form.cleaned_data['branch_code']
        value_transaction = form.cleaned_data['value_transaction']
        user = User.objects.filter(national_code=national_code, branch_code=branch_code).first()
        Deal.objects.create(user=user, value_transaction=value_transaction)
        return redirect(self.success_url)


class DealList(generics.ListAPIView):
    model = Deal
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            deal = Deal.objects.all()
            return deal
        else:
            deal = Deal.objects.filter(user=user)
            return deal
