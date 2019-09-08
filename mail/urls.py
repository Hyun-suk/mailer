from django.urls import path

from . import views

app_name='mail'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send_mail, name='send'),
    path('<uuid:promotion_uuid>/', views.check_open, name='check_open'),
]
