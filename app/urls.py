from django.urls import path
from . import views

urlpatterns = [
    path('',views.EmployeeApi.as_view()),
    path('register', views.RegisterApi.as_view()),
    path('create',views.EmployeeCreateApi.as_view()),
    path('update/<int:pk>',views.EmployeeUpdateApi.as_view()),
    path('delete/<int:pk>',views.EmployeeDeleteApi.as_view()),
]