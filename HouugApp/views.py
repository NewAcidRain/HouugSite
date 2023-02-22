from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterUserFrom



def startPage(request):
    return render(request,"html/startpage.html")


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'html/login.html'
    # def form_valid(self, form):
    #     get_user = self.request.POST['username']
    #     try:
    #         Users.objects.get(user__username=get_user)
    #     except:
    #         Users.objects.create(user=User.objects.get(username=get_user),current_course=None,photo=None)
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse_lazy('main')

class RegisterUser(CreateView):
    form_class = RegisterUserFrom
    template_name = 'html/registration.html'
    success_url = reverse_lazy('login')
