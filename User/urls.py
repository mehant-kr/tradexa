from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'User'

urlpatterns = [    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('user/', views.CreateUserView.as_view(), name='create_user'),
    path('post/', views.CreatePostView.as_view(), name='create_post'),
    path('user/save/', views.Save_confirmation.as_view(), name='save_page'),
    path('post/save/', views.Save_confirmation.as_view(), name='save_page'),

]