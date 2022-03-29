from django.urls import path
from .views import RegisterView, LoginView, DashboardView , LogoutView

urlpatterns = [
    path('register/', LoginView.as_view(), name="register-view"),
    path('login/', RegisterView.as_view(), name="login-view"),
    path('dashboard/', DashboardView.as_view(), name="dashboard-view"),
    path('logout/', LogoutView.as_view(), name="logout-view")
]