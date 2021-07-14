from django.conf.urls import url
from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.CreateProductsView.as_view(), name='add_product'),
    path('save/', views.Save_confirmation.as_view(), name='save_page'),

]