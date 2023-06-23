from django.shortcuts import render

# Create your views here.
def signupPageView(request):
    return render(request, "signup.html")