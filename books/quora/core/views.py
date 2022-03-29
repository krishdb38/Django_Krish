
from django.shortcuts import render, redirect #, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth import authenticate
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from .models import User
from questans.models import Questions, Answers, QuestionGroups
from .forms import  LoginForm, RegisterForm

#https://books.agiliq.com/projects/djenofdjango/en/latest/chapter6.html
# Create your views here.

class DashboardView(FormView):
    
    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Questions.objects.filter(user = user)
            content['userdetail'] = user
            content['questions'] = ques_obj
            ans_obj = Answers.objects.filter(questions = ques_obj[0])
            content["Answers"] = ans_obj
            
            return render(request, 'dashboard.html', content )
        else:
            return redirect(reverse('dashboard-view'))


class RegisterView(FormView):
    
    @method_decorator
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)
    
    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'core/register.html'
        return render(request, template, content)
    
class LoginView(FormView):
    content = {}
    content['form'] = LoginForm
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        content["form"] = LoginForm
        return render(request, 'login.html', content)
        
    def post(self, request):
        content = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username= users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = "Unable to login with provided credentials" + e
            return render( None, 'login.html', content)
        
class LogoutView(FormView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
            