from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate,  logout
from .tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib import messages
import logging


def activate(request, uidb64, token):
    # called from activation link
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token): # check token validity
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend') # user login
        return redirect('chat:home')
    else:
        return redirect(reverse('accounts:login'))


def loginPageView(request):
    # create from
    context = {}
    form = LoginForm(request.POST or None)
    context['form'] = form
    context['form_submitted'] = False

    if request.method == 'POST':
        context['form_submitted'] = True
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat:home')
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', context)

def signupPageView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # prevent login
            user.save()
            print(request)
            # current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': get_current_site(request),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message) # send message for user email
            return redirect('accounts:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def logoutPageView(request):
    logout(request)
    return redirect(reverse('accounts:login'))