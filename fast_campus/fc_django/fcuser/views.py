from django.shortcuts import render
from django.views.generic.edit import View
from .forms import RegistrationForms , LoginForm
from django.views.generic.edit import FormView

# Create your views here.
def index(request):
    return render(request=request, template_name="index.html", 
                  context={ "email": request.session.get("user")})

class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegistrationForms
    success_url = "/"
    
class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"
    
    def form_valid(self, form):
        self.request.session["user"] = form.email
        return super().form_valid(form)
        
