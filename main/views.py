from django.shortcuts import render,redirect
from .forms import mailForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        form=mailForm()
        return render(request,'home.html',{'form':form})
    def post(self,request):
        form=mailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data.get('subject')
            message=form.cleaned_data.get('message')
            recipient=form.cleaned_data.get('to')
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [recipient],
                      fail_silently=False)
            messages.success(request,'Success!!')
            return redirect('home')

