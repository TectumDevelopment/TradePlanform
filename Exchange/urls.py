from django.urls import path
from . import views

urlpatterns = [
    path('assets/create' , views.createAsset  )
]
