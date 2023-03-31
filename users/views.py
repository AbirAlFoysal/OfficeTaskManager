from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login
from taskManager.models import *

from .models import *
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
# from verify_email.email_handler import send_verification_email


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    # def dispatch(self, request, *args, **kwargs):
    #     # will redirect to the home page if a user tries to access the register page while logged in
    #     if request.user.is_authenticated:
    #         return redirect(to='/')

    #     # else process dispatch as it otherwise normally would
    #     return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm
    success_message = "Welcome to ParkingBD!"
    def form_valid(self, form):
        
        remember_me = form.cleaned_data.get('remember_me')
        

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


class EditProfile(UpdateView):
    model = Profile
    # fields = ['name']
    template_name = 'users/edit-profile.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')


def profile(request, pk):
    profile = Profile.objects.get(user=pk)
    return render(request, 'users/profile.html', {'profile': profile})


def profileList(request):
    profile = Profile.objects.all().order_by('-username')
    context = {'profile': profile}
    return render(request, 'users/allmembers.html', context)