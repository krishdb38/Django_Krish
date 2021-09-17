from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('homework/', views.homework, name="homework"),
    path("homework2/<int:pk>", views.HomeworkDetailView.as_view(), name="homework2"),
    path("section_list/", views.SectionListView.as_view(), name="section_list"),
    path('profile_detail/<int:pk>',
         views.ProfileDetailView.as_view(), name="profile_detail")
]
