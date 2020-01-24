from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('password_change/',
         views.MyPasswordChangeView.as_view(
             #success_url=reverse_lazy('profile'),  # 암호 변경되면 그냥 프로필로 넘어가게
             #template_name='accounts/password_change_form.html'
         ), name='password_change'),

    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'
    # ), name='password_change_done'),
]
