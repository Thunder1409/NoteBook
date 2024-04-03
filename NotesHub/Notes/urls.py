from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('save/', views.save, name='save'),
    path('delete/', views.delete, name='delete'),
    path('open/', views.open, name='open'),
    path('new/', views.new, name='new'),
    path('test/', views.test, name='test'),

]