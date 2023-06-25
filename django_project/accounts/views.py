from .forms import InputForm, SignUpForm, SignUpForm2
from django.shortcuts import render, redirect
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



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('chat:home')
    else:
        return render(request, 'account_activation_invalid.html')

def loginPageView(request):
    context = {}
    form = InputForm(request.POST or None)
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
                # Limpar a mensagem de erro do contexto
                context.pop('error_message', None)
                return redirect('chat:home')  # Redirecionar para a view 'home' no app 'chat'
            else:
                context['error_message'] = 'Invalid username or password'

    return render(request, 'login.html', context)

import logging


def signupPageView(request):

    logger = logging.getLogger(__name__)
    if request.method == 'POST':
        logger.info("Received POST request")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:account_activation_sent')
    else:
        logger.info("Received GET request")

        form = SignUpForm2()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def logoutPageView(request):
    logout(request)
    return redirect('accounts:login')
