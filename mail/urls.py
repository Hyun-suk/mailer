from django.urls import path

from . import views

app_name='mail'
urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customers/<str:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('send/', views.send_mail, name='send'),
    path('settings/', views.settings, name='settings'),
    path('<uuid:promotion_uuid>/', views.check_open, name='check_open'),
]
