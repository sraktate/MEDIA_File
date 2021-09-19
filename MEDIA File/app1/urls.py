from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('userReg/',views.UserRegisterView,name='sign-up'),
    path('ho/',views.HomeView,name='Home'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "register/reset_password.html"), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "register/password_reset_sent.html"), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "register/password_reset_form.html"), name ='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "register/password_reset_done.html"), name ='password_reset_complete'),
    path('change-password/', views.change_password,name='Change_password'),

]
