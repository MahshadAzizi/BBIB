from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView, DetailView
from .models import User
from .forms import LogInForm, AddUserForm
from django.urls import reverse


class LogInView(FormView):
    form_class = LogInForm
    template_name = 'user/login.html'
    success_url = 'Result'

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, "You are now logged in as {}".format(user.username))
            if not user.is_superuser:
                return redirect('Result')
            else:
                return redirect('user_panel')

        messages.error(self.request, "Invalid username or password.")
        return self.render_to_response(self.get_context_data())


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect(reverse('login'))


def user_panel(request):
    if request.method == 'GET':
        user = request.user
        if not user.is_superuser:
            return redirect('Result')
        else:
            form = AddUserForm
            return render(request, 'user/user_panel.html', {'form': form})
    elif request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            form = AddUserForm
            return render(request, 'user/user_panel.html', {'form': form})


class UserList(View):
    """Return list of user"""
    model = User
    template_name = 'user/user_list.html'

    def get(self, request):
        all_user = User.objects.all()
        return render(request, self.template_name, {"all_user": all_user})


class UserDetail(DetailView):
    """Return detail of user"""
    model = User
    context_object_name = 'user'
    template_name = 'user/user_detail.html'


def user_update(request, id):
    instance = User.objects.get(id=id)
    # obj = get_object_or_404(User, id=id)
    form = AddUserForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user/user_update.html', {'form': form})
