from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('login/', views.LoginView, name='login'),
	path('logout/', views.LogoutView, name='logout'),
	path('details/<int:id>', views.complaintDetails, name='details'),
	path('new_comment/', views.CommentView, name='comment'),
	path('delete/<int:id>',views.deleteDetails, name ='deleteDetails'),
	path('details/<int:id>', views.complaintDetails, name='details')
]
