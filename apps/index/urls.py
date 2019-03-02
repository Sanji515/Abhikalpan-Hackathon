from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('login/', views.LoginView, name='login'),
	path('logout/', views.LogoutView, name='logout')
]