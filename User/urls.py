from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'User'

urlpatterns = [
    path('user/', views.CreateUserView.as_view(), name='create_user'),
    path('post/', views.CreatePostView.as_view(), name='create_post'),
    path('user/save/', views.Save_confirmation.as_view(), name='save_page'),
    path('post/save/', views.Save_confirmation.as_view(), name='save_page'),

]