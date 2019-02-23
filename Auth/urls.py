from django.urls import path
from . import views

urlpatterns = [
    path('token',views.getToken),
    path('time',views.getTime),

]
