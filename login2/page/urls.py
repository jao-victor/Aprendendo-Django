from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.login_user, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('', views.home, name='home'),
    path('logout/',views.user_logout,name = 'logout'),

]
