from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^medidor/$', views.MedidorView.as_view(), name='medidor'),

        ]
