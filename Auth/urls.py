from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth),
    path('token',views.getToken),

]
